import daiquiri.core.env as env

from . import ADDITIONAL_APPS, DJANGO_APPS

SITE_IDENTIFIER = 'example.com'
SITE_TITLE = 'example.com'
SITE_DESCRIPTION = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.'
SITE_LICENSE = 'CC0'
SITE_CREATOR = 'Anna Admin'
SITE_CONTACT = {
    'name': 'Anna Admin',
    'address': 'Example Road 1',
    'email': 'admin@example.com',
    'telephone': '+01 234 56789',
}
SITE_PUBLISHER = 'Leibniz Institute for Astrophysics Potsdam (AIP)'
SITE_CREATED = '2025-01-01'
SITE_UPDATED = '2025-03-01'

INSTALLED_APPS = (
    DJANGO_APPS
    + [
        'theme',
        'daiquiri.auth',
        'daiquiri.conesearch',
        'daiquiri.contact',
        'daiquiri.core',
        'daiquiri.datalink',
        'daiquiri.files',
        'daiquiri.jobs',
        'daiquiri.metadata',
        'daiquiri.oai',
        'daiquiri.query',
        'daiquiri.registry',
        'daiquiri.serve',
        'daiquiri.stats',
        'daiquiri.tap',
        'daiquiri.uws',
    ]
    + ADDITIONAL_APPS
)

PASSWORD_HASHERS = [
    'daiquiri.core.hashers.CrypdSHA512PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_PASSWORD_MIN_LENGTH = 8

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_VERIFICATION = env.get('ACCOUNT_EMAIL_VERIFICATION', 'mandatory')

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

AUTH_SIGNUP = True
AUTH_TERMS_OF_USE = True
