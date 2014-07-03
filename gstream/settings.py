"""
Django settings for gstream project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'gstream')

gettext = lambda s: s

# template dirs
TEMPLATE_DIRS = (os.path.join(BASE_DIR,"gstream","templates"),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (

    ################################ CMS ###########################
    'djangocms_link',
    'djangocms_column',
    'djangocms_oembed',
    'djangocms_table',
    'djangocms_text_ckeditor',  # note this needs to be above the 'cms' entry
    'cms',  # django CMS itself
    'mptt',  # utilities for implementing a modified pre-order traversal tree
    'menus',  # helper for model independent hierarchical website navigation
    'south',  # intelligent schema and data migrations
    'sekizai',  # for javascript and css management
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list before 'django.contrib.admin'.
   
    ################################ DJANGO #########################
    'django.contrib.messages',  # to enable messages framework (see :ref:`Enable messages <enable-messages>`)
    'django.contrib.admin', 
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ################################ OTHER HELPERS ###################
    'crispy_forms',
    'easy_thumbnails',
  
    ################################ GSTREAM #########################
    
    'gstream.apps.accounts',
    
    #Admin content apps
    'gstream.apps.carousels',

    #User content apps
    'gstream.apps.content',
    'gstream.apps.blogs',
    'gstream.apps.locations',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
)

CMS_TOOLBARS = [
    # CMS Toolbars
    'cms.cms_toolbar.PlaceholderToolbar',
    'cms.cms_toolbar.BasicToolbar',
    'cms.cms_toolbar.PageToolbar',
]


ROOT_URLCONF = 'gstream.urls'

WSGI_APPLICATION = 'gstream.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gstream',      
        'USER': 'gstream',        
        'PASSWORD': 'gstream',                  
        'HOST': '127.0.0.1',
        'PORT': 5432, 
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
]


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = '/opt/data/web/static'
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
    )

STATICFILES_DIRS = (
     os.path.join(PROJECT_DIR, "static_source/"),
    )

# Media 
MEDIA_ROOT = '/opt/data/web/media'
MEDIA_URL = "/media/"

#django sites (required by django cms)
SITE_ID = 1

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
)

CMS_TEMPLATES = (
    ('cms/template_basic.html', 'Basic Template'),
)


CRISPY_TEMPLATE_PACK = 'bootstrap3'


SOUTH_MIGRATION_MODULES = {
        'easy_thumbnails': 'easy_thumbnails.south_migrations',
    }


if not os.path.isfile(os.path.join(PROJECT_DIR, 'settings_local.py')):
    print "settings_local.py not present - skipping"
else:
    try:
        from settings_local import *
        print "loading settings_local.py"
    except ImportError:
        print "import error in the settings_local.py file."
        raise



