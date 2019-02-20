from math import *
from psm_plot import *

#Note this is specified def f_string():
##You can choose not to use this... Just delete it in that case
def f_string():
    fn_string = "x-2*exp(-x)"
    return fn_string

def f(x):
    #tmp = 1.2*pow(x,3)+2*pow(x,2)-20*x-10
    #tmp = x - 2.0*exp(-x)
    #If you are not using f_string uncomment the line above
    #If you are not using the f_string comment out the next two lines
    string = f_string()
    tmp = eval(string)
    return tmp

def main():
    a = 0.0         #define and a and b (bracketing values)
    b = 1.0
    dx = .01
    N = (int)((b-a)/dx)
    x = []
    fx = []
    for i in range(0,N+1):
        x.append(i*dx+a)
        fx.append(f(x[i]))
    print(x)
    #print(fx)

    #if you are not using f_string type in the name of the function on the next line
    function_name = f_string()
    title_base = "Plot of " + function_name
    title = title_base
    filename = "function_plot.png"
    xlabel = "x"
    ylabel = "f(x)"
    root_data_label = "root approximations"
    y_func_label = function_name


    LinePlot111(x,fx,xlabel,ylabel,title,filename)

if __name__ == '__main__':
    main()











