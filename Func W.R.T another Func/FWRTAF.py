import numpy as np
from matplotlib import pyplot as plt

#plt.xkcd()
def fun_1(x):
    f=5*(np.sin(x))
    return f
def fun_2(x):
    f=2*(np.cos(x))
    return f

#-------------------------------------------------------------------------------------------------------------------------------------
# To plot the given function.

dx = 0.05
low_x = float(input("Enter lower limit of x:"))
up_x = float(input("Enter upper limit of x:"))
def draw_1(matA):
    plt.plot(matA[0],matA[1])

func_value1 = []
func_value2 = []
for j in np.arange(low_x,up_x,dx):
    func_value1.append(fun_1(j))
    func_value2.append(fun_2(j))
draw_1([func_value1,func_value2])
plt.show()

   

