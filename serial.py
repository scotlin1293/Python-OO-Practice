"""Python serial number generator."""

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

class SerialGenerator:
  
    def __init__(self, start=0):
        """create generator with default start 0
        """
        self.start = self.next = start
    
    def __repr__(self):
        """create representation of serial
        """
        return f"<SerialGenerator start ={self.start} next={self.next}>"

    def generate(self):
        """generate next number to return"""
        self.next = self.next + 1
        return self.next - 1

    def reset(self):
        """set self.next back to the chosen start point"""
        self.next = self.start

  
serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())