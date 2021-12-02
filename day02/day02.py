with open("input.txt", "r") as course:

    course = course.read().splitlines()

    horizontal_pos = 0
    depth = 0
    aim = 0

    for i in range(len(course)):
        seq = [p for pair in course[i:i+1] for p in pair.split()]

        if seq[0] == "forward":
            horizontal_pos += int(seq[1])
            depth += (aim * int(seq[1]))
        elif seq[0] == "down":
            aim += int(seq[1])
        elif seq[0] == "up":
            aim -= int(seq[1])

    print(horizontal_pos * depth)