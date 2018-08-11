import urllib
import json
from datetime import datetime

def output(line):
    line = '{0} {1}'.format(datetime.now().isoformat(), line)
    f = open('log.txt', 'a+')
    f.write(line+'\n')
    f.close()
    print line

def getData(uri, where=''):
    params = urllib.urlencode({'f': 'pjson'}) if where == '' else urllib.urlencode({'f': 'pjson', 'where': where})
    baseurl = 'http://ww1.yorkmaps.ca/arcgis/rest/services/'
    fullurl = '{0}{1}?{2}'.format(baseurl, uri, params)
    output(fullurl)
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
        if 'features' in data:
            output(len(data['features']))
        else:
            output(data)
