import os

from dotenv import load_dotenv

load_dotenv()


def get_env_variable(variable_name, default):
    if os.getenv(variable_name):
        return os.getenv(variable_name)
    else:
        return default
