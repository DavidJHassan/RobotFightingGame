from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import NodePath
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode

from Equipment import Equipment

class CreateEquipment(Equipment):
    def __init__(self,modelPath,tag,health, offense):
        Equipment.__init__(self)

        self.model = loader.loadModel(modelPath)
        self.tag = tag
        self.health = health
        self.offense = offense

        if self.health != 0:
            self.isHealth = True

        if self.offense != 0:
            self.isOffense = True


