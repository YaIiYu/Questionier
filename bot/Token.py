from os import environ
from typing import Final


class TgToken():
    TOKEN: Final = environ.get('TOKEN', 'define me')