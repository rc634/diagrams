import numpy as np
import matplotlib.pyplot as plt
from draw import *

pic = diagram(-0.5,-6.5,6.5,0.5)

line1 = squiggle(0.,0.,6.286,0.,pic,'k',0.7,'-')
line2 = squiggle(6.286,0.,6.286,-4.121,pic,'k',0.7,'-')
line3 = squiggle(6.286,-4.121,6.286-3.357,-4.121,pic,'k',0.7,'-')
line4 = squiggle(6.286-3.357,-4.121,6.286-3.357,-4.121+1.864,pic,'k',0.7,'-')
line5 = squiggle(6.286-3.357,-4.121+1.864,0,-4.121+1.864,pic,'k',0.7,'-')
line6 = squiggle(0,0,0,-6.148,pic,'k',0.7,'-')
line7 = squiggle(0,-6.148,6.286,-6.148,pic,'k',0.7,'-')
line8 = squiggle(6.286,-6.148,6.286,-4.121,pic,'k',0.7,'-')
line9 = squiggle(1.942,-6.148,1.942,-6.148+1.820,pic,'k',0.7,'-')
line10 = squiggle(1.942,-6.148+1.820,6.286-3.357,-6.148+1.820,pic,'k',0.7,'-')
line11 = squiggle(6.286-3.357,-6.148+1.820,6.286-3.357,-4.121,pic,'k',0.7,'-')
line12 = squiggle(1.942,-6.148+0.910,3.942,-6.148+0.910,pic,'k',0.7,'-')
line12 = squiggle(3.942,-6.148+0.910,5.286,-6.148+0.910,pic,'k',0.7,'--')
line13 = squiggle(3.942,-6.148+0.910,3.942,-6.148,pic,'k',0.7,'-')
pic.framed = False
pic.draw_and_save('floorplan_ground.png')