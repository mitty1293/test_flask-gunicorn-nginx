from flask import Flask
import os

config_type = {
    "development": "app.config.Development",
    "production": "app.config.Production"
}

app = Flask(__name__, instance_path='/run/secrets', instance_relative_config=True)
app.config.from_object(config_type.get(os.getenv("FLASK_CONFIG_TYPE", "production")))
app.config.from_pyfile("secrets_test")

from app.views import views