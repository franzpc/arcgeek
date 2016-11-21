## Espacio para modificar directorios y direccion completa (incluido en 
## nombre y extension .shp) del archivo mascara
## Nota: Publicado en ArcGeek (www.acolita.com)
##----------------------------------------------------------------
DirectorioShapes = "D:\datosFranz\ArchivosShape"
ShapeMascara = "D:\datosFranz\ArchivosShape\Santiago_de_cali.shp"
DirectorioSalida = "D:\datosFranz\ArchivosShapeCortados"
##----------------------------------------------------------------



import glob,processing,os

listadoShapes = glob.glob(DirectorioShapes + "\\" + "*.shp")
for shp in listadoShapes:
	nombreSHP = os.path.basename(shp) #(shp[:-4])
	ShapeEntrada = DirectorioShapes + "\\" + nombreSHP
	ShapeCortado = DirectorioSalida + "\\" + nombreSHP
	processing.runalg("qgis:clip",ShapeEntrada,ShapeMascara,ShapeCortado)