import pygame
import os
import random
from utils.player import Player, WIDTH, HEIGHT
from utils.enemy import Enemy


pygame.font.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Game")


BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background_black.png")), (WIDTH, HEIGHT))


def collide(object1, object2):
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) is not None


def main():
    run = True
    FRAMESPERSECOND = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("SegoeUI", 50)
    lost_font = pygame.font.SysFont("SegoeUI", 60)

    enemies = []
    wave_length = 5
    enemy_velocity = 2

    player_velocity = 5
    laser_velocity = 10

    player = Player(300, 650)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WINDOW.blit(BACKGROUND, (0, 0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.spawn(WINDOW)

        player.spawn(WINDOW)

        if lost:
            lost_label = lost_font.render("You Lose!!", 1, (255, 255, 255))
            WINDOW.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FRAMESPERSECOND)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FRAMESPERSECOND * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemies = [Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                           for _ in range(wave_length)]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_velocity > 0:  # left
            player.x -= player_velocity
        if keys[pygame.K_d] and player.x + player_velocity + player.get_width() < WIDTH:  # right
            player.x += player_velocity
        if keys[pygame.K_w] and player.y - player_velocity > 0:  # up
            player.y -= player_velocity
        if keys[pygame.K_s] and player.y + player_velocity + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_velocity
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies:
            enemy.move(enemy_velocity)
            enemy.move_lasers(laser_velocity, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_velocity, enemies)


def main_menu():
    title_font = pygame.font.SysFont("SegoeUI", 50)
    run = True
    while run:
        WINDOW.blit(BACKGROUND, (0, 0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255, 255, 255))
        WINDOW.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        title_label = title_font.render("Use 'wasd' to move", 1, (255, 255, 255))
        WINDOW.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 500))
        title_label = title_font.render("and space bar to shoot", 1, (255, 255, 255))
        WINDOW.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 550))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()
