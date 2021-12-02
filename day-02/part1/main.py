h_pos = 0
depth = 0

# hpos cmds
FORWARD = "forward"

# depth cmds
DOWN = "down"
UP = "up"

with open("../input.txt") as input_file:
    lines = input_file.read().splitlines()
    for l in lines:
        cmd, num = l.split()
        num = int(num)

        if cmd == FORWARD:
            h_pos += num
        elif cmd == DOWN:
            depth += num
        elif cmd == UP:
            depth -= num

solution = h_pos * depth
print("With a horizontal pos {} and a depth of {} the result is {}".format(
    h_pos, depth, solution))
