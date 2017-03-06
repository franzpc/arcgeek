# ---------------------------------------------------------------------------
# Autor: Antonio Pantoja @PantojaAntonio
# Fecha: 10/01/2017
# email: apantoja.ciat@gmail.com
# Proposito: Extraer con mascara shp, desde una carpeta con archivos raster TIF
# # Nota: Basado en http:\\gis.stackexchange.com\questions\75086\how-to-for-loop-a-folder-to-batch-clip-rasters-by-polygon-using-python-and-qgis
# otra manera funcion que funciona, pero unicamente ejecutando un script Stand Alone es es usando
#			swarp= 'gdalwarp -dstnodata 0 -q -cutline %s -crop_to_cutline -of GTiff %s %s' % (ArchivoSHAPEmascara, raster, corte)
#           call(swarp)
#			Para ello se tiene que hacer la importacion:  #from subprocess import call
# Publicado en ArcGeek (www.acolita.com)
# ---------------------------------------------------------------------------

import glob,os
import subprocess


'''Modificar directorios. Note la letra r y las comillas al principio y final de la linea'''
CarpetaTIForiginales = r"D:\_Franz\04_cortarTIF_QGIS\datosFranz\TIF_originales"
ArchivoSHAPEmascara  = r"D:\_Franz\04_cortarTIF_QGIS\datosFranz\MascaraSHP\Santiago_de_cali.shp"  
CarpetaSalidaCortes  = r"D:\_Franz\04_cortarTIF_QGIS\datosFranz\SalidaCortados"



rasters = glob.glob(CarpetaTIForiginales + "\\" + "*.tif")

for raster in rasters:
	print "archivo a procesar: " + raster
	corte = CarpetaSalidaCortes + "\\" + os.path.basename(raster)	
	subprocess.call('gdalwarp -dstnodata 0 -q -cutline %s -crop_to_cutline -of GTiff %s %s' % (ArchivoSHAPEmascara, raster, corte))
