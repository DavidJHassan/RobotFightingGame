from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import NodePath
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode

class Robot(NodePath):
    
    def __init__(self, x, y, z):
        NodePath.__init__(self,loader.loadModel("models/box"))
 
        min, max = self.getTightBounds()
        size = max - min
        maximum = -1
        for i in size:
            if i > maximum:
                maximum = i

        self.reparentTo(render)
        self.setPos(x, y, z)

        self.cnode = CollisionNode('CSrobot')
        self.cnode.addSolid(CollisionSphere(0,0,0,maximum + 0.3))
        self.cnodePath = self.attachNewNode(self.cnode)
        self.cnodePath.show()

            
