from flask import Flask
from flask_oauth import OAuth


app = Flask(__name__)
app.config.from_object('ifttt_uber.default_settings')
app.config.from_envvar('IFTTT_UBER_SETTINGS')


oauth = OAuth(app)
uber_api = oauth.remote_app(
    'uber',
    base_url=app.config.get('UBER_BASE_API_URL'),
    request_token_url=None,
    authorize_url=app.config.get('UBER_AUTHORIZATION_ENDPOINT'),
    access_token_url=app.config.get('UBER_TOKEN_ENDPOINT'),
    consumer_key=app.config.get('UBER_CLIENT_ID'),
    consumer_secret=app.config.get('UBER_CLIENT_SECRET')
)


@app.route('/')
def index():
    if 'uber_access_token' in session:
        me = uber_api.get('/me')
        return jsonify(me.data)
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return uber_api.authorize(callback=url_for('authorized', _external=True))


@app.route('/login/authorized')
def authorized():
    resp = uber_api.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error'],
            request.args['error_description']
        )
    session['uber_access_token'] = (resp['access_token'], '')
    me = uber_api.get('/me')
    return jsonify(me.data)


@uber_api.tokengetter
def get_uber_oauth_token():
    return session.get('uber_access_token')


@app.route('/trip_update')
def trip_update():
    event = json.loads(request.data)
    if (
        event.get('event_type') == 'all_trips.status_changed' and
        event.get('meta')
    ):
        status = event.get('meta', {}).get('status')
        requests.post(
            'https://maker.ifttt.com/trigger/{status}/with/key/{maker_key}'.format(
                status=status, maker_key=app.config.get('IFTTT_MAKER_KEY')
            )
        )
    return request.data
