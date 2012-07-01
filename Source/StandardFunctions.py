from math import *
from panda3d.core import Vec3

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import NodePath
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode

from BodyPart import BodyPart


#calcDistance takes 2 points and returns distance between them
def calcDistance( a, b):
    diff = a - b
    return diff.length()

def calcDistance2D(a, b):
    return calcDistance(a, b)

#caclDirection takes 2 points and returns unit vector representing direction
#from the first point to the second point
def calcDirection( a, b):
    vec = b - a
    if vec.length() == 0:
        return vec
    vec /= vec.length()
    return vec

#Function is only needed to make the code easier to understand
def calcDirection2D( a, b):
    return calcDirection(a, b)


def UnsignedAngleBetweenTwoV3(a, b):
    a = NormalizeV3(a)
    b = NormalizeV3(b)
    Angle = acos(DotV3(a,b))
    return Angle

def radiansToDegrees(x):
    return x*(180/pi)

def degreesToRadians(x):
    return x*(pi/180)


def NormalizeV3(a):
        return scaleV3( 1/sqrt( pow(a.getX(),2) + pow(a.getY(),2) + pow(a.getZ(), 2)) , a)


def DotV3(a,b):
    return a.getX()*b.getX() + a.getY()*b.getY() +  a.getZ() * b.getZ()

def scaleV3(a,v):
    return Vec3( a*v.getX(), a*v.getY(), a*v.getZ())