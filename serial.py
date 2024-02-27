"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """initialized start and current to the starting value. Only current will be modifiable"""
        self.start = start
        self.current = start

    def __repr__(self):
        return f"SerialGenerator start = {self.start}, current = {self.current}"

    def generate(self):
        """prints the current number, then adds 1 to it, giving the sequential number each time"""
        print(self.current)
        self.current += 1

    def reset(self):
        """resets the current number to equal the starting number"""
        self.current = self.start