
from cement.utils.version import get_version as cement_get_version

VERSION: tuple = (0, 0, 7, 'beta', 0)


def get_version(version: tuple = VERSION) -> str:
    ver_string: str = cement_get_version(version)
    return ver_string
