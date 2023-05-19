from pathlib import Path
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-gj^f*2cm_37t_z!8$%99phnv_)86k7_a=f$^%+5_9pine2i&ui'

SITE_ID = 1

DEBUG = True

ALLOWED_HOSTS = [
    #
    'discover.io',
    #
    'localhost',
    '127.0.0.1'
]

LOGIN_REDIRECT_URL = 'accounts_app:dashboard'
LOGIN_URL = 'accounts_app:login'
LOGOUT_URL = 'accounts_app:logout'
# LOGOUT_REDIRECT_URL = 'accounts_app:logout'

INSTALLED_APPS = [
    #
    'accounts_app',
    #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'django.contrib.sites',
    #
    'django_extensions',
    #
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #
    'allauth.socialaccount.providers.google',
    #
    'crispy_forms',
    #
    'crispy_bootstrap5'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'discover.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'discover.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [
    #
    'django.contrib.auth.backends.ModelBackend',
    #
    'allauth.account.auth_backends.AuthenticationBackend',
    #
    'accounts_app.backends.create_profile',
    #
    'accounts_app.backends.EmailAuthBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'APP': {
            'client_id': '279331855250-hfncl9r1u99lldg2ho0nqlmmlsg630n6.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        'AUTH_PARAMS': {
            'access_type': 'offline',
        },
        # 'OAUTH_PKCE_ENABLED': True
    }
}

# ACCOUNT_ADAPTER = 'allauth.account.adapter.DefaultAccountAdapter'
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
# ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = settings.LOGIN_URL
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
# ACCOUNT_EMAIL_REQUIRED = False
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Site]'
# # ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'
# ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 60
# ACCOUNT_EMAIL_MAX_LENGTH = 254
# ACCOUNT_MAX_EMAIL_ADDRESSES = 2 # default=None



# SOCIALACCOUNT_ADAPTER = 'allauth.socialaccount.adapter.DefaultSocialAccountAdapter'
# SOCIALACCOUNT_AUTO_SIGNUP = True
# SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION
# SOCIALACCOUNT_EMAIL_REQUIRED = ACCOUNT_EMAIL_REQUIRED
# SOCIALACCOUNT_LOGIN_ON_GET = False
# SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
# # SOCIALACCOUNT_SOCIALACCOUNT_STR = str of user object
# SOCIALACCOUNT_STORE_TOKENS = False







