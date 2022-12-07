class File():
    def __init__(self,name,size):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size

    def getName(self):
        return self.name

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
            self.size += item.getSize()


def cd(line,current_directory):
    target = line[5:].strip()  # get destination directory (or command)
    if target == "..":
        print("move up")
        current_directory = current_directory.getParent()
    else:
        print("move to",target)
        current_directory = current_directory.getChild(target)
    #print("Current directory:",current_directory.getName())

def ls(source,index,line,current_directory):
    i=index+1
    limit = len(source)
    line = source[i] #look at following line
    while line[0]!="$": #until new command found or end of file reached
        line = line.strip()
        if line[0:3]=="dir":
            name = line[4:]
            print("Adding directory",name)
            new_directory = Dir(name,parent=current_directory)
            current_directory.addDir(new_directory)
        else:
            line = line.split()
            size=line[0]
            name=line[1]
            new_file = File(name,size) #create new file of name line[1] and size line[0]
            current_directory.addFile(new_file)
            print("Adding new file called",new_file.getName(),"of size",new_file.getSize())
        if i == limit - 1: break # avoid index out of bounds issue
        i+=1
        line=source[i]
    return i

def parse_command(source,index,line,current_directory):
    if "cd" in line:
        cd(line,current_directory)
        return index+1
    elif "ls" in line:
        return ls(source,index,line,current_directory)
    else:
        print("Error - command neither cd nor ls")

def main():
    root = Dir("root",None) # create root directory        ## <-- NOT SURE IF NEED TO ADJUST
    current_directory = root

    file_path = 'day7_input.txt'  # terminal output
    with open(file_path) as input_file:
        all_output = input_file.readlines()  # read all terminal output
        all_output = all_output[1:]  # skip first line -- simply sets to root directory; redundant.

    for i in range(len(all_output)):  # parse rest of commands.
        line = all_output[i]  # get current line
        if line[0]=="$":
            line = parse_command(all_output,i,line,current_directory)
        elif line[0:4] == "$ ls":
            nextindex = i + 1
            while (all_output[nextindex][0] != "$"):  # until the next command
                line = all_output[nextindex]  # add contents
                if line[0:3] == "dir":
                    print("I found a directory called", line[4:].strip())
                else:
                    line = line.split()
                    filesize = line[0]
                    filename = line[1].strip()
                    print("I found a file called", filename, "of size", filesize)
                    #file_system[current_filepath][filename] = filesize
                nextindex += 1


if __name__ == "__main__":
    main()