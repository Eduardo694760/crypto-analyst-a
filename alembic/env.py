import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# adiciona a raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# importa o Base central e todos os modelos
from src.models.base import Base
from src.models.crypto_models import Crypto
from src.models.favorites_model import Favorite
from src.models.user_models import User
from src.models.history_model import History
from src.models.logs_model import Log

target_metadata = Base.metadata


target_metadata = Base.metadata



