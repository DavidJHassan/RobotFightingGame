from math import pi, sin, cos
from random import randint
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import CollisionHandlerEvent
from panda3d.core import CollisionTraverser
from panda3d.core import Mat3
from panda3d.core import Vec3
import sys

from Bullet import Bullet
from Robot import Robot

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        base.cTrav = CollisionTraverser()
        base.event = CollisionHandlerEvent()
        base.event.addInPattern('into')
        base.event.addAgainPattern('again')
        base.event.addOutPattern('out')
        base.event.addInPattern('%fn-into')
        
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)
		
        point = Point3()
        
        #Create robots and assign ids used to access the correct object from collision entry data.
        #TODO: Consider extending ids to all sprites
        self.robots = dict()
        self.id = 0
        for i in range( 10 ):
            point.set(randint(-50, 50), randint(-50, 50), 0)
            self.robots[self.id] = Robot(point, self.id ) 
            self.id += 1


        self.player = self.loader.loadModel("../Models/robotfull")
        self.player.setPos(0,0,0)
        self.player.setScale(4,4,4)
        self.playerDirection = Vec3()
        self.playerDirection.set(0.0,1.0,0.0)

        self.rotationX = 0
        self.rotationY = 0
        self.rotationZ = 0
        self.player.reparentTo(self.render)

        #Sets up a Third Person Camera View#
        self.ThirdPerson = True
        self.cameraDirection = Vec3()
        self.cameraDirection.set(0.0,1.0,0.0)
        self.Zoom = 0
        self.CAMERA_HEIGHT = 12
        self.CAMERA_LENGTH = 25
        self.setCamera()
        ####################################

        #Control Schemes##############################
        self.accept("arrow_up", self.up)
        self.accept("arrow_up-repeat", self.up)

        self.accept("arrow_down", self.down)
        self.accept("arrow_down-repeat", self.down)

        self.accept("arrow_left", self.left)
        self.accept("arrow_left-repeat", self.left)

        self.accept("arrow_right", self.right)
        self.accept("arrow_right-repeat", self.right)

        self.accept("w", self.up)
        self.accept("w-repeat", self.up)

        self.accept("a", self.left)
        self.accept("a-repeat",self.left)

        self.accept("s", self.down)
        self.accept("s-repeat", self.down)

        self.accept("d", self.right)
        self.accept("d-repeat",self.right)

        self.accept("q",self.lookLeft)
        self.accept("q-repeat",self.lookLeft)

        self.accept("e",self.lookRight)
        self.accept("e-repeat",self.lookRight)

        self.accept("page_up", self.lookUp)
        self.accept("page_up-repeat", self.lookUp)

        self.accept("page_down",self.lookDown)
        self.accept("page_down-repeat",self.lookDown)

        self.accept("[",self.tiltLeft)
        self.accept("[-repeat",self.tiltLeft)

        self.accept("]",self.tiltRight)
        self.accept("]-repeat",self.tiltRight)

        self.accept( 'mouse1', self.fire)
        #self.accept( 'mouse1-up', self.setMouseButton)
        self.accept( 'mouse2', self.ResetZoom)
        #self.accept( 'mouse2-up', self.setMouseButton)
        #self.accept( 'mouse3', self.setMouseButton)
        #self.accept( 'mouse3-up', self.setMouseButton)
        self.accept( 'wheel_up', self.ZoomIn)
        self.accept( 'wheel_down', self.ZoomOut)

        self.accept("t",self.TogglePerson)#Allows you to toggle between first and third person view

        self.accept("space", self.fire);
        ###############################################

        self.accept('into', self.collision)
        self.accept('bullet-into', self.bulletCollision )
        self.accept('again', self.collision)
        self.accept('out', self.collision)

        self.bullets = {}

        self.disableMouse()
        
        base.cTrav.showCollisions(self.render)
    
    def collision(self, entry):
        t = 4
        print "collision detected from=" + entry.getFromNodePath().getName()
        #print entry
    
    def bulletCollision(self, entry):
        print "bulletCollision detected"
        try:
            id = int(entry.getIntoNodePath().getName() )
        except ValueError:
            print "in bulletCollision " + entry.getIntoNodePath().getName() + " is not an integer"
            sys.exit(1)
            
        if self.robots[id].damage() <= 0 :
            del self.robots[id]
    
    
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3 )
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def fire(self):
        b = Bullet(self.player.getX(), self.player.getY() + 1, self.player.getZ(), self.playerDirection)
        print b.cnodePath
        base.cTrav.addCollider(b.cnodePath, base.event)
        colliders = base.cTrav.getColliders()
        #print "there are " + str(base.cTrav.getNumColliders() ) + "colliders"
        #for i in colliders:
        #    print i

    def setCamera(self):
        if(self.ThirdPerson):
            self.camera.setPos(self.player.getX() - self.CAMERA_LENGTH * self.cameraDirection.getX(), self.player.getY() - (self.CAMERA_LENGTH * self.cameraDirection.getY())+ self.Zoom, self.player.getZ() + self.CAMERA_HEIGHT)
            self.camera.setHpr( self.rotationX, -20 + self.rotationY, self.rotationZ)
        else:
            self.camera.setPos(self.player.getX(), self.player.getY()+2, self.player.getZ() + self.CAMERA_HEIGHT - 5)#-2 and -4 to adjust into fpv
            self.camera.setHpr( self.rotationX, -20 + self.rotationY ,self.rotationZ)

    def lookLeft(self):
        self.rotationX+= 0.5
        self.lookX()

    def lookRight(self):
        self.rotationX-= 0.5
        self.lookX()

    def lookUp(self):
        self.rotationY+=0.5
        self.setCamera()

    def lookDown(self):
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
        self.player.setH(self.rotationX)
        matrix = Mat3()
        matrix.setRotateMat(self.rotationX)
        self.playerDirection.set(0, 1, 0)
        self.playerDirection = matrix.xform(self.playerDirection)
        
        if self.ThirdPerson == False:
            self.player.setHpr(self.rotationX,0,0)
        else: 
            self.cameraDirection.set(0,1,0)
            self.cameraDirection = matrix.xform(self.cameraDirection)

        self.setCamera()

    def up(self):
        self.player.setPos(self.player.getX() + (1 * self.playerDirection.getX() ), self.player.getY() + (1 * self.playerDirection.getY()), self.player.getZ() )
        self.setCamera()

    def down(self):
        self.player.setPos(self.player.getX() - (1 * self.playerDirection.getX() ), self.player.getY() - (1 * self.playerDirection.getY()), self.player.getZ() )
        self.setCamera()
  
    def rotateVec(self, vector, angle):
        matrix = Mat3()
        matrix.setRotateMat(angle)
        return matrix.xform(vector)
    
    def left(self):
        direction = self.rotateVec(self.playerDirection, 90)
        self.player.setPos(self.player.getX() + (1 * direction.getX() ), self.player.getY() + (1 * direction.getY() ), self.player.getZ() )
        self.setCamera()
  
    def right(self):
        direction = self.rotateVec(self.playerDirection, 90)
        self.player.setPos(self.player.getX() - (1 * direction.getX() ), self.player.getY() - (1 * direction.getY() ), self.player.getZ() )
        self.setCamera()

    def TogglePerson(self):
        if(self.ThirdPerson):
            self.ThirdPerson = False
        else:
            self.ThirdPerson = True
        
        self.setCamera()

    def ZoomIn(self):
        if(self.Zoom < self.CAMERA_LENGTH - 15):
            self.Zoom+=.1
        self.setCamera()

    def ZoomOut(self):
        if(self.Zoom > -(self.CAMERA_LENGTH - 10) ):
            self.Zoom-=.1
        self.setCamera()
    
    def ResetZoom(self):
        self.Zoom = 0


app = MyApp()
app.run()
