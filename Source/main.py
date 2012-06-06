from math import pi, sin, cos
from random import randint
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import CollisionHandlerEvent
from panda3d.core import CollisionTraverser

 
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

        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)
		
        for i in range( 10 ):
            r = Robot(randint(-50, 50), randint(-50, 50), 0)
            print r.cnodePath
            base.cTrav.addCollider( r.cnodePath, base.event)

        self.player = self.loader.loadModel("models/box")
        self.player.setPos(0,0,0)
        self.player.reparentTo(self.render)

        self.CAMERA_HEIGHT = 10
        self.CAMERA_LENGTH = 25
        self.setCamera()
                
        self.bullets = {}
        
        self.accept("arrow_up", self.up)
        self.accept("arrow_up-repeat", self.up)

        self.accept("arrow_down", self.down)
        self.accept("arrow_down-repeat", self.down)

        self.accept("arrow_left", self.left)
        self.accept("arrow_left-repeat", self.left)

        self.accept("arrow_right", self.right)
        self.accept("arrow_right-repeat", self.right)
                        
        self.accept("space", self.fire);
        self.accept('into', self.collision)
        self.accept('again', self.collision)
        self.accept('out', self.collision)
        
        
        self.disableMouse()
        
        base.cTrav.showCollisions(self.render)

        colliders = base.cTrav.getColliders()
        print "there are " + str(base.cTrav.getNumColliders() ) + " colliders"
        for i in colliders:
            print i
        
        patterns = base.event.getInPatterns()
        print "there are " + str( base.event.getNumInPatterns())
        for i in patterns:
            print i
    
    def collision(self, entry):
        print "collision detected"
        print entry

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3 )
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def fire(self):
        b = Bullet(self.player.getX(), self.player.getY() + 1, self.player.getZ())
        print b.cnodePath
        base.cTrav.addCollider(b.cnodePath, base.event)
        colliders = base.cTrav.getColliders()
        #print "there are " + str(base.cTrav.getNumColliders() ) + "colliders"
        #for i in colliders:
        #    print i

    def setCamera(self):
        self.camera.setPos(self.player.getX(), self.player.getY() - self.CAMERA_LENGTH, self.player.getZ() + self.CAMERA_HEIGHT)
        self.camera.setHpr( 0, -20,0)

    def up(self):
        self.player.setPos(self.player.getX(), self.player.getY() + 1, self.player.getZ() )
        self.setCamera()

    def down(self):
        self.player.setPos(self.player.getX(), self.player.getY() - 1, self.player.getZ() )
        self.setCamera()
  
    def left(self):
        self.player.setPos(self.player.getX() - 1, self.player.getY(), self.player.getZ() )
        self.setCamera()
  
    def right(self):
        self.player.setPos(self.player.getX() + 1, self.player.getY(), self.player.getZ() )
        self.setCamera()

app = MyApp()
app.run()
