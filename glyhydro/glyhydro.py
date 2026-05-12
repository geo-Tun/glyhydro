"""Main module."""
def SCS_T_lag(hydraulic_length, max_retention_post_runoff, Curve_Number, average_watershed_slope):
        S= (1000/Curve_Number)-10
        T_lag= ((hydraulic_length)**0.8)* ((S + 1)**0.7)/(1900*(sqrt(average_watershed_slope)))
        return T_lag
if _name__= "__main__":
    SCS_T_lag()
    

