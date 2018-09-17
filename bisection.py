from math import *
import scipy as sp
from psm_plot import *
from random import *

#Note this is specified def f_string():
def f_string():
    fn_string = "pow(x,3)-x-exp(x)-2"
    return fn_string

def f(x):
    #tmp = 1.2*pow(x,3)+2*pow(x,2)-20*x-10
    #tmp = x - 2.0*exp(-x)
    string = f_string()
    tmp = eval(string)
    return tmp

def main():
    a = 2.0
    b = 4.0
    dx = .01
    N = (int)((b-a)/dx)
    x = []
    fx = []
    for i in range(0,N+1):
        x.append(i*dx+a)
        fx.append(f(x[i]))
    print(x)
    #print(fx)

    function_name = f_string()
    title_base = "Plot of " + function_name
    title = title_base
    filename = "bisection_"+function_name+".png"
    xlabel = "x"
    ylabel = "f(x)"
    root_data_label = "root approximations"
    y_func_label = function_name


    LinePlot111(x,fx,xlabel,ylabel,title,filename)

#FunctionRootPlot111(x,xlabel,f,ylabel,root_approx,root_data_label,title,filename)



if __name__ == '__main__':
    main()











