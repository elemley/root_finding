
from math import *
import numpy as np
import matplotlib.pyplot as plt

def my_plotter(ax,data1, data2, param_dict):
    out = ax.plot(data1,data2,**param_dict)
    return out


def main():
    """
    fig = plt.figure()
    fig.suptitle('No axes on this figure')
    fig, ax_lst = plt.subplots(2,2)
    """

    """
    x = np.linspace(0,2,100)
    plt.plot(x,x,label='linear')
    plt.plot(x,x**2,label='quadratic')
    plt.plot(x,x**3,label='cubic')

    plt.xlabel('x label')
    plt.ylabel('ylabel')
    plt.title("Basic Plot")
    plt.legend()
    plt.show()
    """

    """
    x = np.arange(0,10,0.2)
    y=np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.show()
    """

    """
    data1, data2, data3, data4 = np.random.randn(4,100)
    fig, (ax1,ax2) = plt.subplots(1,2)
    my_plotter(ax1,data1,data2,{'marker':'x'})
    my_plotter(ax2, data3, data4, {'marker': 'o'})
    plt.show()
    """


    plt.ioff()
    for i in range(3):
        plt.plot(np.random.rand(10))
        plt.show()













if __name__ == '__main__':
    main()












