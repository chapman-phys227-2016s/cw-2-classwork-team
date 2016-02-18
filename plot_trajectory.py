#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys

def trajectory_function(x, theta, v0 , y0 ) :
    """
    Returns the trajectory of a ball as a function of:
    x: the coordinate along the ground in meters
    v0: the initial velocity in m/s (optional)
    theta: the angle the ball makes with the y axis, in radians (optional)
    y0: initial height (optional)
    """
    
    return x * np.tan(theta) - ( 9.8 * x**2 / (2 * v0** 2 * (np.cos(theta) ** 2))) + y0

def test_zeros():
    """
    Tests trajectory function with x = 0, theta = pi, v0 = 1, and y0 = 0
    asserting that the target trajectory is 0
    """
    target_trajectory = 0.0
    assert (trajectory_function(0, np.pi, 1, 0) == target_trajectory)

def plot_trajectory_function():
    """
    Plots the trajectory given the command line arguements
    over the range -5 to 5 with points at the interval .1
    """
    t = np.arange(-5,5, .1)
    plt.plot(t,trajectory_function(t),'g^')
    plt.show()
    return

def plot_trajectory_function(theta, v0, y0):
    """
    Plots the trajectory given the arguements theta, v0, and y0
    over the range -5 to 5 with points at the interval .1
    """
    t = np.arange(-5,5, .1)
    plt.plot(t,trajectory_function(t, float(theta), float(v0), float(y0)),'g^')
    plt.show()
    return

def main():
    #print(trajectory_function(1,float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))))
    #plot_trajectory_function()
    return


if __name__ == "__main__":
    main()