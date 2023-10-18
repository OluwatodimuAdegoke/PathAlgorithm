import sys

box = []
ans = []
checked = []
start_and_end = []
accepted_values = ['x','o','#',' ']
slength = {"length":0}

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

def main():
    if(check_name()):
        try:

            file = open(sys.argv[1], "r")
            f = file.readlines()

            row = len(f)
            col = 0
            for a in f:
                if len(a)-1 > col:
                    col = len(a) - 1

            maze = [[0 for i in range(col)] for j in range(row)]

            for i in range(0,row):
                for j in range(0,col):
                    try:
                        if f[i][j] in accepted_values:
                            maze[i][j] = f[i][j]
                        else: 
                            raise ValueError
                    except:
                        maze[i][j] = "#"

        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            start, end = get_points(maze)
            print_maze(maze)
            soln = search(maze,start,end)
            get_ans(soln,row,col,maze)
            print("####Solution####")
            print_maze(maze)
            print("Solution Length: ",slength["length"])
            file.close()

def check_name():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".txt"):
            return True
        else:
            sys.exit("Not a txt file")
    else:
        sys.exit("Command line arguments not correct")

#Get Start and End Points
def get_points(maze):
    c = 0
    for i in maze:
        if 'x' in i:
            p = (maze.index(i),i.index('x'))
            start_and_end.append(p)
            end = Node(p)
            c += 1
        if 'o' in i:
            p = (maze.index(i),i.index('o'))
            start_and_end.append(p)
            start = Node(p)
            c += 1

    if c != 2:
        sys.exit("No start or end point")
    else:
        return start, end
    
def search(maze,start,end):

    box.append(start)
    now = start
    while not now == end and len(box) != 0:

        #change this to check the method from BFS to DFS
        now = box.pop()
        slength["length"] += 1
        # print("Box is",box,"now :",now.point)
        checked.append(now.point)

        #have a way to know the parents of each node
        points = now.connected_point(maze)
        for i in points:
            if i in checked or any(node.point == i for node in box):
                    continue
            box.append(Node(i,parent = now,check=True))

        # print("Checked",checked)      
        # print("Box here: ",box,"now: ",now.point)

    if now == end:
        end.check = True
        end.parent = now.parent
        # print("Solved",end.parent.point)
        return end
    else:
        sys.exit("No Solution Found")

def get_ans(end,row,col,maze):
    temp = end.parent
    while temp.check == True:
        ans.append(temp.point)
        temp = temp.parent
    for i in range(0,row):
        for j in range(0,col):
            if (i,j) in checked:
                if (i,j) in ans:
                    maze[i][j] = "█"
                elif (i,j) not in start_and_end:
                    maze[i][j] = "▲"

def print_maze(maze):
    for a in maze:
        for b in a:
            print(b,end="")
        print()



if __name__ == '__main__':
    main()