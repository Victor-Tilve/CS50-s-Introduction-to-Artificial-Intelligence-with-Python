'''
Created on 7/03/2021

@author: VATS
'''
import stackFrontier

class QueueFrontier(stackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node