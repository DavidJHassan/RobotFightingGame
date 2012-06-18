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
from pandac.PandaModules import Texture, TextureStage, DirectionalLight, AmbientLight, TexGenAttrib, VBase4
import sys

from Bullet import Bullet
from Robot import Robot
from AI import AI
from Player import Player
#from SkySphere import SkySphere
    
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

        self.skybox = loader.loadModel("../Models/skybox.egg")
        self.skybox.setPos(-8,42,0)
        self.skybox.setScale(1000)
        self.skybox.reparentTo(render)

        point = Point3()
        
        #Create robots and assign ids used to access the correct object from collision entry data.
        #TODO: Consider extending ids to all sprites
        self.robots = dict()
        self.id = 0
        for i in range( 10 ):
            point.set(randint(-50, 50), randint(-50, 50), 0)
            self.robots[self.id] = AI(point, self.id, randint(1,10) / 5 ) 
            self.id += 1

        point = Point3()
        point.set(0,0,0)
        self.player = Player(point, self.id, 1)
        self.robots[self.id] = self.player
        self.id += 1

        self.accept('into', self.collision)
        self.accept('bullet-into', self.bulletCollision )
        self.accept('again', self.collision)
        self.accept('out', self.collision)

        self.disableMouse()
        
        base.cTrav.showCollisions(self.render)
    
    def collision(self, entry):
        t = 4
        #print "collision detected from=" + entry.getFromNodePath().getName()
        #print entry
    
    def bulletCollision(self, entry):
        #print "bulletCollision detected"
        try:
            id = int(entry.getIntoNodePath().getName() )
            bulletID = int( entry.getFromNodePath().getTag("id") )
        except ValueError:
            #print "in bulletCollision " + entry.getIntoNodePath().getName() + " is not an integer"
            #print "or bullet id tag is not an int"
            return 
        
        
        if bulletID == id:
            return
        
        entry.getFromNodePath().removeNode()
            
        try:
            if self.robots[id].damage() <= 0 :
                del self.robots[id]
            point = Point3()
            point.set(randint(-50, 50), randint(-50, 50), 0)
            self.robots[self.id] = AI(point, self.id, randint(1,10) / 5 ) 
            self.id += 1

        except KeyError:
            #TODO: figure out why keyerror is being called
            return
    

app = MyApp()
app.run()
