#!/usr/bin/python
'''
Created on 22.7.2013

@author: janmatilainen
'''

if __name__ == '__main__':
    pass
import time
from datetime import datetime
from  pyReadCpu import cpuMonitor
#from pyInOut import myIO
import cherrypy
 

class myCherry:
    def index(self):
        appname = "spotify"
        top = cpuMonitor(appname)
        myTop = top.readTop()
        cpu = cpuMonitor(appname)
        cpu_usage = cpu.readAppTop()
        cpu = str(cpu_usage)
        timestamp = datetime.now().time()
        logthis = "<th>" + str(timestamp) + "</th><th>" + cpu + "</th>"  
        log_cell = str(logthis)
        myRow = []
        myColumn = []
        top_cell = ""
    
        for x in xrange(len(myTop)):
            myRow.append(myTop[x].split())
#             print myRow[x]
            top_cell += "<tr><th>" + str(myRow[x]).replace('[', '').replace(']', '').replace('\'','').replace(',','</th><th>') + "</th></tr>"
            
        str1 =  str(top_cell)
#        top_cell.append(str(myRow))
#        log_cell = str(logthis)
        return '<html><center><table border="1"><tr><th>{str1}</th></tr><th><tr><th>{appname}</th>{log_cell}</th></tr></table></center></html>'.format(**vars())
    index.exposed = True
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.server.socket_port = 8787
cherrypy.quickstart(myCherry())

'''
Looping eternally. 1 round lasts 5 second, so we'll get 
good enough statistics from my point of view. 
We could let the application also to just plain run there all the time and fetch the stats
With browser when needed
using spotify as an application get the data from
most likely we should already know what app (the name of the application) we're tracking
 the appname is used by pyReadCpu to fetch the pid and the cpu usage
 The pid should however be stored somewhere in the system already
 in case all the applications we have store the pid -files in same folder on the server,
 we could easily monitor ALL of them by fetching the pids from pid -files

while (True):

    
    #print logthis
    f = open('./cpulog.log','a+')
    f.write(logthis)
    f.close()

    
    
    f2 = open('./toplog','a+')
    f2.write(str(timestamp) + "\n")
        
    for x in xrange(11):
            #print str(myTop[x])
            #f = open('./toplog','a+')
            f2.write(str(myTop[x] + "\n"))
    f2.close()
    
    time.sleep(5)
'''