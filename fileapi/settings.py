"""
Django settings for fileapi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DEFAULT_SECRET_KEY = '7clb$a&c(*ter7=+bo-vn=43d3jrjxo#l(n+ysw^6#4t&5t&fj'

SECRET_KEY = os.environ.get('SECRET_KEY', DEFAULT_SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'on') == 'on'

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(';')

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'fileapi',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fileapi.urls'

WSGI_APPLICATION = 'fileapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3'))
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


def jwt_decode_handler(token):
    """Customized handler to fix compatibility with pyJWT 1.0+"""
    import jwt
    from jwt_auth import settings as jwt_settings
    options = {
        'verify_exp': jwt_settings.JWT_VERIFY_EXPIRATION,
    }
    return jwt.decode(
        token,
        key=jwt_settings.JWT_SECRET_KEY,
        verify=jwt_settings.JWT_VERIFY,
        algorithms=[jwt_settings.JWT_ALGORITHM, ],
        leeway=jwt_settings.JWT_LEEWAY,
        options=options)

JWT_DECODE_HANDLER = jwt_decode_handler
