# -*- coding:utf-8 -*-
from enthought.traits.api import HasTraits, Str, Int, Instance, Delegate

class Parent(HasTraits):
    # 初始化：last_name初始化为'Zhang'
    last_name = Str('Zhang')

class Child(HasTraits):
    age = Int

    # 验证：father属性的值必须是Parent类的实例
    father = Instance(Parent)

    # 代理：将Child对象的last_name属性代理给其father属性的last_name
    last_name = Delegate('father')

    # 监听：当age属性的值被修改时，下面的函数将被运行
    def _age_changed(self, old, new):
        print "Age changed from %s to %s" % (old, new)
