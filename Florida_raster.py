import arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

def Raster_to_Contour():
    #Set up working environment
    arcpy.env.workspace = r"C:\GIS Automation\Florida Project\data"
    
    
    #Reproject Raster
    arcpy.ProjectRaster_management("03meter_smoothed.tif", "03meter_smoothed_reproject.tif", "NAD 1983 StatePlane Florida East FIPS 0901 (US Feet).prj", "NEAREST")

    #Build pyramids for Raster
    #arcpy.BuildPyramids_management("f19_resample_2_reproject.tif", "-1", "NONE", "NEAREST", "NONE", "75")

    #Convert Raster unit from meter to feet
    outRas = Raster("03meter_smoothed_reproject.tif") * 3.28
    outRas.save("03meter_smoothed_feet.tif")

    #Extract Contours
    arcpy.sa.Contour("03meter_smoothed_feet.tif", "contours_feet_1.shp", 1, 0)
    
    #Export to CAD
    input_feature = "contours_feet_1.shp"
    output_type = "DWG_R2013"
    output_file = "Contours_feet_1_crash.dwg"
    try: 
        arcpy.ExportCAD_conversion(input_feature, output_type, output_file)

    except:
        print arcpy.GetMessages()

if __name__ == '__main__':
    Raster_to_Contour()