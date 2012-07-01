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
from CreateEquipment import CreateEquipment
from Equipment import Equipment
class Robot:
    
    def __init__(self, position, id, scale):

        if scale == 0:
            scale = 0.1



        self.equipment = []
        self.equipment.append(CreateEquipment("../models/box","leftshoulder",50,50))

        self.health = scale * 3 

        self.id = id
        point = Point3()
        point.set(position.getX(), position.getY(), position.getZ() + (2.1 * scale))# 2.1 is a very close approximation to the length of the legs. By raising the torso up 2.1, we can then fit the legs underneath.
        self.body = BodyPart(point,"../Models/robotbody","body",render,scale,scale,scale)
        self.body.node.setTag("type", "robot")
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

        tag = []
        pos = []

        self.arms = []
        point.set(0,0,0)
        self.arms.append(BodyPart(point, "../Models/robotarm","leftarm",leftArmPlace) )
        self.arms.append(BodyPart(point,"../Models/robotarm","rightarm",rightArmPlace) )
        tag.append(leftArmPlace)
        tag.append(rightArmPlace)
        pos.append(self.arms[0].node.getRelativePoint(tag[0], point ))
        pos.append(self.arms[1].node.getRelativePoint(tag[1], point ))
        self.arms[0].node.setPos(-pos[0].getX(), -pos[0].getY(), -pos[0].getZ())
        self.arms[1].node.setPos(-pos[1].getX(), -pos[1].getY(), -pos[1].getZ())

        self.legs =[]
        self.legs.append(BodyPart(point, "../Models/robotleg","leftleg",leftLegPlace) )
        self.legs.append(BodyPart(point,"../Models/robotleg","rightleg",rightLegPlace) )
        tag.append(leftLegPlace)
        tag.append(rightLegPlace)
        pos.append(self.legs[0].node.getRelativePoint(tag[2], point ))
        pos.append(self.legs[1].node.getRelativePoint(tag[3], point ))
        self.legs[0].node.setPos(-pos[2].getX(), -pos[2].getY(), -pos[2].getZ())
        self.legs[1].node.setPos(-pos[3].getX(), -pos[3].getY(), -pos[3].getZ())


        self.head = BodyPart(point,"../Models/robothead","head",headPlace)
        tag.append(headPlace)
        pos.append(self.head.node.getRelativePoint(tag[4], point ))
        self.head.node.setPos(-pos[4].getX(), -pos[4].getY(), -pos[4].getZ())


        min = Point3()
        max = Point3()
        self.body.node.calcTightBounds(min, max)
        self.size = max - min
        print "size ="
        print self.size
        self.cnode = CollisionNode(str(id))
        self.cnode.addSolid(CollisionSphere(0, 0, 0, self.size.length() /(2 * scale) ) )
        self.cnodePath = self.body.node.attachNewNode(self.cnode)
        self.cnodePath.show()
        base.cTrav.addCollider( self.cnodePath, base.event)

    def damage(self):
        self.health -= 1
        
        if self.health <= 0:
            self.body.node.setTag("type", "destroyed")

            for i in self.equipment:
                if(i.getModel().isEmpty()):
                    raise Exception("Model not found in damage")
                i.getModel().setPos(self.body.node.getX(),self.body.node.getY(),0)
                i.getModel().reparentTo(render)
               # i.getModel().setScale(scaleX, scaleY, scaleZ)

            self.body.node.removeNode()


        return self.health






