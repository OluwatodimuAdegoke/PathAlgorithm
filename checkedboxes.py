#Contains the class that houses the nodes that has been checked
class Checked:

    def __init__(self):
        self._box = []
        self._length = 0

    @property
    def length(self):
        return self._length
    
    @property
    def box(self):
        return self._box
    
    def add(self,new):
        self._length += 1
        self._box.append(new)
    