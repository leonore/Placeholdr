# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['placeholdr.pythonanywhere.com']

# HTTPS redirect
SECURE_SSL_REDIRECT = True

# Secure iframes
SECURE_FRAME_DENY = True

# X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

# X-Content-Type-Options: nosniff
SECURE_CONTENT_TYPE_NOSNIFF = True

# Cookie security
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# CSP
CSP_DEFAULT_SRC = ("'self'", 'cdnjs.cloudflare.com')
CSP_IMG_SRC = ('*')

# Referer Policy
REFERRER_POLICY = "same-origin"

# HSTS
SECURE_HSTS_SECONDS = 15552000