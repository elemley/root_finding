from math import *
import scipy as sp
from psm_plot import *
from random import *



def f(x):
    return x**2

def f_prime(x):
    return 2*x

def main():
    a = 2.0     #left side of bracketing values for root
    b = 3.0     #right side of bracketing values for root
    x_start = 0.0
    x_end = 10.0
    root_approx = [a,b]

    #FunctionRootPlot111(x,xlabel,f,ylabel,root_approx,root_data_label,title,filename)
    #LinePlot111(x,fx,xlabel,ylabel,title,filename)


if __name__ == '__main__':
    main()


