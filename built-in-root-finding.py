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

def fprime_string():
    fn_string = "exp(0.5*x)+0.5*x*exp(0.5*x)+1.2"
    return fn_string

def fprime(x):
    string = fprime_string()
    tmp = eval(string)
    return tmp

def fprime2_string():
    fn_string = "0.5*exp(0.5*x)+0.5*(exp(0.5*x)+0.5*x*exp(0.5*x))"
    return fn_string

def fprime2(x):
    string = fprime_string()
    tmp = eval(string)
    return tmp

def main():
    #There are many built-in root finding techniques in scipy. Below are some examples of using them.

    #These functions are part of scipy.optimize

    #bisection

    #   scipy.optimize.bisect(f, a, b, args=(), xtol=2e-12, rtol=8.881784197001252e-16, maxiter=100, full_output=False,disp=True)

        #Mostly only worry about the first three arguments, but if you need to use more:
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html#scipy.optimize.bisect
        # returns x0 - a float that is root of f between a and b

    a = 1.0     #left side of bracketing values for root
    b = 2.0     #right side of bracketing values for root
    x0 = scipy.optimize.bisect(f,a,b)
    generic_output = "The result of using {} on {} {} {} {} {} is {}"
    print(generic_output.format("bisection", f_string(), "between", a, "and", b, x0 ))



    #   scipy.optimize.newton(func, x0, fprime=None, args=(), tol=1.48e-08, maxiter=50, fprime2=None)[source]

        #At a minimum you need the function and a starting guess for the root (x0)
        #If you supply fprime - Newton-Raphson is used. If not Secant is used.
        #If you supply fprime2 a technique that can use the second derivative is used (Halley's method)
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html#scipy.optimize.newton
        # returns x0 - a float that is root of f


    x0_guess = 2.0  # initial guess for root
    x0 = scipy.optimize.newton(f,x0_guess)
    print(generic_output.format("secant", f_string(), "starting at", x0_guess, "", "", x0))

    x0 = scipy.optimize.newton(f,x0_guess,fprime)
    print(generic_output.format("Newton-Raphson", f_string(), "starting at", x0_guess, "", "", x0))

    x0 = scipy.optimize.newton(f,x0_guess,fprime,fprime2=fprime2)
    print(generic_output.format("Halley's Method", f_string(), "starting at", x0_guess, "", "", x0))

if __name__ == '__main__':
    main()


