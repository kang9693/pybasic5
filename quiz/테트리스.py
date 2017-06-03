import os
import time
import pygame                   # pygame 모듈을 import
from pygame.locals import *     # pygame.locals 하위 모듈을 import
import tkinter 
import random
try:
    import pygame as pg
except ImportError:
    audio = None
else:
    audio = True
import sys
from matrix_rotation import rotate_array as ra


for key in ('<Down>', '<Left>', '<Right>', 'a', 'A', 's', 'S', 'd', 'D'):
	self.parent.bind(key, self.shift)
for key in ('q', 'Q', 'e', 'E', '<Up>', 'w', 'W'):
    self.parent.bind(key, self.rotate)
for key in ('<space>', '<End>', '<Control_R>', 'z', 'Z', '0', 'c', 'C'):