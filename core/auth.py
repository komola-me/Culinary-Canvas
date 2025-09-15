from datetime import timedelta
from decouple import config

ALGORITHM = 'HS256'

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
}

CELERY_BROKER_URL=config('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND=config('CELERY_RESULT_BACKEND')
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
# EMAIL_FROM=config('EMAIL_FROM')
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True