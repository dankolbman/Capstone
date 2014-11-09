import matplotlib.pyplot as plt

def func(x):
  contact = 0.5
  dia = 1.0
  y = 0
  if( x/dia < 1+contact/2):
    y = 1 - x/dia
  elif( x/dia >= (1+contact/2) and x/dia < (1 + contact)):
    y = x/dia - 1.5
  else:
    y = 0
  
  return y

def func2(x):
  contact = 0.5
  dia = 1.0
  y = abs(x/dia/contact*4 - 2*(1+contact)/(dia*contact)) - 1
  #y = abs(x/dia - (1+contact/2)) - 1
  
  return y


x = [ i/500 for i in range(1,1000) ]
fx = [ func(i/500) for i in range(1,1000) ]

y = [ i/500 for i in range(1,1000) ]
fy = [ func2(i/500) for i in range(1,1000) ]

plt.plot(x, fx, y, fy)
plt.grid()
plt.show()
