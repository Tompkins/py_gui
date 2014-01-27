from enthought.traits.api import TraitHandler, HasTraits, Trait

class TraitEvenInteger(TraitHandler):
    def validate(self, object, name, value):
        if type(value) is int and value > 0:
            return value - value % 2
        self.error(object, name, value)

    def info(self):
        return 'a positive even integer'

class B(HasTraits):
    v = Trait(1, TraitEvenInteger())
