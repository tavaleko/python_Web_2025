# __int__.py
from .module import greet
__version__ = '1.0.0'
__doc__ = 'Это пакет который содержит...'
__author__ = 'John'
__all__ = ['greet']# список функций к кторой нельзя обратиться

from .utils import add
