from math import *
import time
from psm_plot import *
from random import *

def f(x):
    return 3.01*x**3 - 2.54*x**2 + 0.25

#Below is a function definition
def main():

    a = -1.0
    b = 0.0
    dx = .01
    N = (int)((b-a)/dx)
    for i in range(0,N):
        x = i*dx+a
        print("%15.14e %15.14e" % (x, f(x)))







if __name__ == '__main__':
    main()











