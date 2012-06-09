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
    
    def __init__(self, position):
            
        point = Point3()
        point.set(0,0,5)
        self.body = BodyPart(point,"../Models/robotbody","body",render,.5,.5,.5)
        #base.cTrav.addCollider( self.body.cnodePath, base.event)
        
        leftArmPlace = self.body.node.find("**/leftarm")
        if(leftArmPlace.isEmpty()):
            raise Exception("Left arm was not loaded properly")
        rightArmPlace = self.body.node.find("**/rightarm")
        if(rightArmPlace.isEmpty()):
            raise Exception("Right arm was not loaded properly")
        headPlace = self.body.node.find("**/head")
        if(headPlace.isEmpty()):
            raise Exception("The head was not loaded properly")
        leftLegPlace = self.body.node.find("**/leftleg")
        if(leftLegPlace.isEmpty()):
            raise Exception("Left leg was not loaded properly")
        rightLegPlace = self.body.node.find("**/rightleg")
        if(rightLegPlace.isEmpty()):
            raise Exception("Right leg was not loaded properly")



        #point.set(0,0,self.body.size[2])
        #self.head = BodyPart(point, "../Models/robothead","head",self.body.node)
        #base.cTrav.addCollider( self.head.cnodePath, base.event)

        self.arms = []
        point.set(0,0,0)
        self.arms.append(BodyPart(point, "../Models/robotarm","leftarm",leftArmPlace))
        self.arms.append(BodyPart(point,"../Models/robotarm","rightarm",rightArmPlace))

        self.legs =[]
        self.legs.append(BodyPart(point, "../Models/robotleg","leftleg",leftLegPlace))
        self.legs.append(BodyPart(point,"../Models/robotleg","rightleg",rightLegPlace))

        self.head = []
        self.head.append(BodyPart(point,"../Models/robothead","head",headPlace))
        #point.set(-self.body.size[0] / 2,0,0)
        #self.arms.append(BodyPart(point, "../Models/robotarm","arm",self.body.node ) )
        #base.cTrav.addCollider( self.arms[0].cnodePath, base.event)
        #base.cTrav.addCollider( self.arms[1].cnodePath, base.event)

        """self.legs = []
        point.set(-self.body.size[0] / 2, 0, -self.body.size[2] /2)
        self.legs.append(BodyPart(point, "../Models/robotleg","leg",self.body.node ) )
        point.set(-self.body.size[0] / 2, 0, -self.body.size[2] /2)
        self.legs.append(BodyPart(point, "../Models/robotleg","leg",self.body.node ) )
        #base.cTrav.addCollider( self.legs[0].cnodePath, base.event)
        #base.cTrav.addCollider( self.legs[1].cnodePath, base.event)"""
