#! /usr/bin/env python

"""
File: fill_arrays_vectorized.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 5.3
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Generates 2 arrays that have x and h(x) values
"""

import numpy as np

def h(x):
    """
    Takes input, x, and returns the value of h(x)
    """
    return (1/np.sqrt(2*np.pi))*np.exp(-1/2*(x)**2)

def genArrays():
    """
    Generates 2 arrays, x and y, that contain x and h(x) values for 41 uniformly spaced x coordinates in [-4,4]
    Inputs: N/A
    Outputs: tuple x and y with x and h(x) values, respectively
    """
    x = np.linspace(-4,4,41)
    y = h(x)
    return x,y

def test_h():
    assert(h(5) == (1/np.sqrt(2*np.pi))*np.exp(-1/2*(5)**2))

def test_y():
    x, y = genArrays()
    for i,elem in enumerate(x):
        print("y[" + str(i) + "] = " + str(h(elem)))
        assert(y[i] == h(elem))