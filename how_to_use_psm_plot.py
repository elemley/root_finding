from math import *
import numpy as np
from psm_plot import *


# Note this is specified def f_string():
def f_string():
    # fn_string = "1.2*pow(x,3)+2*pow(x,2)-20*x-10"
    # fn_string = "pow(x,3)-x-exp(x)-2"
    fn_string = "a*x*exp(0.5*x)+1.2*x -5"
    return fn_string


def f(a, x):
    string = f_string()
    tmp = eval(string)
    return tmp


def main():
    # LinePlot111
    # If you have one list
    x = np.arange(0, 10, .1)
    a1 = 0.5
    f1 = []

    for num in x:
        f1.append(f(a1, num))

    # LinePlot111(x,f1,"x","f(x)","LinePlot111","LinePlot111.png")

    # ScatterPlot111
    # To make the same plot as before but with points/markers instead of a line
    # ScatterPlot111(x,f1,"x","f(x)","ScatterPlot111","ScatterPlot111.png")

    # TwoLineColorsPlot111
    a2 = 0.8
    f2 = []
    for num in x:
        f2.append(f(a2, num))

    # To make a plot with two lines with different colors
    # TwoLineColorsPlot111(x,f1,"f1",f2,"f2","x","f(x)","TwoLineColorsPlot111","TwoLineColorsPlot111.png")

    # ThreeLineColorsPlot111
    a3 = 0.3
    f3 = []
    for num in x:
        f3.append(f(a3, num))
    # ThreeLineColorsPlot111(x,f1,"f1",f2,"f2",f3,"f3","x","f(x)","ThreeLineColorsPlot111","ThreeLineColorsPlot111.png")

    # FourLineColorsPlot111
    a4 = 0.2
    f4 = []
    for num in x:
        f4.append(f(a4, num))
    # FourLineColorsPlot111(x,f1,"f1",f2,"f2",f3,"f3",f4,"f4","x","f(x)","FourLineColorsPlot111","FourLineColorsPlot111.png")

    # FiveLineColorsPlot111
    a5 = 0.7
    f5 = []
    for num in x:
        f5.append(f(a5, num))
    # FiveLineColorsPlot111(x,f1,"f1",f2,"f2",f3,"f3",f4,"f4",f5,"f5","x","f(x)","FiveLineColorsPlot111","FiveLineColorsPlot111.png")

    # LineScatterPlot111
    # make one plot as a line and one as scatter
    #LineScatterPlot111(x,f1,f2,"x","f(x)","LineScatterPlot111","LineScatterPlot111.png")

    # LinePlot211
    # make two plots with same x
    # LinePlot211(x,f1,f2,"x","f1","f2","LinePlot211","LinePlot211.png")

    # LinePlot121
    # make two plots with same x
    # LinePlot121(x,f1,f2,"x","f1","f2","LinePlot121","LinePlot121.png")

    # LinePlot311
    # make three plots with same x
    #LinePlot311(x, f1, f2, f3, "x", "f1", "f2", "f3", "LinePlot311", "LinePlot311.png")

    # LinePlot131
    # make three plots with same x
    #LinePlot131(x, f1, f2, f3, "x", "f1", "f2", "f3", "LinePlot131", "LinePlot131.png")

    # ScatterPlot211
    # make two plots with same x
    #ScatterPlot211(x,f1,f2,"x","f1","f2","ScatterPlot211","ScatterPlot211.png")

    # ScatterPlot121
    # make two plots with same x
    #ScatterPlot121(x,f1,f2,"x","f1","f2","ScatterPlot121","ScatterPlot121.png")

    # ScatterPlot311
    # make three plots with same x
    #ScatterPlot311(x, f1, f2, f3, "x", "f1", "f2", "f3", "ScatterPlot311", "ScatterPlot311.png")

    # ScatterPlot131
    # make three plots with same x
    #ScatterPlot131(x, f1, f2, f3, "x", "f1", "f2", "f3", "ScatterPlot131", "ScatterPlot131.png")

    








if __name__ == '__main__':
    main()
