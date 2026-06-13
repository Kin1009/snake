import time, random, system, graphics as g

g.init()
c = g.canvas
TOP = 12
W, H = 240, 135
CELL = 6

cols = W // CELL
rows = H // CELL
score = 0
snake = [(10, 10)]
dir = (1, 0)
food = (20, 10)

def spawn():

    while True:

        pos = (
            random.randint(0, cols - 1),
            random.randint(0, rows - 1)
        )

        if pos not in snake:
            return pos
exit_hold_start = None

def check_exit():
    global exit_hold_start

    if system.key1_pressed() and system.key2_pressed():

        if exit_hold_start is None:
            exit_hold_start = time.ticks_ms()

        elif time.ticks_diff(time.ticks_ms(), exit_hold_start) > 2000:
            return True

    else:
        exit_hold_start = None

    return False

while True:

    if check_exit():
        break

    if system.key1_just_pressed():
        dir = (-dir[1], dir[0])

    if system.key2_just_pressed():
        dir = (dir[1], -dir[0])

    head = snake[0]

    new_head = (
        (head[0] + dir[0]) % cols,
        (head[1] + dir[1]) % rows
    )
    
    if new_head == food:

        score += 1
        food = spawn()

    else:

        snake.pop()

    snake.insert(0, new_head)

    c.fillScreen(0x000000)

    # food
    c.fillRect(
    food[0] * CELL,
    TOP + food[1] * CELL,
    CELL,
    CELL,
    0x00FF00
    )

    # snake
    for s in snake:

        c.fillRect(
            s[0] * CELL,
            TOP + s[1] * CELL,
            CELL,
            CELL,
            0xFFFFFF
        )
    c.setTextColor(0xFFFFFF)
    c.setCursor(2, 2)
    c.print("Score: " + str(score))
    c.push(0, 0)
    time.sleep_ms(120)