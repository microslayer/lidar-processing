pip install geopandas
import GeoPandas

tree_layer = gpd.read_file(gpd.datasets.get_path('Z:GIS/gtech734/LastTestshp.shp'))
tree_layer = tree_layer[['shape','MYFLD']]
dissolved_tree_layer = tree_layer.dissolve(by='MYFLD')
dissolved_tree_layer.plot();
head = dissolved_tree_layer.head()
print head