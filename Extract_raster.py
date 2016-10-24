# ---------------------------------------------------------------------------
# Autor: Antonio Pantoja @PantojaAntonio
# Fecha: 11/10/2016
# email: apantoja.ciat@gmail.com
# Proposito: Extraer con mascara shp o raster, sirve para una sola carpeta ejemplo worldclim
# Nota: Publicado en ArcGeek (www.acolita.com)
# ---------------------------------------------------------------------------

import arcpy,os
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

os.system('cls')


CarpetaEntrada = raw_input("\nIndique carpeta de entrada (con varios archivos Raster) ")
ArchivoMascara = raw_input("\nEntrar el archivo mascara, capa raster o archivo shp (Incluyendo extension .shp)")
CarpetaSalida = raw_input("\ncarpeta salida de los nuevos raster cortados ")



arcpy.env.workspace = CarpetaEntrada 
rasters = arcpy.ListRasters("*", "GRID")
for raster in rasters:
	print raster
	arcpy.env.snapRaster = raster
	corte = CarpetaSalida + "\\" + raster

	outExtractByMask = ExtractByMask(raster, ArchivoMascara)
	outExtractByMask.save(corte)

print "Proceso terminado !!!"
print "revisar: " , CarpetaSalida    
