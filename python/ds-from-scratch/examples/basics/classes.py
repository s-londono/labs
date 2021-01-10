

class CountingClicker:
    """A class can/should have a docstring, just like a function.
       - Class methods that start with underscore are considered private by convention."""

    def __init__(self, count=0):
        """Constructor"""
        self.count = count

    def __repr__(self):
        """Produces a string representation of a class instance"""
        return f"CountingClicker(count={self.count})"

    def click(self, times=1):
        self.count += times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


# Test some use cases using assert
clckr = CountingClicker()
assert clckr.read() == 0, "Clicker should start with count 0"

clckr.click()
clckr.click()
assert clckr.read() == 2, "After two clicks, clicker should have count 2"

clckr.reset()
assert clckr.read() == 0, "After reset, clicker should be back to 0"


class NonResetClicker(CountingClicker):
    """This class inherits from CountClicker"""

    def reset(self):
        """Overrides the reset method inherited from CountClicker"""
        pass
