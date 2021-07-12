import numpy as np
import matplotlib.pyplot as plt
from draw import *

adm = diagram(-5,-5,5,5)
root2 = np.sqrt(2)
iroot2 = 1/root2
n = adm.N
aesthetic_wobble_2 = np.zeros(n)
aesthetic_wobble_3 = np.zeros(n)
aesthetic_wobble_4 = np.zeros(n)
aesthetic_wobble = np.zeros(n)
for i in range(n):
	dx = 1/float(n-1)
	x = float(i)*dx
	aesthetic_wobble_4[i] = x*(1-x)*(x-0.66)*(x-0.33)
	aesthetic_wobble_3[i] = x*(1-x)*(x-.5)
	aesthetic_wobble_2[i] = x*(1-x)*(x-1.5)
	aesthetic_wobble[i] = x*(1.-x)*(x-.55)


line1 = squiggle(1,-3,2,-1,adm,'k',0.7,'-')
line2 = squiggle(2,-1,-1,0,adm,'k',0.7,'-')
line3 = squiggle(-1,0,-3,-2,adm,'k',0.7,'-')
line4 = squiggle(-3,-2,1,-3,adm,'k',0.7,'-')
line1.deform(aesthetic_wobble_3,1)
line2.perturb(2,0.03)
line3.deform(aesthetic_wobble_3,1)
line4.deform(aesthetic_wobble_4,2)

line5 = squiggle(1,0,2,2,adm,'k',0.7,'-')
line6 = squiggle(2,2,-1,3,adm,'k',0.7,'-')
line7 = squiggle(-1,3,-3,1,adm,'k',0.7,'-')
line8 = squiggle(-3,1,1,0,adm,'k',0.7,'-')
line5.deform(aesthetic_wobble_3,1)
line6.perturb(2,0.03)
line7.deform(aesthetic_wobble_3,1)
line8.perturb(2,0.03)

line9 = squiggle(1,-3,1,0,adm,'k',0.7,'--')
line10 = squiggle(2,-1,2,2,adm,'k',0.7,'--')
line11 = squiggle(-1,0,-1,3,adm,'k',0.7,'--')
line12 = squiggle(-3,-2,-3,1,adm,'k',0.7,'--')
line9.deform(aesthetic_wobble,2)
line10.deform(aesthetic_wobble,-1)
line11.deform(aesthetic_wobble_4,-5)
line12.deform(aesthetic_wobble_2,1)

adm.add_text(-4.2,0,r"$\mathcal{M}$",'k',24)
adm.add_text(2,-3,r"$\Sigma_t$",'k',24)
adm.add_text(-4,2,r"$\Sigma_{t+\delta t}$",'k',24)

adm.add_text(-0.92,-1.83,r"$(t,x^i)$",'k',8)
adm.add_text(1.05,1.25,r"$(t+\delta t,x^i)$",'k',8)
adm.add_text(-1.58,1.74,r"$(t+\delta t,x^i-\beta^i \delta t)$",'k',8)

adm.add_text(-1.15,-0.8,r"$m^\mu$",'k',12)
adm.add_text(0.05,-1.19,r"$t^\mu$",'k',12)
adm.add_text(0.08,0.78,r"$\beta^i$",'k',12)

adm.add_arrow(-0.5,-1.5,-0.5,1.5)
adm.add_arrow(-0.5,-1.5,1.3,1.)
adm.add_arrow(-0.5,1.5,1.3,1.)

adm.framed = False
adm.draw_and_save('adm.png')



