SIZE = 99

def build_array(forest):
    f = open('day_8.txt', 'r')
    for line in f:
        row = []
        line = line.strip()
        for tree in line:
            row.append(tree)
        forest.append(row)


def check_visibility(forest):
    max_score = 0     
    for row in range(0, SIZE):
        for col in range(0, SIZE):
            tree = forest[row][col]
            #check left
            tallest = True
            i = col - 1
            left_count = 0
            while tallest and i >= 0:
                left_count += 1
                if forest[row][i] < tree:
                    i -= 1
                else:
                    tallest = False
                    
            #check right
            tallest = True
            i = col + 1
            right_count = 0
            while tallest and i < SIZE:
                right_count += 1
                if forest[row][i] < tree:
                    i += 1
                else:
                    tallest = False
            
            #check above
            tallest = True
            i = row - 1
            up_count = 0
            while tallest and i >= 0:
                up_count += 1
                if forest[i][col] < tree:
                    i -= 1
                else:
                    tallest = False
            
            #check below
            tallest = True
            i = row + 1
            down_count = 0
            while tallest and i < SIZE:
                down_count += 1
                if forest[i][col] < tree:
                    i += 1
                else:
                    tallest = False

            #calculate score
            score = left_count * right_count * up_count * down_count
            if score > max_score:
                max_score = score
                
    print(max_score)
        
 
if __name__ == '__main__':
    forest = []
    build_array(forest)
    check_visibility(forest)
    
    
