from math import *
import sympy as sympy
import numpy as np
from psm_plot import *

#Note this is specified def f_string():
def f_string():
    fn_string = "x**3-x-exp(x)-1"
    #fn_string = "-0.3*x**3"
    return fn_string

def f(x):
    string = f_string()
    tmp = eval(string)
    return tmp

def main():
    x = 1.0
    print(f(x))
    print("x=", x)
    print(f"f(x)= {f_string()} = {f(x)}")

    xvals = np.linspace(-1,1)

    function_name = f_string()
    function_syms = sympy.latex(sympy.simplify(function_name))
    title_base = "Plot of " + "$" + function_syms + "$"
    title = title_base
    filename = "fn_string_example.png"
    xlabel = "x"
    ylabel = "f(x)"
    #root_data_label = "root approximations"
    #y_func_label = function_name

    Function0Plot111(xvals,f,xlabel,ylabel,title,filename)


    #FunctionRootPlot111(x, xlabel, f, ylabel, root_data, root_data_label, title, filename)




if __name__ == '__main__':
    main()















