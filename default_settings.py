import os


UBER_BASE_API_URL = 'https://api.uber.com/v1'
UBER_AUTHORIZATION_ENDPOINT = 'https://login.uber.com/oauth/v2/authorize'
UBER_TOKEN_ENDPOINT = 'https://login.uber.com/oauth/v2/token'
UBER_CLIENT_ID = os.environ['UBER_CLIENT_ID']
UBER_CLIENT_SECRET = os.environ['UBER_CLIENT_SECRET']

IFTTT_MAKER_KEY = os.environ['IFTTT_MAKER_KEY']
