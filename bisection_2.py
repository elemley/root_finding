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
    b = 3.0
    x_start = 0.0
    x_end = 4.0
    root_approx = [a,b]
    bisect = (a+b)/2
    root_approx.append(bisect)




    """
    dx = .01
    N = (int)((b-a)/dx)
    x = []
    fx = []
    for i in range(0,N):
        x.append(i*dx+a)
        fx.append(f(x[i]))
    #print(x,fx)
    """

    x = np.linspace(x_start, x_end, 100)


    function_name = f_string()
    title_base = "Plot of " + function_name
    title = title_base
    filename = "bisection_"+function_name+".png"
    xlabel = "x"
    ylabel = "f(x)"
    root_data_label = "root approximations"
    y_func_label = function_name

    FunctionRootPlot111(x,xlabel,f,ylabel,root_approx,root_data_label,title,filename)
    #LinePlot111(x,fx,xlabel,ylabel,title,filename)





if __name__ == '__main__':
    main()


"""max_iterations = 1000
count = 0
xns = [(a+b)/2.0]
err_stop = 0.0001
relerr=[1.1*err_stop]

if f(a)*f(b) < 0:
    print "Specified Interval OK. Proceeding with bisection method"

    while relerr[count] > err_stop and count < max_iterations:
        count += 1
        if f(a)*f(xns[count -1]) < 0:
            b=xns[count-1]
            root_approx.append(b)
        else:
            a = xns[count-1]
            root_approx.append(a)
        xns.append((a+b)/2)
        tmp = abs((xns[count]-xns[count -1])/xns[count])
        relerr.append(tmp)
        print a, b, xns[count], relerr[count]

    #print xns, relerr
else:
    print "Sorry please edit your interval values a, b"
relerr.pop(0)
"""








