#! /usr/bin/env python

"""
File: read_2columns.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module plots the points of two lists of data, as well as printing the maximum and minimum values of the generated arrays.

"""

import numpy as np
import matplotlib.pyplot as plt

def data_prep1(filename='xy.dat'):
    """Processes files of two columns into two seperate, vectorized data sets."""
    infile = open(filename)
    x_data = []
    y_data = []
    for line in infile:
        data = line.split()
        x_data.append(float(data[0]))
        y_data.append(float(data[1]))
    x_data = np.array(x_data)
    y_data = np.array(y_data)
    return x_data, y_data

def data_prep2(filename='xy.dat'):
    """Processes files of two columns into two seperate, vectorized data sets."""
    data = np.loadtxt(filename, dtype=np.float)
    return data[:,0], data[:,1]

def data_plot_display(xinfo=data_prep1()[0], yinfo=data_prep1()[1]):
    """Plots the data given and prints the max and mean of both data sets."""
    print 'Max x:  ' + str(np.amax(xinfo))
    print 'Max y:  ' + str(np.amax(yinfo))
    print 'Mean x:  ' + str(np.mean(xinfo))
    print 'Mean y:  ' + str(np.mean(yinfo))
    plt.plot(xinfo, yinfo, 'bo')
    plt.show()

def test_other_file1(filename='testerfile.dat'):
    """Uses a specified testfile to ensure that the indexes were correct."""
    test_run = data_prep1(filename)
    apt = (test_run[0][2] == 2) and (test_run[1][2] == 2)
    msg = 'Values indexed incorrectly.'
    assert apt

def test_other_file2(filename='testerfile.dat'):
    """Uses a specified testfile to ensure that the indexes were correct."""
    test_run = data_prep2(filename)
    apt = (test_run[0][2] == 2) and (test_run[1][2] == 2)
    msg = 'Values indexed incorrectly.'
    assert apt
