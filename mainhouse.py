from spawnerhouse import spawnerh

def curvecreatorh(polist, building_gdf,angle_weight,first_value,second_value,status,radius):  
    #define amunt of iterations
    radius = radius/0.6*2

    #dynamic iteration count:
    # <= 1 km  -> 6 iterations
    # >= 50 km -> 12 iterations
    #between   -> linear interpolation
    min_radius = 1000        #1 km
    max_radius = 50000       #50 km
    min_iter = 6
    max_iter = 11
    
    if radius <= min_radius:
        iternumber = min_iter
    elif radius >= max_radius:
        iternumber = max_iter
    else:
        t = (radius - min_radius) / (max_radius - min_radius)
        iternumber = round(min_iter + t * (max_iter - min_iter)) 

    if angle_weight <= 500:
        iternumber = iternumber +1
    if angle_weight <= 50:
        iternumber = iternumber +1
    #iternumber = 12 #iterations maybe based on line length (this is the old verison that doesnt have that
    
    #main loop
    for k in range(int(iternumber)):
        status.value = f"<b style='color: green;'>{k}/{iternumber}</b>"
        #insert and move points
        polist = spawnerh(polist, k, building_gdf,angle_weight,first_value,second_value)
    #print(polist)
    return polist

#curvecreator([(0.1,0.1),(0.2,0.2),(0.3,0.4),(0.5,0.6)])
