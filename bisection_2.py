from math import *
import scipy as sp
from psm_plot import *
from random import *

#Note this is specified def f_string():
def f_string():
    #fn_string = "1.2*pow(x,3)+2*pow(x,2)-20*x-10"
    #fn_string = "pow(x,3)-x-exp(x)-2"
    fn_string = "x*exp(0.5*x)+1.2*x -5"
    return fn_string

def f(x):
    string = f_string()
    tmp = eval(string)
    return tmp

def main():
    a = 1.0     #left side of bracketing values for root
    b = 2.0     #right side of bracketing values for root
    x_start = 0.0
    x_end = 10.0
    root_approx = [a,b]

    if f(a)*f(b) < 0:

        rel_err_stop = 1e-5     #adjust as needed...
        rel_err = 1.1*rel_err_stop  #set value large enough to start process
        count = 0
        max_iter = 1000
        #Where the bisection technique goes


        print(count)
        print(rel_err)
        print(root_approx)
        print(xns)
    else:
        print("Oops your a and b values don't bracket the root" )

    """
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
    """



if __name__ == '__main__':
    main()




"""
while rel_err > rel_err_stop and count < max_iter:
    count += 1
    xns = (a + b) / 2.0
    root_approx.append(xns)
    if f(a) * f(xns) < 0:
        b = xns
    else:
        a = xns
    if count > 1:
        rel_err = abs((xns - xns_old) / xns)

        # rel_err-=0.01*1e-5

    xns_old = xns

"""