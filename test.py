import urllib
import json
from datetime import datetime
import argparse
from time import sleep
from time import time

parser = argparse.ArgumentParser(description='run test against ArcGIS services')
parser.add_argument('--wait', help='wait minutes before next test')
args = vars(parser.parse_args())
wait = float(args['wait']) if args['wait'] != None else None

def output(line):
    line = '{0} {1}'.format(datetime.now().isoformat(), line)
    f = open('log.txt', 'a+')
    f.write(line+'\n')
    f.close()
    print line

def outputResponse(line, respTime):
    output('{0} Response Time: {1}ms'.format(line, int(round(respTime))))

def getData(uri, where=''):
    params = urllib.urlencode({'f': 'pjson'}) if where == '' else urllib.urlencode({'f': 'pjson', 'where': where})
    baseurl = 'http://ww1.yorkmaps.ca/arcgis/rest/services/'
    fullurl = '{0}{1}?{2}'.format(baseurl, uri, params)
    startTime = time()
    result = urllib.urlopen(fullurl).read()
    endTime = time()
    outputResponse(fullurl, (endTime - startTime)*1000)
    return json.loads(result)

while 1:
    data = getData('Hosted')
    services = data['services']
    for service in services:
        baseuri = service['name'] + '/' + service['type']
        data = getData(baseuri)
        layers = data['layers']
        for layer in layers:
            uri = baseuri + '/{0}/query'.format(layer['id'])
            # output(uri)
            data = getData(uri, 'ObjectId>0')
            if 'features' in data:
                output(len(data['features']))
            else:
                output(data)
    if wait == None:
        break;
    else:
        sleep(wait*60)

