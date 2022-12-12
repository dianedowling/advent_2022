WIDTH = 40
HEIGHT = 6

     
def show_display(display):
    i = 0
    for j in range(HEIGHT):
        for k in range(WIDTH):
            print(display[i], end="")
            i += 1
        print("\r")        


def check_cycles(cycle, signal_strength, signal_sum, x):
    if (cycle-20) % 40 == 0:
        signal_strength = cycle * x
        signal_sum += signal_strength
    return (signal_strength, signal_sum)


def draw_pixel(cycle, x, display):
    pixel = cycle - 1
    multiplier = pixel // 40
    x = x + (multiplier * 40) #adjust for each new row
    if pixel in (x-1, x, x+1):
        display[pixel] = "#"    


def cathode_ray_tube(display):
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
            draw_pixel(cycle, x, display)
        elif row_data[0] == "addx":
            while add_cycle < 2:
                cycle += 1
                (signal_strength, signal_sum) = check_cycles(cycle, signal_strength, signal_sum, x)
                draw_pixel(cycle, x, display)
                add_cycle += 1
            x += int(row_data[1])
            add_cycle = 0
                    
    
if __name__ == '__main__':
    display = []
    for i in range(WIDTH * HEIGHT):
        display.append(".")
    cathode_ray_tube(display)
    show_display(display)
    
        
