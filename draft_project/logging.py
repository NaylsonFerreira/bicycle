import logging
import os

from django.conf import settings


class IgnoreSelect(logging.Filter):
    def filter(self, record):
        return 'SELECT' not in record.getMessage()


def log_config():
    LOG_LEVEL = ['debug', 'info', 'warning', 'error', 'critical']
    logs_dir = os.path.join(settings.BASE_DIR, 'logs')

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{asctime} {levelname} {message}',
                'style': '{',
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
            'ignore_select': {
                '()': 'draft_project.logging.IgnoreSelect',
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': False,
            },
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['console', 'debug'],
                'filters': ['ignore_select'],
            },
        }
    }
    for log_file in LOG_LEVEL:
        log_file_path = os.path.join(logs_dir, f"{log_file}.log")
        if not os.path.exists(log_file_path):
            open(log_file_path, 'a').close()

        LOGGING_CONFIG['handlers'].update({f"{log_file}": {
            'level': log_file.upper(),
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': log_file_path,
            'maxBytes': 1024 * 1024 * 10,
            'formatter': 'simple'
        }})

    LOGGING_CONFIG['loggers']['django']['handlers'] += [
        f"{log_file}" for log_file in LOG_LEVEL
    ]

    return LOGGING_CONFIG
