from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import NodePath
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode

class BodyPart:

    def __init__(self, position, file, name, parent, scaleX =1, scaleY =1, scaleZ =1):
        
        self.node = loader.loadModel(file)
        self.node.reparentTo(parent)
        self.node.setPos(position)
        self.node.setScale( scaleX, scaleY, scaleZ)

        min = Point3()
        max = Point3()
        self.node.calcTightBounds(min, max)
        self.size = max - min
        maximum = -1
        for i in self.size:
            if i > maximum:
                maximum = i


        self.cnode = CollisionNode('cs' + name)
        self.cnode.addSolid(CollisionSphere(0,0,0,maximum + 0.3))
        self.cnodePath = self.node.attachNewNode(self.cnode)
        self.node.showTightBounds()