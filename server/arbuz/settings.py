import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eunq8#$v(#15yjrd1rip6a=-vech-ptmpxq+_zqoa&n(vr5%k@'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']
DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.sites', # For include sites
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'server.arbuz',
    'server.main',
    'server.session',
    'server.translator',

)

MIDDLEWARE_CLASSES = [
    'subdomains.middleware.SubdomainURLRoutingMiddleware', # Subdomain package
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 1
ROOT_URLCONF = 'server.arbuz.urls.en'

SUBDOMAIN_URLCONFS = {
    None: 'server.arbuz.urls.en',
    'en': 'server.arbuz.urls.en',
    'pl': 'server.arbuz.urls.pl',
    'de': 'server.arbuz.urls.de',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'html'),
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

WSGI_APPLICATION = 'server.arbuz.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'spasungate',
        'USER':     'spasungate',
        'PASSWORD': 'szczypiorek&spasungate',
        'HOST':     'localhost',
        'PORT':     '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us' # pl/de/en-us
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'client', 'static'),
)


SESSION_ENGINE = "django.contrib.sessions.backends.cache"
 
# geoip2
GEOIP_PATH = os.path.join(BASE_DIR, 'server', 'arbuz', 'geoip')

# Other
SESSION_SAVE_EVERY_REQUEST = True
DISPLAY_STATUS = True
