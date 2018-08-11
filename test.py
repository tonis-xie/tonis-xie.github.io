import urllib
import json
params = urllib.urlencode({'f': 'pjson'})
f = urllib.urlopen("http://ww1.yorkmaps.ca/arcgis/rest/services/Hosted?%s" % params)
result = f.read()
data = json.loads(result)
print data
