'''
Created on 16.7.2013

@author: janmatilainen
'''
import subprocess
from datetime import datetime

class cpuMonitor(object):
    '''
    classdocs
    '''


    def __init__(self,appname):
        '''
        Constructor
        '''
        self.appname = appname
        
    def readCpu(self):
        """Return int containing CPU -usage used by defined application name."""
        self.process = subprocess.Popen("ps -o pcpu -p `ps -ef | grep -i %s | grep -v grep |grep -v Users| awk '{ print $2 }'`" % self.appname,
                                        shell=True,
                                        stdout=subprocess.PIPE,
                                        )
        self.cpu = self.process.communicate()[0].split('\n')
        #self.process.terminate()
        #print float(self.cpu[1])
        #cpu = float(self.cpu[1])
        return float(self.cpu[1])
    
    def readTop(self):
        timestamp = datetime.now().time()
        self.process = subprocess.Popen("top -stats pid,rsize,vsize,cpu,th,pstate,time,command -o cpu -O +rsize -s 2 -n 10 -l 2| grep -A10 PID",
                                        shell=True,
                                        stdout=subprocess.PIPE)
        self.top = self.process.communicate()[0].split('\n')
### Since the first captured top output does not contain the wanted data,
### we remove the first 13 elements 

        for x in xrange(12):
            del self.top[0]

        return self.topq
        
    def readAppTop(self):
        timestamp = datetime.now().time()
        self.app = subprocess.Popen("ps -ef | grep -i %s | grep -v grep |grep -v Users| awk '{ print $2 }'" % self.appname,
                                        shell=True,
                                        stdout=subprocess.PIPE)
        self.appPid = self.app.communicate()[0].split('\n')
        #print self.appPid[0]
        
        self.process = subprocess.Popen("top -pid %s -stats pid,rsize,vsize,cpu,th,pstate,time,command -o cpu -O +rsize -s 2 -n 1 -l 2| grep -A10 PID" % self.appPid[0],
                                        shell=True,
                                        stdout=subprocess.PIPE)
        self.appTop = self.process.communicate()[0].split('\n')
### Since the first captured top output does not contain the wanted data,
### we remove the first 1st elements 

        return self.appTop[1]