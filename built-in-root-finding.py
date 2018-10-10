from math import *
import scipy.optimize
from string import *
from psm_plot import *
from random import *

#Note this is specified def f_string():
def f_string():
    fn_string = "x*exp(0.5*x)+1.2*x -5"
    return fn_string

def f(x):
    string = f_string()
    tmp = eval(string)
    return tmp

def main():
    #There are many built-in root finding techniques in scipy. Below are some examples of using them.

    #These functions are part of scipy.optimize

    #bisection

    #scipy.optimize.bisect(f, a, b, args=(), xtol=2e-12, rtol=8.881784197001252e-16, maxiter=100, full_output=False,disp=True)

        #Mostly only worry about the first three arguments, but if you need to use more:
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html#scipy.optimize.bisect
        # returns x0 - a float that is root of f between a and b

    a = 1.0     #left side of bracketing values for root
    b = 2.0     #right side of bracketing values for root
    x0 = scipy.optimize.bisect(f,a,b)
    generic_output = "The result of using {} on {} {} {} {} {} is {}"
    print(generic_output.format("bisection", f_string(), "between", a, "and", b, x0 ))



if __name__ == '__main__':
    main()


