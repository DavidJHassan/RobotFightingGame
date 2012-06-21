from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import Mat3
from panda3d.core import Vec3
from panda3d.core import NodePath
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode

from BodyPart import BodyPart
from Robot import Robot
from Bullet import Bullet

class Player(Robot):
    
    def __init__(self, position, id, scale):
        Robot.__init__(self,position,id,scale)

        
        self.rotationX = 0
        self.rotationY = 0
        self.rotationZ = 0
        
        self.playerDirection = Vec3()
        self.playerDirection.set(0.0,1.0,0.0)
        self.scale = scale
        
        #Sets up a Third Person Camera View#
        self.ThirdPerson = True
        self.cameraDirection = Vec3()
        self.cameraDirection.set(0.0,1.0,0.0)
        self.fpvec = Vec3() #Used to set the correct camera location for First Person View
        self.fpvec.set(0,2.0, 0)
        self.CAMERA_HEIGHT = 12*self.scale
        self.CAMERA_LENGTH = 25*self.scale
        self.setCamera()
        ####################################
        
        #Control Schemes##############################
        base.accept("arrow_up", self.up)
        base.accept("arrow_up-repeat", self.up)
        
        base.accept("arrow_down", self.down)
        base.accept("arrow_down-repeat", self.down)
        
        base.accept("arrow_left", self.left)
        base.accept("arrow_left-repeat", self.left)
        
        base.accept("arrow_right", self.right)
        base.accept("arrow_right-repeat", self.right)
        
        base.accept("w", self.up)
        base.accept("w-repeat", self.up)
        
        base.accept("a", self.left)
        base.accept("a-repeat",self.left)
        
        base.accept("s", self.down)
        base.accept("s-repeat", self.down)
        
        base.accept("d", self.right)
        base.accept("d-repeat",self.right)
        
        base.accept("q",self.lookLeft)
        base.accept("q-repeat",self.lookLeft)
        
        base.accept("e",self.lookRight)
        base.accept("e-repeat",self.lookRight)
        
        base.accept("page_up", self.lookUp)
        base.accept("page_up-repeat", self.lookUp)
        
        base.accept("page_down",self.lookDown)
        base.accept("page_down-repeat",self.lookDown)
        
        base.accept("[",self.tiltLeft)
        base.accept("[-repeat",self.tiltLeft)
        
        base.accept("]",self.tiltRight)
        base.accept("]-repeat",self.tiltRight)
        
        base.accept( 'mouse1', self.fire)
        #base.accept( 'mouse1-up', self.setMouseButton)
        base.accept( 'mouse2', self.ResetZoom)
        #base.accept( 'mouse2-up', self.setMouseButton)
        #base.accept( 'mouse3', self.setMouseButton)
        #base.accept( 'mouse3-up', self.setMouseButton)
        base.accept( 'wheel_up', self.ZoomIn)
        base.accept( 'wheel_down', self.ZoomOut)
        
        base.accept("t",self.TogglePerson)#Allows you to toggle between first and third person view
        
        base.accept("space", self.fire);
        ###############################################
    
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        base.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3 )
        base.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
    
    def fire(self):
        Bullet(self.body.node.getX(), self.body.node.getY(), self.body.node.getZ(), self.playerDirection, -1)
    
    def setCamera(self):
        if(self.ThirdPerson):
            base.camera.setPos(self.body.node.getX() - (self.CAMERA_LENGTH * self.cameraDirection.getX()), self.body.node.getY() - ( self.CAMERA_LENGTH  * self.cameraDirection.getY()), self.body.node.getZ() + self.CAMERA_HEIGHT)
            base.camera.setHpr( self.rotationX, -20 + self.rotationY, self.rotationZ)
        else:
            base.camera.setPos(self.body.node.getX() + self.fpvec.getX(), self.body.node.getY() + self.fpvec.getY(), self.body.node.getZ() + self.CAMERA_HEIGHT - 3*self.scale)
            base.camera.setHpr( self.rotationX, -20 + self.rotationY ,self.rotationZ)
    
    def lookLeft(self):
        self.rotationX+= 0.5
        self.lookX()
    
    def lookRight(self):
        self.rotationX-= 0.5
        self.lookX()
    
    def lookUp(self):
        if(self.ThirdPerson):
            if(self.CAMERA_LENGTH >= 0 and self.CAMERA_HEIGHT >= -10*self.scale):
                self.rotationY+=0.5
                self.CAMERA_LENGTH -= 0.1 *self.scale
                self.CAMERA_HEIGHT -= 0.15*self.scale
        else:
            if(self.rotationY <=90):
                self.rotationY+=0.5
        self.setCamera()
    
    def lookDown(self):
        
        if(self.ThirdPerson):
            if(self.CAMERA_LENGTH <=26.5*self.scale and self.CAMERA_HEIGHT <=13.5*self.scale):
                self.rotationY-=0.5
                self.CAMERA_LENGTH += 0.1 *self.scale
                self.CAMERA_HEIGHT += 0.15*self.scale
        else:
            if(self.rotationY >= -65):
                self.rotationY-=0.5
        self.setCamera()
    
    def tiltLeft(self):
        if(self.rotationZ != -12.5):
            self.rotationZ-=0.5
        self.setCamera()
    
    def tiltRight(self):
        if(self.rotationZ != 12.5):
            self.rotationZ+=0.5
        self.setCamera()
    
    def lookX(self):
        self.body.node.setH(self.rotationX)
        matrix = Mat3()
        matrix.setRotateMat(self.rotationX)
        self.playerDirection.set(0, 1, 0)
        self.playerDirection = matrix.xform(self.playerDirection)
        
        if self.ThirdPerson == False:
            self.body.node.setHpr(self.rotationX,0,0)
            self.fpvec.set(0,2,0)
            self.fpvec = matrix.xform(self.fpvec)
        
        else:
            self.cameraDirection.set(0,1,0)
            self.cameraDirection = matrix.xform(self.cameraDirection)
        
        self.setCamera()
    
    def up(self):
        self.body.node.setPos(self.body.node.getX() + (1 * self.playerDirection.getX() ), self.body.node.getY() + (1 * self.playerDirection.getY()), self.body.node.getZ() )
        self.setCamera()
    
    def down(self):
        self.body.node.setPos(self.body.node.getX() - (1 * self.playerDirection.getX() ), self.body.node.getY() - (1 * self.playerDirection.getY()), self.body.node.getZ() )
        self.setCamera()
    
    def rotateVec(self, vector, angle):
        matrix = Mat3()
        matrix.setRotateMat(angle)
        return matrix.xform(vector)
    
    def left(self):
        direction = self.rotateVec(self.playerDirection, 90)
        self.body.node.setPos(self.body.node.getX() + (1 * direction.getX() ), self.body.node.getY() + (1 * direction.getY() ), self.body.node.getZ() )
        self.setCamera()
    
    def right(self):
        direction = self.rotateVec(self.playerDirection, 90)
        self.body.node.setPos(self.body.node.getX() - (1 * direction.getX() ), self.body.node.getY() - (1 * direction.getY() ), self.body.node.getZ() )
        self.setCamera()
    
    def TogglePerson(self):
        self.rotationY = 0
        self.ResetZoom()
        self.CAMERA_HEIGHT = 12*self.scale
        self.CAMERA_LENGTH = 25*self.scale
        
        if(self.ThirdPerson):
            self.ThirdPerson = False
        else:
            self.ThirdPerson = True
            self.lookX()
        
        self.setCamera()
    
    def ZoomIn(self):
        self.CAMERA_LENGTH -=  0.1
        self.setCamera()
    
    def ZoomOut(self):
        self.CAMERA_LENGTH +=  0.1
        self.setCamera()
    
    def ResetZoom(self):
        self.CAMERA_LENGTH = 25*self.scale

