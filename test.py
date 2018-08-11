import urllib
import json

def getData(uri, where=''):
    params = urllib.urlencode({'f': 'pjson'}) if where == '' else urllib.urlencode({'f': 'pjson', 'where': where})
    baseurl = 'http://ww1.yorkmaps.ca/arcgis/rest/services/'
    fullurl = '{0}{1}?{2}'.format(baseurl, uri, params)
    print fullurl
    f = urllib.urlopen(fullurl)
    result = f.read()
    return json.loads(result)

data = getData('Hosted')
services = data['services']
for service in services:
    uri = service['name'] + '/' + service['type']
    data = getData(uri)
    layers = data['layers']
    for layer in layers:
        uri += '/{0}/query'.format(layer['id'])
        data = getData(uri, 'ObjectId>0')
        print len(data['features'])
