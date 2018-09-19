from math import *
import scipy as sp
from psm_plot import *
from random import *

#Note this is specified def f_string():
def f_string():
    #fn_string = "1.2*pow(x,3)+2*pow(x,2)-20*x-10"
    fn_string = "pow(x,3)-x-exp(x)-2"
    return fn_string

def f(x):
    #tmp = 1.2*pow(x,3)+2*pow(x,2)-20*x-10
    #tmp = x - 2.0*exp(-x)
    string = f_string()
    tmp = eval(string)
    return tmp

def main():
    a = 2.0     #left side of bracketing values for root
    b = 3.0     #right side of bracketing values for root
    x_start = 0.0
    x_end = 10.0
    root_approx = [a,b]

    FunctionRootPlot111(x,xlabel,f,ylabel,root_approx,root_data_label,title,filename)
    #LinePlot111(x,fx,xlabel,ylabel,title,filename)


if __name__ == '__main__':
