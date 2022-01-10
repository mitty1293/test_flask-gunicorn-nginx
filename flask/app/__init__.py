from flask import Flask
from logging.config import dictConfig
import os

# logのフォーマット設定。logレベルもここで指定する。
# DEBUG->INFO->WARN->ERROR->CRITICAL
dictConfig({
    'version': 1,
    'formatters': {'default':{
        'format': '[%(asctime)s] level: %(levelname)s module: %(module)s message: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# フォーマット設定せずに標準で良いなら以下。
# from flask import logging
# logging.basicConfig(level=logging.INFO)
# app.logger.info('called hello world')

config_type = {
    "development": "app.config.Development",
    "production": "app.config.Production"
}

app = Flask(__name__, instance_path='/run/secrets', instance_relative_config=True)
app.config.from_object(config_type.get(os.getenv("FLASK_CONFIG_TYPE", "production")))
app.config.from_pyfile("secrets_test")

from app.views import views