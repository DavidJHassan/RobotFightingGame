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
        self.body = BodyPart(point, "../Models/robotbody","body",render,0.5,0.5,0.5)
        #base.cTrav.addCollider( self.body.cnodePath, base.event)
        
        place = self.body.node.find("**/leftarm")
        print place
        #point.set(0,0,self.body.size[2])
        #self.head = BodyPart(point, "../Models/robothead","head",self.body.node)
        #base.cTrav.addCollider( self.head.cnodePath, base.event)

        self.arms = []
        point.set(0,0,0)
        self.arms.append(BodyPart(point, "../Models/robotarm","arm",place) )
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
