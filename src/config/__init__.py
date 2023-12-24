from os import path as oPath        # Импорт модуля операционной системы
from sys import path as spath       # Импорт системного модуля 

current_directory = oPath.dirname(oPath.abspath(__file__)) # Получение текущей деректории 

spath.append(current_directory)     # Добавление текущей дериктории к дериктории модуля

from telegramExample import *       # Импорт методов