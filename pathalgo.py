import sys
import copy
from node import Node


box = []
checked = []
start_and_end = []
accepted_values = ['x','o','#',' ']
slength = {"length":0}


def main():
    if(check_name()):
        try:

            file = open(sys.argv[1], "r")
            f = file.readlines()

            #Get the number of columns and rows
            row = len(f)
            col = 0
            for a in f:
                if len(a)-1 > col:
                    col = len(a) - 1

            #Initialize the maze
            maze = format_maze(f, row, col)

        except FileNotFoundError:
            sys.exit("File does not exist")

        else:

            get_points(maze)
            oldmaze = copy.deepcopy(maze)
            soln = search(maze,start_and_end[0],start_and_end[1])
            get_ans(soln,row,col,maze)
            print_maze(oldmaze,maze,col)
            print("Solution Length: ",slength["length"])

            file.close()

def format_maze(f, row, col):
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
    return maze

def check_name():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".txt") and (sys.argv[2] == "DFS" or sys.argv[2] == "BFS"):
            return True
        else:
            sys.exit("Not a txt file")
    else:
        sys.exit("Command line arguments not correct: (pathalgo.py) (maze file) (DFS or BFS)")

#Get Start and End Points
def get_points(maze):
    c = 0
    for i in maze:
        if 'x' in i:
            a = (maze.index(i),i.index('x'))
            end = Node(a)
            c += 1
        if 'o' in i:
            b = (maze.index(i),i.index('o'))
            start = Node(b)
            c += 1

    if c != 2:
        sys.exit("Start and End point must be one")
    else:
        start_and_end.append(start)
        start_and_end.append(end)

#Search for the end node
def search(maze,start,end):

    box.append(start)
    now = start
    while not now == end and len(box) != 0:

        #change this to check the method from BFS to DFS
        if(sys.argv[2] == "DFS" ):
            now = box.pop()
        else:
            now = box.pop(0)

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

#Get the points in the solution
def get_ans(end,row,col,maze):
    temp = end.parent
    ans = []
    while temp.check == True:
        ans.append(temp.point)
        temp = temp.parent
    for i in range(0,row):
        for j in range(0,col):
            if (i,j) in checked:
                if (i,j) in ans:
                    maze[i][j] = "█"
                elif not any( node.point == (i,j)  for node in start_and_end):
                    maze[i][j] = "▲"

def print_maze(oldmaze, maze ,col):
    print()
    sp = max(0,col-6)
    print("-"*sp,f"{sys.argv[2]} Solution","-"*sp)
    for i,j in zip(oldmaze,maze):
        for a in i:
            print(a,end="")
        print("  ",end="")
        for b in j:
            print(b,end="")
        print()



if __name__ == '__main__':
    main()