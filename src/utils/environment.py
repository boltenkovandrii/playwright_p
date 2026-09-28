import os

from dotenv import load_dotenv

load_dotenv()


def get_env_variable(variable_name: str, default: str) -> str:
    value = os.getenv(variable_name)
    if value:
        return value
    return default
