"""The common module contains common functions and classes used by the other modules.
"""
from math import sqrt
def hello_world():
    """Prints "Hello World!" to the console.
    """
    print("Hello World!")
def SCS_T_lag(hydraulic_length, max_retention_post_runoff, Curve_Number,           average_watershed_slope):
        S= (1000/Curve_Number)-10
        T_lag= ((hydraulic_length)**0.8)* ((S + 1)**0.7)/(1900*(sqrt          (average_watershed_slope)))
        return T_lag