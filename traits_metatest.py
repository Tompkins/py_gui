# -*- coding:utf-8 -*-
from enthought.traits.api import HasTraits, Int, Str, Array, List

class MetadataTest(HasTraits):
    i = Int(99, myinfo="test my info")
    s = Str("test", label=u"字符串")
    # NumPy的数组
    a = Array
    # 元素为Int的列表
    list = List(Int)

test = MetadataTest()
