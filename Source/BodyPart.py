from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import NodePath
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode

class BodyPart:

    def __init__(self, position, file, name, parent, scaleX =4, scaleY =4, scaleZ =4):
        
        self.node = loader.loadModel(file)
        self.node.reparentTo(parent)
        self.node.setPos(position)
        self.node.setScale(scaleX, scaleY, scaleZ)
        #self.node.showTightBounds()

