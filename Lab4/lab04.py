import arcpy

# GDB for Lab04
folder_path= r'C:\\Users\\Grady\\Desktop\\GISlab\\GISprogramming'
gdb_name='GISprogramming_Lab04.gdb'
gdb_path=folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path,gdb_name)

# read csv
csv_path= r'C:\\Users\\Grady\Desktop\\GISlab\\GISprogramming\\Lab04\\Lab04_Data\\garages.csv'
garage_layer_name= 'Garage_Points'
garages= arcpy.MakeXYEventLayer_management(csv_path,'x','y',garage_layer_name)

# put garages in gdb
input_layer=garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer,gdb_path)

#get garage_points layer
garage_points= gdb_path + '\\' + garage_layer_name


campus= r'C:\\Users\\Grady\Desktop\\GISlab\\GISprogramming\\Lab04\\Lab04_Data\\campus.gdb'
buildings_campus= campus + '\\Structures'

buildings= gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus,buildings)

spatial_ref= arcpy.Describe(buildings).spatialReference

arcpy.Project_management(garage_points,gdb_path + '/Garage_points_reprojected',spatial_ref )

garageBuffered= arcpy.Buffer_analysis(gdb_path + '\Garage_points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

arcpy.Intersect_analysis([garageBuffered,buildings], gdb_path +'\Garage_Building_intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path+ '\Garage_Building_intersection.dbf',r'C:\\Users\\Grady\Desktop\\GISlab\\GISprogramming\\Lab04\\Lab04_Data', 'nearbyBuildings.csv')
