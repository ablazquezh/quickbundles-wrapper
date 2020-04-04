# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:33:36 2020

@author: Alberto Blázquez Herranz (alb.blazquez.h@gmail.es)

QuickBundles Wrapper for Time Series data clustering.

Input formatting function.

Last update - 04/04/2020
Provides functionality for adapting the input-data format to the requirements 
of the QuickBundles module.
Supported input formats:
    
    + (2D data) Nested lists.
"""

import numpy as np

def format_trajectory_set(trajectory_set):
    """
    This function converts a trajectory (or set of trajectories) into the adequate format for its processing
    by QuickBundles algortihm (numpy matrix [[X][Y]] - list of these matrices if a set of trajectories is passed).
    """
    
    formatted_trajectories = None
    
    if len(trajectory_set) >= 2:
    
        formatted_trajectories = []
        for i in range(len(trajectory_set)):
        
            formatted_trajectories.append(np.asarray([ x for x in zip(trajectory_set[i][0], trajectory_set[i][1]) ]))
    else:
    
        formatted_trajectories = np.asarray([ x for x in zip(trajectory_set[0], trajectory_set[1]) ])
    
    return formatted_trajectories 