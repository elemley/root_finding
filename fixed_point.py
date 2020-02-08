from math import *
from psm_plot import *
from tabulate import tabulate
import sympy as sympy


#Note this is specified def f_string():
def g_string():
    #fn_string = "1.2*pow(x,3)+2*pow(x,2)-20*x-10"
    fn_string = "5/(exp(0.5*x)+1.2)"
    return fn_string

def f_string():
    fn_string = "x*exp(0.5*x)+1.2*x -5"
    return fn_string

def f(x):
    string = f_string()
    tmp = eval(string)
    return tmp

def g(x):
    string = g_string()
    tmp = eval(string)
    return tmp

def main():
    xold = 2.0     #initial guess of x
    root_approx = [xold]

    err_stop = 1e-5     #adjust as needed...
    rel_err = 1.1*err_stop  #set value large enough to start process
    count = 0
    max_iter = 5

    table = [["i","root approx.","rel. error"]]

    for i in range(0,max_iter):
        count+=1
        tmp = g(xold)
        xnew = tmp
        root_approx.append(xnew)
        if count > 1:
            rel_err = abs((xnew-xold)/xnew)
            table.append([i + 1, xnew, f"{rel_err:.2e}"])
            if rel_err <= err_stop:
                break
        else:
            table.append([i+1, xnew, "NA"])
            # if it's not put find a new xns (don't forget to store the old value in'
            # xns_old
        xold = xnew

    print(tabulate(table,tablefmt="fancy_grid", headers="firstrow"))

    x_start = 1
    x_end = 2.5
    x = np.linspace(x_start, x_end, 100)

    function_name = f_string()
    function_syms = sympy.latex(sympy.simplify(function_name))
    title_base = "Plot of " + "$" + function_syms + "$"
    title = title_base
    filename = "fixed_point.png"
    xlabel = "x"
    ylabel = "f(x)"
    root_data_label = "root approximations"
    y_func_label = function_name

    FunctionRootPlot111(x, xlabel, f, ylabel, root_approx, root_data_label, title, filename)


if __name__ == '__main__':
    main()



