import matplotlib.pyplot as plt

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
font = {'family' : 'normal','size'   : 20}
rc('font', **font)

def func(x):
  contact = 0.5
  dia = 1.0
  y = 0
  if( x/dia <= 1): #1+contact/2):
    y = 1 - x/dia
  elif( x/dia > 1 and x/dia < 1+contact/2):
    y = 2*(1 - x/dia)
  elif( x/dia >= (1+contact/2) and x/dia < (1 + contact)):
    y = 2*(x/dia - 1.5)
  else:
    y = 0
  return y

def func2(x):
  contact = 0.5
  dia = 1.0
  y = abs(x/dia/contact*4 - 2*(1+contact)/(dia*contact)) - 1
  return y

x = [ i/500 for i in range(1,1000) ]
fx = [ func(i/500) for i in range(1,1000) ]

# Origin line
plt.axhline(0, color='k')

plt.plot(x,fx, color='b', linewidth=5)
# y axis
plt.ylim(-1, 1.5)
plt.yticks([-0.5, 0, 1], ['F_{adh}', '0', 'F_{Rep}'])
# x axis
plt.xticks([ 1, 1.25, 1.5 ], ['\sigma','\sigma + \epsilon','\sigma+2\epsilon'])
plt.xlabel('Separation Distance')

plt.title('Cell Interaction Potential')
plt.tight_layout()
plt.grid()
plt.savefig('interaction.png')
plt.show()
