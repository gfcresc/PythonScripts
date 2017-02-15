import arcpy, arcinfo

from arcpy.sa import* # this is so i can use the map algebra functions for the rasters 



class LicenseError(Exception): # I open this to account for any possible errors that might happen
    pass

try:  # I want to check first if the license is available before I have it do anything
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
    else:
        print "You don't have this license"
        raise LicenseError

    arcpy.env.workspace = "c:/EsriPress/Python/Data/Exercise09"  #raster workspace
    raster1 = arcpy.Raster("elevation") #varieble for the raster I want to work with

    rasterslope = Slope(raster1) # calculate the slope
    print "Slope Calculated"

    rasteraspect = Aspect(raster1) #calculate the aspect
    print "Aspect Calculated"

    rasterlandcov = Raster("landcover.tif") #grabbing the landcover tif
    print "Getting that other raster"

    moderateS = ((rasterslope > 5) & (rasterslope < 20))  # the specifics asked for in the instructions
    print "A moderate slope? Ok " #moderate sloper from 5 - 20

    southaspect = ((rasteraspect > 150) & (rasteraspect < 270))
    print"South Aspect? DONE"  #south aspect from 150 - 270

    forested = ((raster1 == 41) |(raster1 == 42)|(raster1 == 43))
    print "Forested? Sure" # Forested  41, 42, 43




    rasterfinal = (moderateS * southaspect * forested) # here all the rasters are combined
    print " Mixing it all together and saving it! "
    rasterfinal.save('NewRaster') #here is where the final raster is saved
    print "All Done! "

    arcpy.CheckInExtension("Spatial") 

except LicenseError:
    print("Spatial Analyst license is unavailable")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(-1)) # to get the last error message.