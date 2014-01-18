# -*- coding: cp936 -*-
from enthought.traits.api import HasTraits, Str, Int
from enthought.traits.ui.api import View, Item

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int

    view = View(
        Item('department', label = u"����", tooltip=u"���ĸ����Ÿɻ�"),
        Item('name', label = u"����"),
        Item('salary', label = u"����"),
        Item('bonus', label = u"����"),
        title = u"Ա������", width=250, height=150, resizable=True
        )

if __name__ == "__main__":
    p = Employee()
    p.configure_traits()
