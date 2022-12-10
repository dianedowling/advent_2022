class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move_history = [(0,0)]


def move_head(head, direction):
    if direction == "U":
        head.y += 1
    elif direction == "D":
        head.y -= 1
    elif direction == "R":
        head.x += 1
    elif direction == "L":
        head.x -= 1
    

def move_tail(head, tail):
    if abs(tail.x - head.x) <= 1 and abs(tail.y - head.y) <= 1:
        # no need to move
        tail.move_history.append((tail.x, tail.y))
    else:
        # need to move
        if head.x - tail.x == 2: # x is right
            tail.x += 1
            if head.y > tail.y: # y is up                
                tail.y += 1
            elif head.y < tail.y: # y is down
                tail.y -= 1            
        elif head.x - tail.x == -2: # x is left
            tail.x -= 1
            if head.y > tail.y: # y is up                
                tail.y += 1
            elif head.y < tail.y: # y is down
                tail.y -= 1 
        elif head.y - tail.y == 2: # y is up
            tail.y += 1
            if head.x > tail.x: # x is right               
                tail.x += 1
            elif head.x < tail.x: # x is left
                tail.x -= 1
        elif head.y - tail.y == -2: # y is down
            tail.y -= 1
            if head.x > tail.x: # x is right               
                tail.x += 1
            elif head.x < tail.x: # x is left
                tail.x -= 1
           
        tail.move_history.append((tail.x, tail.y))            
    

def rope_bridge():
    head = Player()
    tail = Player()
    f = open('day_9.txt', 'r')
    for row in f:
        row = row.strip().split(" ")
        direction = row[0]
        steps = int(row[1])
        for i in range(steps):
            move_head(head, direction)
            move_tail(head, tail)
    unique = set(tail.move_history)
    print(len(unique))  
 

if __name__ == '__main__':
    rope_bridge()
    
    
