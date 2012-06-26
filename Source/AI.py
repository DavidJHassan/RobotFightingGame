from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import Point2
from panda3d.core import NodePath
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode
from random import randint

from BodyPart import BodyPart
from Bullet import Bullet
from Robot import Robot
from StandardFunctions import *

class AI(Robot):
    
    def __init__(self, position, id, scale):
        Robot.__init__(self,position,id,scale)
            
        self.type = randint(0,1)
        
        if self.type == 0:
            taskMgr.add( self.randomWalk, 'walk')
            self.destination = Point2()
            self.setRandomPoint( self.destination )
        else:
            taskMgr.add( self.hunt, 'hunt')
            self.target = None
                
        self.time = 0
        self.bulletTime = 0

    def setRandomPoint(self, point):
        point.setX( randint(-50, 50) )
        point.setY(randint(-50, 50) )

    def randomWalk( self, task ):
        if self.body.node == None or self.body.node.isEmpty():
            return Task.done

        
        if task.time - self.time <= 0.1:
            return Task.cont
        self.time = task.time
                    
            
        if calcDistance2D(self.destination, self.body.node.getPos().getXy() ) <= 1:
            self.setRandomPoint( self.destination )

        direction = calcDirection2D(self.body.node.getPos().getXy(), self.destination )
        #print "randomWalk destination ="
        #print direction

        self.body.node.setX( self.body.node.getX() + direction.getX() )
        self.body.node.setY( self.body.node.getY() + direction.getY() )
        return Task.cont

    def hunt( self, task ):
        if self.body.node.isEmpty():
            return Task.done

        
        if self.target == None or self.target.isEmpty() or self.target.getTag("type") == "destroyed":
            list = render.findAllMatches("**/=type=robot")
            print "list size = " + str(list.size())
            if list.size() < 2:
                return Task.cont

            target = randint(0, list.size() - 1 )
            self.target = list.getPath( target )
            if self.target == self.body.node:
                return Task.cont

        if task.time - self.time <= 0.1:
            return Task.cont
        self.time = task.time
        
        if calcDistance2D( self.target.getPos().getXy(), self.body.node.getPos().getXy() ) < 1:
            if task.time - self.bulletTime >= 5:
                Bullet(self.body.node.getX(), self.body.node.getY(), self.body.node.getZ(), calcDirection( self.body.node.getPos(), self.target.getPos() ), self.id)
                self.bulletTime = task.time
        else:
            direction = calcDirection2D(self.body.node.getPos().getXy(), self.target.getPos().getXy() )
           # print "in hunt direction="
          #  print direction
            self.body.node.setX( self.body.node.getX() + direction.getX() )
            self.body.node.setY( self.body.node.getY() + direction.getY() )

        return Task.cont





