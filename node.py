

class Node():
    def __init__(self,point,parent = None,check = False):
        self.point = point
        self.parent = parent
        self.check = check

    def __eq__(self,other):
        if self.point == other.point:
            return True
        else:
            return False
    def check_parent(self):
        if self.parent == None:
            return False
        else:
            return True
        
    def connected_point(self,maze):
        points = []
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for a in directions:
            x = a[0]+self.point[0]
            y = a[1]+self.point[1]
            try:
                if maze[x][y] == 'x':
                    return [(x,y)]
                elif maze[x][y] == ' ':
                    points.append((x,y))
                else:
                    continue
            except:
                continue
        return points
