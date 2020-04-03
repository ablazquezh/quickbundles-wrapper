# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:39:52 2020

@author: Alberto Blázquez Herranz (alb.blazquez.h@gmail.es)


QuickBundles Wrapper for Time Series data clustering.
Module functionalities:
    
    + data preparation (including resampling, metric setup and rearrangement of data).
        - TODO: enrich available metrics' pool to enable metric selection. This will
        aid adequation to more problems apart from geolocated data.
        
    + automated clustering with hyperparameter tuning.
        - TODO: look for better performance metrics than silhouette (which may be
        flawing a bit). Possible 'performance metric selection' capability.
        
Last update - 03/04/2020
Currently, this functionalities support 1D and 2D data.
In case timestamps are not provided, data is assumed to be in ascending order.
"""


