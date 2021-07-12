import numpy as np
import matplotlib.pyplot as plt
from draw import *

feyn = diagram(-5,-5,5,5) #picture object, will contain all lines, arrows, text ...

n = feyn.N # detail of each line (points per line)

line1 = squiggle(0,0,2,2,feyn,'k',0.7,'-')
line1.make_arrow(0.5)


feyn.framed = False


feyn.draw_and_save('feynman_diagram.pdf')