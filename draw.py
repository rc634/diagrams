import numpy as np
import matplotlib.pyplot as plt

class squiggle:
    def __init__(self,x0,y0,x1,y1,diagram,colour,thicc,line):
    	self.N = diagram.N
    	self.x = np.zeros(self.N)
    	self.y = np.zeros(self.N)
    	self.start = [x0,y0]
    	self.end = [x1,y1]
    	self.L = np.sqrt((x1-x0)**2 + (y1-y0)**2)
    	self.dL = self.L/(float(self.N-1))
    	self.c = (x1-x0)/self.L
    	self.s = (y1-y0)/self.L
    	self.colour = colour
    	self.thicc = thicc
    	self.line = line
    	self.make()
    	self.is_arrow = False
    	self.arrow_head_place = 0

    	diagram.add_line(self)

    def make(self):
    	for i in range(self.N):
    		self.x[i] = self.start[0] + (self.end[0]-self.start[0]) * float(i)/float(self.N-1)
    		self.y[i] = self.start[1] + (self.end[1]-self.start[1]) * float(i)/float(self.N-1)

    def plot(self,ax):
    	if (self.is_arrow):
    		ax.arrow(self.x[:self.arrow_head_place],self.y[:self.arrow_head_place],color=self.colour, linewidth = self.thicc, linestyle = self.line, head_width=0.1)
    		ax.plot(self.x[self.arrow_head_place:],self.y[self.arrow_head_place:],color=self.colour, linewidth = self.thicc, linestyle = self.line)
    	else:    	
    		ax.plot(self.x,self.y,color=self.colour, linewidth = self.thicc, linestyle = self.line)

    def perturb(self,num,a):
    	t_ = 0
    	for i in range (self.N):
    		self.x[i] += -self.s*a*self.L*np.sin(t_*num*3.1415926/self.L) 
    		self.y[i] += self.c*a*self.L*np.sin(t_*num*3.1415926/self.L)
    		t_ += self.dL

    def deform(self,delta_f,a):
    	for i in range (self.N):
    		self.x[i] += -self.s*a*delta_f[i] 
    		self.y[i] += self.c*a*delta_f[i]

    def make_arrow(self,r):
    	if r>1.:
    		r=1.
    	elif r<0.:
    		r=0.
    	self.arrow_head_place = int(round(r*self.N))
    	self.is_arrow = True


class diagram:
	def __init__(self,x0,y0,x1,y1,dpi=400.):
		plt.rc('text', usetex=True)
		self.N = 1000
		self.framed = True
		self.lines = []
		self.texts = []
		self.arrows = []
		self.ellipses = []
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(1, 1, 1)
		self.ax.set_xlim([x0,x1])
		self.ax.set_ylim([y0,y1])
		self.ax.set_aspect('equal')
		self.dpi = dpi


	def add_line(self,line):
		self.lines.append(line)

	def add_text(self,x_,y_,text_,c_,size_):
		self.texts.append([x_,y_,text_,c_,size_])

	def add_arrow(self,x0,y0,x1,y1,c_='k'):
		self.arrows.append([(x1,y1),(x0,y0),c_])

	def add_ellipse(self,x0,y0,width,height,theta0,c_='k',thickness=0.7,style='-',dash_size='no'):
		self.ellipses.append([x0,y0,width,height,theta0,c_,thickness,style,dash_size])

	def draw_and_save(self,filename):
		
		self.fig.set_dpi(self.dpi)
		for line in self.lines:
			line.plot(self.ax)
		for text in self.texts:
			self.ax.text(text[0],text[1],text[2],color=text[3],fontsize=text[4])
		for arrow in self.arrows:
			self.ax.annotate("",xy=arrow[0], xytext=arrow[1],arrowprops=dict(color=arrow[2],arrowstyle="->"))
		for ellipse in self.ellipses:
			theta0 = ellipse[4]
			ellipse_theta = np.linspace(0.,2.*np.pi,self.N,endpoint=True)
			ellipse_x = ellipse[2]*np.cos(ellipse_theta) 
			ellipse_y = ellipse[3]*np.sin(ellipse_theta)
			if ellipse[8] == 'no':
				plt.plot(np.cos(theta0)*ellipse_x - np.sin(theta0)*ellipse_y + ellipse[0] ,np.sin(theta0)*ellipse_x + np.cos(theta0)*ellipse_y  + ellipse[1], linestyle=ellipse[7], linewidth=ellipse[6], color=ellipse[5])
			else:
				plt.plot(np.cos(theta0)*ellipse_x - np.sin(theta0)*ellipse_y + ellipse[0] ,np.sin(theta0)*ellipse_x + np.cos(theta0)*ellipse_y  + ellipse[1], linestyle=ellipse[7], linewidth=ellipse[6], color=ellipse[5], dashes=ellipse[8])
			

		if self.framed==False:
			plt.axis('off')
		plt.show()
		self.fig.savefig(filename)






