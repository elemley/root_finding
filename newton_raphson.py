from math import *
from psm_plot import *
from tabulate import tabulate
import sympy as sympy

# Note this is specified def f_string():
##You can choose not to use this... Just delete it in that case

def f_prime(x):
    tmp = 1+2.0*exp(-x)
    return tmp

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
    xi = 0.4
    table = [["i","root approx.","rel. error"]]
    err_stop = 1e-6
    root_data = [xi]
    rel_err = 1.1 * err_stop
    max_iter = 200
    table.append([1, xi, "NA"])

    for i in range(0, max_iter):
        xi_1 = xi - f(xi)/f_prime(xi)
        root_data.append(xi_1)
        # calc rel_err here and compare to err_stop
        # if rel_err is less than rel_err stop the loop now
        rel_err = abs((xi_1 -xi)/xi_1)
        table.append([i+2, xi_1, f"{rel_err:.2e}"])
        if rel_err <= err_stop:
            break
        xi = xi_1

    print(tabulate(table,tablefmt="fancy_grid", headers="firstrow"))

    x = np.linspace(x_start, x_end, 100)

    function_name = f_string()
    function_syms = sympy.latex(sympy.sympify(function_name))
    title_base = "Plot of " + "$" + function_syms + "$"
    title = title_base
    filename = "newton_raphson.png"
    xlabel = "x"
    ylabel = "f(x)"
    root_data_label = "root approximations"
    y_func_label = function_name

    FunctionRootPlot111(x, xlabel, f, ylabel, root_data, root_data_label, title, filename)


if __name__ == '__main__':
    main()

