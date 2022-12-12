total = 0 # rotten global variable! 

class Node():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []
        

def print_tree(node, level=0):  
    print("  " * level, node.name, str(node.size))
    for child in node.children:
        print_final_tree(child, level + 1)
        

def traverse(node):
    global total
    if len(node.children) > 0: 
        for child in node.children:            
            node.size += traverse(child)
    if node.size <= 100000:
        total += node.size
    return node.size


def build_tree():
    file_size_total = 0
    f = open('day_7.txt', 'r')
    row=f.readline().strip() #read root line  
    root = Node('/', None) #root
    current_node = root
    eof = False
    while not eof:
        row=f.readline().strip()
        if row == "":
            eof = True
        else:                    
            row_data = row.split(" ")        
            if row == "$ ls": #list
                pass
            elif row_data[1] == "cd":
                if row_data[2] == "/": #go back to root
                    current_node = root
                elif row_data[2] == "..": #go back one level
                    current_node = current_node.parent
                else: # go up one level
                    for child in current_node.children:                        
                        if child.name == row_data[2]:
                            current_node = child
            elif row_data[0] == "dir":
                node = Node(row_data[1], current_node) #add node to tree
                current_node.children.append(node)
            elif row_data[0].isnumeric():
                file_size_total += int(row_data[0])
                current_node.size += int(row_data[0])
    traverse(root)
    print(total)

if __name__ == '__main__':
    build_tree()
