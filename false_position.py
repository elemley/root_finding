from math import *
from psm_plot import *
from tabulate import tabulate
import sympy as sympy

# Note this is specified def f_string():
##You can choose not to use this... Just delete it in that case

def f_string():
    fn_string = 'x - 2.0 * exp(-x)'
    #fn_string = "pow(x,3)-x-exp(x)-1+y"
    #fn_string = "-0.3*x**3"
    #fn_string = "(x**2)-(exp(x)/x)"
    return fn_string

def f(x):
    # tmp = 1.2*pow(x,3)+2*pow(x,2)-20*x-10
    string = f_string()
    tmp = eval(string)
    return tmp

def main():
    a = 0.2  # define and a and b (bracketing values)
    b = 2
    x_start = a
    x_end = b
    table = [["i","root approx.","rel. error"]]
    err_stop = 1e-3
    root_data = [a,b]
    if f(a) * f(b) < 0:
        rel_err = 1.1 * err_stop
        max_iter = 200
        xns_old = (a + b) / 2
        for i in range(0, max_iter):
            xns = (a*f(b)-b*f(a))/(f(b)-f(a))
            root_data.append(xns)
            if f(a) * f(xns) < 0:
                b = xns
            else:
                a = xns
            if i > 0:
                # calc rel_err here and compare to err_stop
                # if rel_err is less than rel_err stop the loop now
                rel_err = abs((xns-xns_old)/xns)
                table.append([i+1, xns, f"{rel_err:.2e}"])
                if rel_err <= err_stop:
                    break
            else:
                table.append([i+1, xns, "NA"])
                # if it's not put find a new xns (don't forget to store the old value in'
                # xns_old
            xns_old = xns
    else:
        print("Your a and b values do not bracket the root")

    print(tabulate(table,tablefmt="fancy_grid", headers="firstrow"))

    x = np.linspace(x_start, x_end, 100)

    function_name = f_string()
    function_syms = sympy.latex(sympy.simplify(function_name))
    title_base = "Plot of " + "$" + function_syms + "$"
    title = title_base
    filename = "false_position.png"
    xlabel = "x"
    ylabel = "f(x)"
    root_data_label = "root approximations"
    y_func_label = function_name

    FunctionRootPlot111(x, xlabel, f, ylabel, root_data, root_data_label, title, filename)


if __name__ == '__main__':
    main()

