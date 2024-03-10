import os
from dotenv import load_dotenv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

SECRET_KEY = 'django-insecure-@tmnx8_=o(3a=i6l#ac&sm3(2==)taolup8l&m=#y$vowl447y'
DEBUG = True
ALLOWED_HOSTS = []

# SECRET_KEY = os.getenv('SECRET')
# DEBUG = False

# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')
# CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS').split(' ')

# SECURE_SSL_REDIRECT = \
#     os.getenv('SECURE_SSL_REDIRECT', '0').lower() in ['true', 't', '1']
# if SECURE_SSL_REDIRECT:
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
# CORS_ALLOWED_ORIGINS = [
#     "https://theiosdivinusaltarchurch.org",
#     "https://www.theiosdivinusaltarchurch.org",
#     "https://church1.azurewebsites.net"
# ]
SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainApp',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django_summernote',
    'cloudinary',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'churchProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
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

WSGI_APPLICATION = 'churchProject.wsgi.application'


# Database
# its created in azure at account of developer_makki
# Database of Azure
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DBNAME'),
#         'HOST': os.environ.get('DBHOST'),
#         'USER': os.environ.get('DBUSER'),
#         'PASSWORD': os.environ.get('DBPASS'),
#         'OPTIONS': {'sslmode': 'require'},
#     }
# }

# Database of on local machine
DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# # settings on local machine
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
'CLOUD_NAME': 'dvzrr9pok',
'API_KEY': '418716841781465',
'API_SECRET': 'UV-Q_Nbb4kiAi8XFAkKUPRZr3Sc',
}          



# azure settings

# DEFAULT_FILE_STORAGE = 'churchProject.azure_storage.AzureMediaStorage'
# STATICFILES_STORAGE = 'churchProject.azure_storage.AzureStaticStorage'

# AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
# AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
# AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'), 
# ]

# STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/media/'
# MEDIA_ROOT = BASE_DIR / 'mediafiles'
