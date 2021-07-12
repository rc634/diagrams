import numpy as np
import matplotlib.pyplot as plt
from draw import *

floorplan = diagram(-1,8,-1,8)

line1 = squiggle(0,0,0,5,floorplan,'k',0.7,'-')
line1 = squiggle(1,1,0,5,floorplan,'k',0.7,'-')



floorplan.framed = False
floorplan.draw_and_save('schwarzschild.png')