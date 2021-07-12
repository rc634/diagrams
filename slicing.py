import numpy as np
import matplotlib.pyplot as plt
from draw import *

pic = diagram(-5,-5,5,5)
'''
root2 = np.sqrt(2)
iroot2 = 1/root2
n = pic.N
lorentzian_thin = np.zeros(n)
lorentzian_fat = np.zeros(n)
lorentzian_vfat = np.zeros(n)
lorentzian_med = np.zeros(n)
for i in range(n):
	dx = 1/float(n-1)
	x = float(i)*dx
	lorentzian_thin[i] = 0.01/(0.01+ (x-0.5)**2)
	lorentzian_fat[i] = 0.1/(0.1+ (x-0.5)**2)
	lorentzian_vfat[i] = 0.3/(0.3+ (x-0.5)**2)
	lorentzian_med[i] = 0.03/(0.03+ (x-0.5)**2)


pic.add_arrow(-4.,-4.5,-4.,4.)
pic.add_arrow(-4.5,-4.,4.,-4.)
pic.add_text(-4.8,0.,r"$t$",'k',16)
pic.add_text(0.,-5.,r"$x^i$",'k',16)
'''
line1 = squiggle(0.,0.,0.,4.,pic,'k',0.7,'-')
'''
line1.perturb(20,0.01)
line2 = squiggle(-0.000001,0.,0.000001,0.,pic,'k',5.,'-')
line3 = squiggle(-4.,-3.,4.,-3.,pic,'k',0.7,'-')
line4 = squiggle(-4.,0.,4.,0.,pic,'k',0.7,'-')
line4.deform(lorentzian_fat,-1.4)
line5 = squiggle(-4.,3.,4.,3.,pic,'k',0.7,'-')
line5.deform(lorentzian_thin,-3.7)
line6 = squiggle(-4.,-1.5,4.,-1.5,pic,'k',0.7,'-')
line6.deform(lorentzian_vfat,-0.5)
line7 = squiggle(-4.,1.5,4.,1.5,pic,'k',0.7,'-')
line7.deform(lorentzian_med,-2.5)

pic.add_text(4.2,-3.5,r"$\Sigma_0$",'k',16)
pic.add_text(4.2,-2.,r"$\Sigma_1$",'k',16)
pic.add_text(4.2,-0.5,r"$\Sigma_2$",'k',16)
pic.add_text(4.2,1.0,r"$\Sigma_3$",'k',16)
pic.add_text(4.2,2.5,r"$\Sigma_4$",'k',16)
pic.add_text(0.5,4.,r"$Singularity$",'k',16)

'''
pic.framed = False
pic.draw_and_save('foliation.png')