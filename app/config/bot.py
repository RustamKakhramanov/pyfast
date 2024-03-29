from enum import Enum
from app.apps.core.bot.middlewares.main import MainMiddleware
from app.apps.core.bot.middlewares.language import LanguageMiddleware
from app.apps.core.bot.middlewares.has_tariff import HasTariffMiddleware
from app.config import env


class RunningMode(str, Enum):
    LONG_POLLING = "LONG_POLLING"
    WEBHOOK = "WEBHOOK"


TG_TOKEN = env("TG_TOKEN", cast=str)

RUNNING_MODE = env("RUNNING_MODE", cast=RunningMode, default=RunningMode.LONG_POLLING)
WEBHOOK_URL = env("WEBHOOK_URL", cast=str, default="")


MIDDLEWARE = (
    HasTariffMiddleware,
    MainMiddleware,
    LanguageMiddleware
)
