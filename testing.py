import sentry_sdk
sentry_sdk.init(
	dsn='https://5a47dfa361a44e35aa933b700c9c9e46@sentry.io/1499922',
	release='abc555'
	)
im_gonna_break = 1 / 0