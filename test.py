import urllib
f = urllib.urlopen("http://ww1.yorkmaps.ca/arcgis/rest/services/Hosted?f=pjson")
print f.read()
