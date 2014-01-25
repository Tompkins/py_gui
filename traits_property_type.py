from enthought.traits.api import TraitType, HasTraits, Float

class ScaledValue(TraitType):
    def init(self):
        self.value = 0

    def get(self, object, name):
        print "get %s.%s" % (object, name)
        return self.value * object.scale

    def set(self, object, name):
        print "set %s.%s = %s" % (object, name, value)
        self.value = value

class A(HasTraits):
    scale = Float(1.0)
    t1 = ScaledValue
