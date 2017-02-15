#Challenge 1
#In ArcGIS Desktop Help, research the AddLayer function of the ArcPy
#mapping module and use it to write a script that adds the parks layer
#from the Parks data frame in Austin_TX.mxd to the other two data
#frames in the same map document.
#Gina Fonseca 
import arcpy

mxd = arcpy.mapping.MapDocument(r"C:\EsriPress\Python\Data\Exercise10\Austin_TX.mxd") #MXD I used to accomplish the INsert Layer
dfPark= arcpy.mapping.ListDataFrames(mxd, "Parks")[0] #this variable references the data frame the park lyr is located
insertLayer=arcpy.mapping.ListLayers(mxd, "Parks", dfPark)[0] #this is the park lyr

dfFacil = arcpy.mapping.ListDataFrames(mxd, "Facilities")[0] # These variables reference the Data Frames I want to put the parks lyr in.
dfStreet = arcpy.mapping.ListDataFrames(mxd, "Street Trees")[0]

refFacil = arcpy.mapping.ListLayers(mxd, "",dfFacil)[0]   #these are variables created it determines the location where the new layer will be inserted
refStreet = arcpy.mapping.ListLayers(mxd, "", dfStreet)[0]



arcpy.mapping.InsertLayer(dfFacil, refFacil, insertLayer, "BEFORE") # Here is where the magic happens all my variables come together here so the park lyr is inserted
arcpy.mapping.InsertLayer(dfStreet, refStreet, insertLayer, "AFTER")



mxd.saveACopy(r"C:\EsriPress\Python\Data\Exercise10\Austin_TX2.mxd") # creates a copy
del mxd
del insertLayer #removes locks
print "All done!"

#InsertLayer (, reference_layer, insert_layer, {insert_position})
#data frames son Street Trees y Facilities
#Variable for both frames 
#DF, Ref for each 
