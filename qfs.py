import numpy as np
import matplotlib.pyplot as plt
from draw import *

g = [100./256.,210./256.,0.,1.]
r = [220./256.,0.,0.,1.]
b = [0.,60./256.,1.,1.]

adm = diagram(-6.3,-6.3,5.3,6.3,400)
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


line1 = squiggle(2,-6,5,-3,adm,'k',0.7,'-')
line2 = squiggle(5,-3,-2,-1,adm,'k',0.7,'-')
line3 = squiggle(-2,-1,-6,-4,adm,'k',0.7,'-')
line4 = squiggle(-6,-4,2,-6,adm,'k',0.7,'-')
line1.deform(aesthetic_wobble_3,1)
line2.perturb(2,0.03)
line3.deform(aesthetic_wobble_3,1)
line4.deform(aesthetic_wobble_3,-3)



line9 = squiggle(-2.58,3.74,-1.792,-3.367,adm,b,0.7,'-')
line10 = squiggle(-1.59,3.64,-1.792,-3.367,adm,r,0.7,'-')

line5 = squiggle(2,1,5,4,adm,'k',0.7,'-')
line6 = squiggle(5,4,-2,6,adm,'k',0.7,'-')
line7 = squiggle(-2,6,-6,3,adm,'k',0.7,'-')
line8 = squiggle(-6,3,2,1,adm,'k',0.7,'-')
line5.deform(aesthetic_wobble_3,1)
line6.perturb(2,0.03)
line7.deform(aesthetic_wobble_3,1)
line8.perturb(2,0.03)
#line11 = squiggle(-6.,-5.,-6.,5.,adm,'k',0.7,'-')
#line12 = squiggle(-6,-4,-6,2,adm,'k',0.7,'--')
#line9.deform(aesthetic_wobble,2)

adm.add_text(-5,-1.3,r"$\mathcal{M}$",'k',12)
adm.add_text(4,-2.6,r"$\Sigma_t$",'k',12)
adm.add_text(4,4.5,r"$\Sigma_{t+\delta t}$",'k',12)
adm.add_text(-0.77,3.4,r"$V_1$",'r',8)
adm.add_text(-0.24,3.4,r"$V_2$",'b',8)
adm.add_text(-0.5,-3.6,r"$V_1$",'k',8)
adm.add_text(-2.24,3.75,r"$\delta V$",'k',8)
adm.add_text(-4.3,-3.7,r"$x^\mu = \{t,x^i\}$",'k',8)
adm.add_text(-2.8,4.9,r"$x^\mu = \{t+\delta t,x^i\}$",'k',8)
adm.add_text(1.56,0.,r"$\delta t \cdot \alpha n^\mu$",b,8)
adm.add_text(-0.1,-0.69,r"$\delta t \cdot t^\mu$",r,8)
adm.add_text(-3.3,-0.6,r"$N^\mu$",r,8)
adm.add_text(-4.0,1.0,r"$\tilde{N}^\mu$",b,8)
adm.add_text(-0.77,0.4,r"$M$",r,8)
adm.add_text(-0.24,0.4,r"$\tilde{M}$",b,8)
adm.add_text(-2.03,1.,r"$H$",r,8)
adm.add_text(-2.6,0.2,r"$\tilde{H}$",b,8)
adm.add_text(2.15,2.97,r"$\delta t \cdot \beta^i$",g,8)
adm.add_text(-6.46,5.1,r"Time ",'k',8)

adm.add_arrow(2.,3.1,0.92,3.3,g)
adm.add_arrow(0.8,-3.66,2.,3.16,b)
adm.add_arrow(0.8,-3.66,1.,3.3,r)
adm.add_arrow(-6.,-5.5,-6.,5.)
adm.add_arrow(-1.71,-0.61,-2.79,-0.5,r)
adm.add_arrow(-2.32,1.49,-3.5,1.24,b)

adm.framed = False

adm.add_ellipse(-0.5,-3.5,1.3,0.6,-np.pi/24.,r,0.7)
adm.add_ellipse(-0.5,-3.5,1.3,0.6,-np.pi/24.,b,0.7,'dashed',[12,12])
adm.add_ellipse(-0.3,3.5,1.3,0.6,-np.pi/24.,r,0.7)
adm.add_ellipse(-0.3,3.5,2.3,1.0,-np.pi/24.,b,0.7)

adm.draw_and_save('qfs_coloured.png')



