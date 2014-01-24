# -*- coding:utf-8 -*-
from enthought.traits.api import *

class Point(HasTraits):
    x = Int
    y = Int

class Circle(HasTraits):
    center = Instance(Point)
    x = DelegatesTo('center')
    y = PrototypedFrom('center')
    r = Int

p = Point()
c = Circle()
c.center = p
