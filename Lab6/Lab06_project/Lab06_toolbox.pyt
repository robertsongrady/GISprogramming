# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools =[RenderTool]


class RenderTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        param0= arcpy.Parameter(displayName="Your working project",name="workProject",datatype="DEFile",parameterType="Required",direction="Input")
        param1= arcpy.Parameter(displayName="Name of the layer you want to render",name="layername",datatype="GPString",parameterType="Required",direction="Input")
        param2= arcpy.Parameter(displayName="Folder of the new project for saving the render layer",name="newproject folder",datatype="DEFolder",parameterType="Required",direction="Input")
        param3 = arcpy.Parameter(displayName="Name of the new project for saving the render layer",name="newprojectname",datatype="GPString",parameterType="Required",direction="Input")
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        # Define our progressor variables
        readTime =2.5
        start =8
        maximum = 100
        step = 25

        # Setup the progressor
        arcpy.SetProgressor("step","Checking project and layer...", start, maximum, step)
        time.sleep(readTime)
                            
        # Add message to the results pane
        arcpy.AddMessage("Checking project and layer...")

        # Reference to our .aprx
        aprxFileAddress = parameters[0].valueAsText
        project= arcpy.mp.ArcGISProject(aprxFileAddress)
        layername= parameters[1].valueAsText

        #Grab the layer in the .aprx
        if layername=='GarageParking':
            layer =project.listMaps('Map')[0].listLayers()[1]
            symbology = layer.symbology

            # Increment the progressor and change the label; add message to the results pane
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel("start to update render...")
            time.sleep(readTime)
            arcpy.AddMessage("start to update render...")

            # Update the copy's renderer to be 'Graduated Colors Renderer'
            symbology.updateRenderer('GraduatedColorsRenderer')

            # Tell arcpy which field we want to base our choropleth off of
            symbology.renderer.classificationField= "Shape_Area"

            # Increment the progressor and change the label; add message to the results pane
            arcpy.SetProgressorPosition(start + step + step)
            arcpy.SetProgressorLabel("setting render...")
            time.sleep(readTime)
            arcpy.AddMessage("setting render...")

            # Set how many classes we'll have
            symbology.renderer.breakCount = 5

            # Set the color ramp
            symbology.renderer.colorRamp =project.listColorRamps ('Oranges (5 Classes)')[0]
            # Set the layer's actual symbology equal to the copy's

            layer.symbology = symbology 

            # Increment the progressor and change the label; add message to the results pane
            arcpy.SetProgressorPosition (maximum)
            arcpy.SetProgressorLabel("saving project...")
            time.sleep(readTime)
            arcpy.AddMessage("saving project...")

        if layername =='Structures':
            layer = project.listMaps('Map')[0].listLayers()[0]
            symbology =layer.symbology
            # Increment the progressor and change the label; add message to the results pane
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel("start to update render...")
            time.sleep(readTime)
            arcpy.AddMessage("start to update render...")

            # Update the copy's renderer to be "UniqueValueRenderer"
            symbology.updateRenderer('UniqueValueRenderer')
                                     
            # Increment the progressor and change the label; add message to the results pane
            arcpy.SetProgressorPosition(start + step + step)
            arcpy.SetProgressorLabel("setting render...")
            time.sleep(readTime)
            arcpy.AddMessage("setting render...")

            # Tells arcpy that we want to use "Type" as our unique value
            symbology.renderer.fields= ["Type"]

            # Set the layer's actual symbology equal to the copy's
            layer.symbology =symbology #Very important step

            # Increment the progressor and change the label; add message to the results pane
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel("saving project...")
            time.sleep(readTime)
            arcpy.AddMessage("saving project...")
        else:
            arcpy.AddMessage("We can't work with this layer.")

        newprojectpath = parameters [2].valueAsText + "\\" + parameters [3].valueAsText
        project.saveACopy (newprojectpath)
        arcpy.AddMessage("Done!")
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
