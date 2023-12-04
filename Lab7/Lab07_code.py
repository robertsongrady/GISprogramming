import arcpy
source = r"C:\\Users\\Grady\\Desktop\\GISlab\\GISprogramming\\Lab07\\Lab07_Data\\"
result= r"C:\\Users\\Grady\Desktop\\GISlab\\GISprogramming\\Lab07\\Lab07_results\\"
band1 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF") # blue
band2 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF") # green
band3 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF") # red
banda = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF") # NIR
# composite all bands

composite = arcpy.CompositeBands_management([band1,band2,band3,banda], result + "combined.tif")


# Using DEM to create hillshade
azimuth = 315

altitude = 45

shadows = "NO_SHADOWS"

z_factor = 1

arcpy.ddd.HillShade(source + r"\\n30_w097_1arc_v3.tif", result + r"\\hillshade.tif", azimuth, altitude, shadows, z_factor)

 # Using DEM to create slope image

output_measurement = "DEGREE"

z_factor = 1
arcpy.ddd.Slope(source + r"\\n30_w097_1arc_v3.tif", result + r"\\slopes.tif", output_measurement, z_factor)
