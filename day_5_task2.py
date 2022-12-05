#top of stack is end of list
stacks = [
    ['D','L','V','T','M','H','F'],
    ['H','Q','G','J','C','T','N','P'],
    ['R','S','D','M','P','H'],
    ['L','B','V','F'],
    ['N','H','G','L','Q'],
    ['W','B','D','G','R','M','P'],
    ['G','M','N','R','C','H','L','Q'],
    ['C','L','W'],
    ['R','D','L','Q','J','Z','M','T']
    ]


def move_items():
    f = open('day_5.txt', 'r')
    for row in f:
        data = row.strip().split(' ')
        numbers = [int(data[1]), int(data[3])-1, int(data[5])-1]
        removed = []
        for i in range(numbers[0]):
            item = stacks[numbers[1]].pop()
            removed.append(item)
        for i in range(len(removed)):
            item = removed.pop()
            stacks[numbers[2]].append(item)
    for i in range(len(stacks)):
        print(stacks[i][-1], end='') 


if __name__ == '__main__':
    move_items()
