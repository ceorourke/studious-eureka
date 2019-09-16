import sentry_sdk
from sentry_sdk import capture_message
from sentry_sdk import capture_exception
from sentry_sdk import configure_scope
import time
import os

sentry_sdk.init(
	dsn='https://5d0ad1da55464d9e822c593677e76435@sentry.io/1232413',
    # dsn=os.environ.get('SENTRY_DSN'),
    release=os.environ.get('VERSION')
)

with configure_scope() as scope:
    scope.user = {"email": "testing@example.com"}

try:
    hi_there()
except Exception as e:
    capture_exception(e)
raise