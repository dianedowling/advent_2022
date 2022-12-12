ROUNDS = 10000

class Monkey():
    def __init__(self, num, items, operation, divisor, if_true, if_false):
        self.num = num
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0

    def has_items(self):
        return len(self.items) > 0

    def inspect_and_throw(self, worry_factor):
        self.inspections += 1
        item = self.items.pop(0)
        if self.operation[0] == "+":
            worry_level = item + self.operation[1]
        elif self.operation[0] == "*":
            worry_level = item * self.operation[1]
        elif self.operation[0] == "**":
            worry_level = item * item
        new_worry_level = worry_level % worry_factor
        if new_worry_level % self.divisor == 0:
            return (self.if_true, new_worry_level)
        else:
            return (self.if_false, new_worry_level)

    def catch(self, item):
        self.items.append(item)
        
        

def create_monkeys(monkeys):    
    num = 0 # monkey 0
    items = [73,77]
    operation = ('*',5)
    divisor = 11
    if_true = 6
    if_false = 5
    monkey = Monkey(num, items, operation, divisor, if_true, if_false)
    monkeys.append(monkey)
    num = 1 # monkey 1
    items = [57, 88, 80]
    operation = ('+',5)
    divisor = 19
    if_true = 6
    if_false = 0
    monkey = Monkey(num, items, operation, divisor, if_true, if_false)
    monkeys.append(monkey)
    num = 2 # monkey 2
    items = [61, 81, 84, 69, 77, 88]
    operation = ('*',19)
    divisor = 5
    if_true = 3
    if_false = 1
    monkey = Monkey(num, items, operation, divisor, if_true, if_false)
    monkeys.append(monkey)
    num = 3 # monkey 3
    items = [78, 89, 71, 60, 81, 84, 87, 75]
    operation = ('+',7)
    divisor = 3
    if_true = 1
    if_false = 0
    monkey = Monkey(num, items, operation, divisor, if_true, if_false)
    monkeys.append(monkey)
    num = 4 # monkey 4
    items = [60, 76, 90, 63, 86, 87, 89]
    operation = ('+',2)
    divisor = 13
    if_true = 2
    if_false = 7
    monkey = Monkey(num, items, operation, divisor, if_true, if_false)
    monkeys.append(monkey)
    num = 5 # monkey 5
    items = [88]
    operation = ('+',1)
    divisor = 17
    if_true = 4
    if_false = 7
    monkey = Monkey(num, items, operation, divisor, if_true, if_false)
    monkeys.append(monkey)
    num = 6 # monkey 6
    items = [84, 98, 78, 85]
    operation = ('**',2)
    divisor = 7
    if_true = 5
    if_false = 4
    monkey = Monkey(num, items, operation, divisor, if_true, if_false)
    monkeys.append(monkey)
    num = 7 # monkey 7
    items = [98, 89, 78, 73, 71]
    operation = ('+',4)
    divisor = 2
    if_true = 3
    if_false = 2
    monkey = Monkey(num, items, operation, divisor, if_true, if_false)
    monkeys.append(monkey)

def get_worry_factor(monkeys):
    factor = 1 
    for monkey in monkeys:
        factor *= monkey.divisor
    return factor

def calculate_answer(monkeys):
    inspection_list = []
    for monkey in monkeys:
        inspection_list.append(monkey.inspections)
    largest = max(inspection_list)
    inspection_list.remove(largest)
    second_largest = max(inspection_list)
    print(largest * second_largest)    
                    
    
if __name__ == '__main__':
    monkeys = []
    create_monkeys(monkeys)
    worry_factor = get_worry_factor(monkeys)
    for i in range(ROUNDS):
        for monkey in monkeys:
            while monkey.has_items():
                catcher, item = monkey.inspect_and_throw(worry_factor)
                monkeys[catcher].catch(item)
    calculate_answer(monkeys)

            

    



                
        
    
    
    
        
