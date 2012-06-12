from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import NodePath
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode

from BodyPart import BodyPart

class Robot(NodePath):
    
    def __init__(self, position, id):
            
        point = Point3()
        point.set(position.getX(), position.getY(), position.getZ() )
        self.body = BodyPart(point,"../Models/body","body",render)
        #base.cTrav.addCollider( self.body.cnodePath, base.event)
        
        leftArmPlace = self.body.node.find("**/arm1")
        if(leftArmPlace.isEmpty()):
            raise Exception("Left arm was not loaded properly")
        rightArmPlace = self.body.node.find("**/arm2")
        if(rightArmPlace.isEmpty()):
            raise Exception("Right arm was not loaded properly")
        headPlace = self.body.node.find("**/head")
        if(headPlace.isEmpty()):
            raise Exception("The head was not loaded properly")
        leftLegPlace = self.body.node.find("**/leg1")
        if(leftLegPlace.isEmpty()):
            raise Exception("Left leg was not loaded properly")
        rightLegPlace = self.body.node.find("**/leg2s")
        if(rightLegPlace.isEmpty()):
            raise Exception("Right leg was not loaded properly")

        self.arms = []
        point.set(0,0,0)
        self.arms.append(BodyPart(point, "../Models/robotarm","leftarm",leftArmPlace) )
        self.arms.append(BodyPart(point,"../Models/robotarm","rightarm",rightArmPlace) )

        self.legs =[]
        self.legs.append(BodyPart(point, "../Models/robotleg","leftleg",leftLegPlace) )
        self.legs.append(BodyPart(point,"../Models/robotleg","rightleg",rightLegPlace) )

        self.head = BodyPart(point,"../Models/robothead","head",headPlace)

        min = Point3()
        max = Point3()
        self.body.node.calcTightBounds(min, max)
        self.size = max - min
        print "size ="
        print self.size
        self.cnode = CollisionNode(str(id))
        self.cnode.addSolid(CollisionSphere(0, 0, 0, self.size.length() /2 ) )
        self.cnodePath = self.body.node.attachNewNode(self.cnode)
        self.cnodePath.show()
        base.cTrav.addCollider( self.cnodePath, base.event)

    def damage(self):
        self.body.node.removeNode()
        return 0






