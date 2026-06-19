from spawnerhouse import spawnerh

def curvecreatorh(polist, building_gdf,angle_weight,first_value,second_value):  
    #define amunt of iterations
    iternumber = 12 #iterations maybe based on line length
    #main loop
    for k in range(int(iternumber)):
        #insert and move points
        polist = spawnerh(polist, k, building_gdf,angle_weight,first_value,second_value)
    #print(polist)
    return polist

#curvecreator([(0.1,0.1),(0.2,0.2),(0.3,0.4),(0.5,0.6)])
