from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import NodePath
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode

class Equipment:
    def __init__(self):

        self.model = None
        self.tag = None

        self.isOffense = False
        self.isDefense = False
        self.isHealth = False
        self.isShield = False
        self.isStamina = False
        self.isSpeed = False

        self.health = 0.0
        self.shield = 0.0
        self.speed = 0.0
        self.stamina = 0.0
        self.offense = 0.0
        self.defense = 0.0

    def isHealth(self):
        return self.isHealth


    def isShield(self):
        return self.isShield


    def isStamina(self):
        return self.isStamina

    def isSpeed(self):
        return self.isSpeed


    def isOffense(self):
        return self.isOffense


    def isDefense(self):
        return self.isDefense


    def getHeath(self):
        return self.health

    def getShield(self):
        return self.shield

    def getSpeed(self):
        return self.speed


    def getStamina(self):
        return self.stamina


    def getOffense(self):
        return self.offense


    def getDefense(self):
        return self.defense

    def getModel(self):
        if(self.model.isEmpty()):
            raise Exception("Model not found")
        return self.model

    def getTag(self):
        return self.getTag
