def check_cycles(cycle, signal_strength, signal_sum, x):
    if (cycle-20) % 40 == 0:
        signal_strength = cycle * x
        signal_sum += signal_strength
    return (signal_strength, signal_sum)

def cathode_ray_tube():
    signal_sum = 0
    signal_strength = 0
    x = 1
    cycle = 0
    add_cycle = 0
    f = open('day_10.txt', 'r')
    for row in f:
        row_data = row.strip().split(" ")
        if row_data[0] == "noop":
            cycle += 1
            (signal_strength, signal_sum) = check_cycles(cycle, signal_strength, signal_sum, x)
        elif row_data[0] == "addx":
            while add_cycle < 2:
                cycle += 1
                (signal_strength, signal_sum) = check_cycles(cycle, signal_strength, signal_sum, x)
                add_cycle += 1
            x += int(row_data[1])
            add_cycle = 0

    print(signal_sum)
                    
    
if __name__ == '__main__':
    cathode_ray_tube()
