from enum import Enum

from .homescreen import HomeScreen

class SCREEN_TYPE(Enum):
    HOME = 1


SCREENS = {
    SCREEN_TYPE.HOME: HomeScreen,
}
