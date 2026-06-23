import random

WIDTH = 800
HEIGHT = 600
score = 0
player = Actor("alien")
player.pos = (400, 300)
enemy = Actor("splat")
enemy.pos = (400, 300)
enemy_bad = Actor("green_splat")
enemy_bad.pos = (700, 500)


def move_red():
    enemy.x = random.randint(50, 750)
    enemy.y = random.randint(50, 550)
    clock.unschedule(move_red)
    clock.schedule_interval(move_red, 2.5)


# GREEN SPLAT: Moves strictly on its own heartbeat
def move_green():
    enemy_bad.x = random.randint(50, 750)
    enemy_bad.y = random.randint(50, 550)


def draw():
    screen.fill((0, 0, 0))
    player.draw()
    enemy.draw()
    enemy_bad.draw()
    screen.draw.text("Score: " + str(score), (20, 20), color="white", fontsize=30)


def update():
    global score
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5

    if player.colliderect(enemy):
        score += 1
        move_red()

    if player.colliderect(enemy_bad):
        score -= 1
        move_green()


clock.schedule_interval(move_red, 4.0)
clock.schedule_interval(move_green, 1.2)
