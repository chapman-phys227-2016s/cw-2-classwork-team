"""
File: plot_ball.py 
Copyright (c) 2016 Andrew Malfavon
License: MIT

Course: PHYS227
Assignment: cw-2-classwork-team
Date: Feb 11, 2016
Email: malfa100@mail.chapman.edu
Name: Andrew Malfavon
Description: Plot a formula
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
def f(t, v):
    y = v * t - ((g * t**2) /2)
    return y

def test_f():
    #test the initial condition at time = 0.
    assert f(0, 10) == 0.0
    #test at time = 2, rounding the result to 2 decimal places.
    assert round(f(2, 10), 2) == 0.38
    #test for decimal value of t, rounding the result to 4 decimal places.
    assert round(f(1.5, 10), 2) == 3.96
    #test the end point for t, rounding the result to 3 decimal places.
    assert round(f(20 / g, 10), 3) == 0.0

def plot_here():
    #func = f(range(10.0 / g), 10)
    v = 20
    t = np.linspace(0, 2 * v / 9.8, 100)
    func = f(t, 20)
    plt.plot(t, func)
    plt.title('Trajectory of a Ball')
    plt.xlabel('time (s)')
    plt.ylabel('height (m)')
    plt.show()