"""Main module."""
def SCS_T_lag(hydraulic_length, max_retention_post_runoff, Curve_Number, average_watershed_slope):
        S= (1000/Curve_Number)-10
        T_lag= ((hydraulic_length)**0.8)* ((S + 1)**0.7)/(1900*(sqrt(average_watershed_slope)))
        return T_lag
if _name__= "__main__":
    SCS_T_lag()
    
def latitude(degree, minutes, seconds, hemisphere=""):
    coord= float(degree+ (minutes/60)+(seconds/3600))
    hemisphere = input("Enter the Hemispere")
    new_hem ="N", "North", "north", "Northern", "n", "S", "s", "South", "south","Southern"
    if hemisphere not in new_hem:
        return "Not the expected hemisphere for latitude"
    else:
        return str(coord) +  hemisphere.upper()
    
def longitude(degree, minutes, seconds, hemisphere=""):
    coord= float(degree+ (minutes/60)+(seconds/3600))
    hemisphere = input("Enter the Hemispere")
    new_hem ="E", "East", "east", "eastern", "w", "W", "e", "West", "western","Western"
    if hemisphere not in new_hem:
        return "Not the expected hemisphere for longitude"
    else:
        return str(coord) +  hemisphere.upper()
  
