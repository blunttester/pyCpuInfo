'''
Created on 22.7.2013

@author: janmatilainen
'''
#import 
from datetime import datetime

class myIO(object):
    '''
    classdocs
    '''


    def __init__(self, cpuinfo):
        '''
        Constructor
        '''
        self.cpuinfo = cpuinfo
        self.timestamp = datetime.now().time()
        
    def writeToFile (self):
        f = open('./cpulog.log','a+')
        f.write('tadaa\n')
        f.write(self.timestamp + ';' + self.cpuinfo)
        f.close()

        
        