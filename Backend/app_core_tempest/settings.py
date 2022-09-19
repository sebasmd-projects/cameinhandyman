from unipath import Path

from app_core_tempest.get_value_from_json import get_value

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).ancestor(2)
print("BASE_DIR: ", BASE_DIR)

# Select the appropriate environment
environment = f"{get_value('ENVIRONMENT')}"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_value('SECRET_KEY')

# Global URL
BASE_URL = get_value('BASE_URL')[environment]

# Debug mode
if environment == 'prod':
    DEBUG = False
else:
    DEBUG = True

# SSL Redirect
if environment == 'prod' or environment == 'dev':
    SECURE_SSL_REDIRECT = True
else:
    SECURE_SSL_REDIRECT = False

# Allowed hosts
ALLOWED_HOSTS = get_value('ALLOWED_HOSTS')[environment]

# Cors Allowed Origins
CORS_ALLOWED_ORIGINS = get_value('CORS_ALLOWED_ORIGINS')[environment]

# Database | https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'CONN_MAX_AGE': get_value('DB_CONN_MAX_AGE'),
        'ENGINE': get_value('ENGINE'),
        'NAME': get_value('NAME'),
        'USER': get_value('USER'),
        'PASSWORD': get_value('PASSWORD'),
        'HOST': get_value('HOST'),
        'PORT': get_value('PORT'),
    }
}

# Email Configuration
# https://docs.djangoproject.com/en/4.0/topics/email/
EMAIL_BACKEND = get_value('EMAIL_BACKEND')

# Email security
if bool(get_value('EMAIL_USE_SSL')) == True:
    EMAIL_USE_SSL = bool(get_value('EMAIL_USE_SSL'))

elif bool(get_value('EMAIL_USE_TLS')) == True:
    EMAIL_USE_TLS = bool(get_value('EMAIL_USE_TLS'))

# Email Host
EMAIL_HOST = get_value('EMAIL_HOST')

# Email Port
EMAIL_PORT = get_value('EMAIL_PORT')

# Email User
EMAIL_HOST_USER = get_value('EMAIL_HOST_USER')

# Email Password
EMAIL_HOST_PASSWORD = get_value('EMAIL_HOST_PASSWORD')

# Email Default From
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Application definition
# Django Apps
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Third-party Apps
THIRD_PARTY_APPS = (
    'rest_framework',
    'corsheaders',
    'import_export',
    'ckeditor',
)

# Local Apps
LOCAL_APPS = (
    'apps.dynamicform',
    'apps.backendApps.api_guide',
    'apps.backendApps.home'
)

# Join all apps
INSTALLED_APPS = INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root Path Configuration
ROOT_URLCONF = 'app_core_tempest.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('public', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.context_processors.custom_processors',
            ],
        },
    },
]

# WSGI application configuration
WSGI_APPLICATION = 'app_core_tempest.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = get_value('LANGUAGE_CODE')

TIME_ZONE = get_value('TIME_ZONE')

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CKEditor configuration
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': [
                'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}
