from math import *

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import NodePath
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode
from panda3d.core import CollisionHandlerEvent
from panda3d.core import Vec3

class Bullet(NodePath):
    
    def __init__(self, x, y, z, direction, id):
        NodePath.__init__(self,loader.loadModel("models/box"))
 
        self.reparentTo(render )
        self.setPos(x, y, z)
        
        self.direction = Vec3()
        self.direction.set(direction.getX(), direction.getY(), direction.getZ())
        
        if self.direction.length() == 0:
            self.removeNode()
            return
        
        self.direction /= direction.length()
        
        min, max = self.getTightBounds()
        size = max - min
        maximum = -1
        for i in size:
            if i > maximum:
                maximum = i

        self.cnode = CollisionNode('bullet')
        self.cnode.setTag( "id", str(id) )
        self.cnode.addSolid(CollisionSphere(0, 0, 0, maximum + 0.3))
        self.cnodePath = self.attachNewNode(self.cnode)
        self.cnodePath.show()
        base.cTrav.addCollider(self.cnodePath, base.event)

        taskMgr.add(self.updateBullet, "update Bullet")


    def updateBullet(self, task):
        """if task.time >= 1.0 :
            self.bullets[n].removeNode()
            return Task.done"""
        self.setPos(self.getX() + (0.5 * self.direction.getX()), self.getY() + (0.5 * self.direction.getY()), 0 )
        return Task.cont
            
