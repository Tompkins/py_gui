# -*- coding:utf-8 -*-

from enthought.traits.api import HasTraits, CFloat, Float, List, Enum

class Person(HasTraits):
    cweight = CFloat(50.0)
    weight = Float(50.0)

class Items(HasTraits):
    count_list = List([None, 0, 1, 2, 3, "many"])
    count = Enum(values="count_list")

class Items2(HasTraits):
    count = Enum(None, 0, 1, 2, 3, "many")
