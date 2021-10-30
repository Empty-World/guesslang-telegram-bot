import os
from dotenv import load_dotenv
load_dotenv()


def get_env(name: str, terminal_action: bool = True):
    """
    Get environment variables or you can input your variables into the terminal.
    """
    if name in os.environ:
        return os.environ[name]

    try:
        if terminal_action is True:
            values = input(f'Enter your {name}: ')

            return values
        else:
            return name
    except Exception as e:
        print(e)
