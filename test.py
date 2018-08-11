import urllib
import json

def getData(uri):
    params = urllib.urlencode({'f': 'pjson'})
    baseurl = 'http://ww1.yorkmaps.ca/arcgis/rest/services/'
    fullurl = '{0}{1}?{2}'.format(baseurl, uri, params)
    print fullurl
    f = urllib.urlopen(fullurl)
    result = f.read()
    return json.loads(result)

data = getData('Hosted')
services = data['services']
for service in services:
    data = getData(service['name'] + '/' + service['type'])
    print data['layers']
