"""
Django settings for pet project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',
    'search',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',

    'modeltranslation', # has to be before django.contrib.admin, will raise error otherwise

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'userauth',
    'django_countries',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'widget_tweaks',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin_oauth2',

    'wagtail.contrib.modeladmin',
    'wagtail.contrib.settings',
    'wagtailtrans',
    'cms',
    'wagtailcodeblock',
    'django_extensions',
    'django_comments_xtd',
    'django_comments',
    'wagtailstreamforms',
    'captcha',
    'coverage',
    'dbbackup',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtailtrans.middleware.TranslationMiddleware', # depends on SiteMiddleware and replaces LocaleMiddleware
    # 'django.middleware.locale.LocaleMiddleware', # after SessionMiddleware and before CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'pet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
            os.path.join(BASE_DIR, 'userauth/templates/userauth/'),
            os.path.join(BASE_DIR, 'cms/templates/cms/'),
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

WSGI_APPLICATION = 'pet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', "English"),
    ('fr', "Fran??ais"),
    ('nl', "Nederlands"),
]

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

WAGTAILTRANS_HIDE_TRANSLATION_TREES = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
    os.path.join(BASE_DIR, 'userauth/static/userauth/'),
    os.path.join(BASE_DIR, 'cms/static/cms/'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Wagtail settings

WAGTAIL_SITE_NAME = "pet"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://PythonEatsTail.com'

# custom user model

AUTH_USER_MODEL = 'userauth.CustomUser'

WAGTAIL_USER_CREATION_FORM = 'userauth.forms.WagtailUserCreationForm'
WAGTAIL_USER_EDIT_FORM = 'userauth.forms.WagtailUserEditForm'
WAGTAIL_USER_CUSTOM_FIELDS = ['display_name', 'date_of_birth', 'address1', 'address2', 'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'photo',]


# allauth settings

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_FORM_CLASS = 'userauth.forms.SignupForm'
SOCIALACCOUNT_AUTO_SIGNUP = False # to make the user fill in all required fields

# specified to enforce i18n-patterns when calling LOGIN_URL or LOGIN_REDIRECT_URL
# reverse_lazy because parameters have not yet been defined
LOGIN_URL = reverse_lazy('account_login')
LOGIN_REDIRECT_URL = reverse_lazy('account_profile')

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    },
    'linkedin': {
        'SCOPE': [
            'r_basicprofile',
            'r_emailaddress'
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ],
    },
}

# Wagtail setting for embedded video https://docs.wagtail.io/en/v2.9/topics/writing_templates.html#responsive-embeds
WAGTAILEMBEDS_RESPONSIVE_HTML = True

# wagtailcodeblock theme and languages
WAGTAIL_CODE_BLOCK_THEME = None
WAGTAIL_CODE_BLOCK_LANGUAGES = (
    ('bash', 'Bash/Shell'),
    ('css', 'CSS'),
    ('html', 'HTML'),
    ('javascript', 'Javascript'),
    ('json', 'JSON'),
    ('python', 'Python'),
    ('sql', 'SQL'),
    ('yaml', 'YAML'),
)

# settings for Django Comments Xtd - see https://django-comments-xtd.readthedocs.io/en/latest/tutorial.html
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_SALT = (b"Timendi causa est nescire. "
                     b"Aequam memento rebus in arduis servare mentem.")
COMMENTS_XTD_FROM_EMAIL = "noreply@pythoneatstail.com"
COMMENTS_XTD_CONTACT_EMAIL = "mail@prijme.com"
COMMENTS_XTD_MODEL = 'cms.models.CustomComment'
COMMENTS_XTD_MAX_THREAD_LEVEL = 1  # default is 0
COMMENTS_XTD_LIST_ORDER = ('-thread_id', 'order')  # default is ('thread_id', 'order')
COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'cms.articlepage': {
        'allow_flagging': False,
        'allow_feedback': True,
        'show_feedback': True,
    }
}

# Wagtailstreamforms settings
WAGTAILSTREAMFORMS_FORM_TEMPLATES = (
    ('cms/custom_form.html', _("Custom Form Template")),
)
WAGTAILSTREAMFORMS_ADVANCED_SETTINGS_MODEL = 'cms.AdvancedFormSetting'

# dbbackup settings
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, '../backups')}

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'