import numpy as np
import matplotlib.pyplot as plt
from draw import *

penrose = diagram(-2,-2,2,2)
N = penrose.N
wobble = np.zeros(N)
wobble2 = np.zeros(N)
root2 = np.sqrt(2)
iroot2 = 1/root2
for i in range(N):
	x = float(i)/float(N-1)
	wobble[i] = x*(1-x)*(1.5-x)
	wobble2[i] = x*(1-x)*(-0.5-x)


line3 = squiggle(root2,0,iroot2,iroot2,penrose,'k',0.7,'-')
line4 = squiggle(root2,0,iroot2,-iroot2,penrose,'k',0.7,'-')

line5 = squiggle(0,0,iroot2,iroot2,penrose,'k',0.7,'-')
line6 = squiggle(iroot2,-iroot2,-iroot2,iroot2,penrose,'k',0.7,'-')

line7 = squiggle(-iroot2,iroot2,iroot2,iroot2,penrose,'k',0.7,'-')
line7.perturb(41,0.01)


line12 = squiggle(-iroot2,iroot2,root2,0,penrose,'k',0.7,'--')
line12.deform(wobble2,1.7)


penrose.framed = False
penrose.draw_and_save('schwarzschild2.png')