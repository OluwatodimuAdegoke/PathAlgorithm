from checkedboxes import Checked
#Contains the class that houses nodes to be checked
class Boxes(Checked):

    def remove(self,pos):
        self._length -= 1
        if pos == "last":
            ret = self._box.pop()
            return ret
        else:
            ret = self._box.pop(0)
            return ret
