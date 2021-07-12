import numpy as np
import matplotlib.pyplot as plt
from draw import *

pic = diagram(-0.5,-6.5,6.5,0.5)

line1 = squiggle(0.,0.,2.917,0.,pic,'k',0.7,'-')
line2 = squiggle(2.917,-4.136,2.917,0.,pic,'k',0.7,'-')
line3 = squiggle(0.,0.,0.,-3.664,pic,'k',0.7,'-')
line4 = squiggle(2.,-3.664,0.,-3.664,pic,'k',0.7,'-')
line5 = squiggle(2.917+3.25,0.,2.917,0.,pic,'k',0.7,'-')
line6 = squiggle(2.917+3.25,0.,2.917+3.25,-3.1,pic,'k',0.7,'-')
line7 = squiggle(3.8,-3.1,2.917+3.25,-3.1,pic,'k',0.7,'-')
line8 = squiggle(2.917+3.25,-3.1-3.09,2.917+3.25,-3.1,pic,'k',0.7,'-')
line9 = squiggle(2.917+3.25,-3.1-3.09,0.,-3.1-3.09,pic,'k',0.7,'-')
line10 = squiggle(0.,0.,0.,-3.1-3.09,pic,'k',0.7,'-')
line11 = squiggle(1.23,-6.19,1.23,-5.18,pic,'k',0.7,'-')
line12 = squiggle(2.,-5.18,1.23,-5.18,pic,'k',0.7,'-')
line13 = squiggle(2.,-6.19,2.,-6.19+2.51,pic,'k',0.7,'-')
line14 = squiggle(3.8,-3.1,3.8,-5.118,pic,'k',0.7,'-')
line15 = squiggle(4.62,-5.118,3.8,-5.118,pic,'k',0.7,'-')
line16 = squiggle(5.319,-5.118,4.62,-5.118,pic,'k',0.7,':')
line17 = squiggle(4.62,-6.19,4.62,-5.118,pic,'k',0.7,'-')
line18 = squiggle(5.319,-6.19,5.319,-5.118,pic,'k',0.7,':')
line19 = squiggle(4.62,-5.118,2.917,-5.118,pic,'k',0.7,'--')
pic.framed = False
pic.draw_and_save('floorplan_upstairs.png')