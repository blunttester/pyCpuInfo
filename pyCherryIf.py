'''
Created on 22.7.2013

@author: janmatilainen
'''
#from pyPlotter import *

import cherrypy

class Resource(object):

    def __init__(self, content):
        self.content = content

    exposed = True

    def GET(self):
        return self.to_html(self.content)

class ResourceIndex(Resource):
    def to_html(self, toplog):
        self.toplog = toplog
 
        f = open('./cpulog.log','r')
        html_item = f.read()
        f.close()
        plot_item = toplog

                
        return '<html><center><table border="1"><tr><th>{plot_item}</th></tr><th><tr>{html_item}</th></tr></table></center></html>'.format(**vars())


conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8787,
    },
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.staticdir.debug': True
    }
}

cherrypy.quickstart(ResourceIndex(Resource), '/', conf)