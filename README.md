# ifttt_uber

`ifttt_uber` is a tiny Flask app that registers a webhook to listen for [Uber trip events](https://developer.uber.com/docs/webhooks). It also forwards these events to an [IFTTT Maker channel](https://ifttt.com/maker) so that they can be used to trigger various actions.

In order to get this to work for you, you'll need the following:
- An Uber account,
- An IFTTT account
- Somewhere to host the service (Heroku, DigitalOcean)
