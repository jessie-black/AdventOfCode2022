class File():
    def __init__(self,name,size):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size

    def getName(self):
        return self.name

    def isDir(self):
        return False

class Dir():
    def __init__(self, name,parent):
        self.name = name
        self.parent = parent
        self.size = 0 #initially added directories have no known size
        self.children = [] # list of files or directories

    def getParent(self):
        return self.parent

    def getName(self):
        return self.name

    def getChild(self, target):
        for child in self.children:
            if child.getName() == target: return child
        print("Error: Couldn't find directory named",target)
        return None

    def addDir(self,newDir): # add a new empty subdirectory
        self.children.append(newDir)

    def addFile(self,newFile): # add a new file in to current  directory
        self.children.append(newFile)

    def getSize(self):
        return self.size

    def calculateSize(self): #sum sizes of children and update size to reflect value
        for item in self.children:
            if item.isDir():
                self.size += item.calculateSize()
            else: self.size += item.getSize()
        return self.size

    def isDir(self):
        return True

    def listAllChildren(self):
        for child in self.children:
            print(child.getName(),child.getSize(),"(directory)" if child.isDir() else "(file)")

    def findSmallDirectories(self):
        total=0
        for item in self.children:
            if item.isDir():
                if item.getSize()<=100000:
                    total+=item.getSize()
                total+=item.findSmallDirectories()
        return total

    def matchSize(self,target_size):
        best = 7000000
        for child in self.children:
            if child.isDir():
                size = child.getSize()
                if size>=target_size and size <= best:
                    best = size
                child_size=child.matchSize(target_size)
                if child_size>=target_size and child_size <= best:
                    best = child_size
        return best

def cd(line,current_directory):
    target = line[5:].strip()  # get destination directory (or command)
    if target == "..":
        target_directory = current_directory.getParent()
    else:
        target_directory = current_directory.getChild(target)
    return target_directory

def ls(source,index,line,current_directory):
    i=index+1
    limit = len(source)
    line = source[i] #look at following line
    while line[0]!="$": #until new command found or end of file reached
        line = line.strip()
        if line[0:3]=="dir":
            name = line[4:]
            new_directory = Dir(name,parent=current_directory)
            current_directory.addDir(new_directory)
        else:
            line = line.split()
            size=int(line[0])
            name=line[1]
            new_file = File(name,size) #create new file of name line[1] and size line[0]
            current_directory.addFile(new_file)
        if i == limit - 1: break # avoid index out of bounds issue
        i+=1
        line=source[i]
    return i

def parse_command(source,index,line,current_directory):
    if "cd" in line:
        return index+1, cd(line, current_directory)
    else:
        return ls(source,index,line,current_directory),current_directory

def main():
    root = Dir("root",None) # create root directory (with no parent)
    current_directory = root #point to root directory

    #Read input file
    file_path = 'day7_input.txt'  # terminal output
    with open(file_path) as input_file:
        all_output = input_file.readlines()  # read all terminal output
        all_output = all_output[1:]  # skip first line -- simply sets to root directory; redundant.

    #Model file system based on input
    for i in range(len(all_output)):  # parse rest of commands.
        line = all_output[i]  # get current line
        if line[0]=="$":
            line,current_directory = parse_command(all_output,i,line,current_directory)

    # Okay, time to figure out the solution to part 1...
    total_space_used = root.calculateSize() #get sizes for all directories, recursively.
    print(root.findSmallDirectories()) #print the total sum of all directories of size 100,000 or less

    # Part 2
    print(total_space_used)
    currently_free = 70000000 - total_space_used
    need_to_free = 30000000 - currently_free
    print("Space we need to free:",need_to_free)
    print(root.matchSize(need_to_free))


if __name__ == "__main__":
    main()