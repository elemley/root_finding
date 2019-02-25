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

    x = np.linspace(x_start, x_end, 100)

    function_name = f_string()
    title_base = "Plot of " + function_name
    title = title_base
    filename = "bisection_2.png"
    xlabel = "x"
    ylabel = "f(x)"
    root_data_label = "root approximations"
    y_func_label = function_name

    FunctionRootPlot111(x,xlabel,f,ylabel,root_approx,root_data_label,title,filename)
    #LinePlot111(x,fx,xlabel,ylabel,title,filename)


if __name__ == '__main__':
    main()

