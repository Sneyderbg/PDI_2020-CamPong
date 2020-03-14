from objects.sprites import *
from tools import Tools
import numpy as np
import cv2
import sys


def init_sprites():
    w, h = Tools.translate(window_size, 20, 100)
    x, y = Tools.translate(window_size, 5, int(height / 2 - h / 2))
    j1 = Player(x, y, w, h)
    x = Tools.translate(window_size, width - 10 - w / 2)[0]
    j2 = Player(x, y, w, h)
    j1.set_speed(speed)
    j2.set_speed(speed)
    w, h = 20, 20
    x, y = Tools.translate(window_size, width / 2 - w, height / 2 - h)
    ball = Ball(x, y, w, h)
    return j1, j2, ball


def draw_sprites(surface):
    pygame.draw.rect(surface, J1.color, J1.rect)
    pygame.draw.rect(surface, J2.color, J2.rect)
    pygame.draw.ellipse(surface, JBall.color, JBall.rect)


def cv2_to_pygame(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (width, height))
    frame = pygame.image.frombuffer(frame.tostring(), np.shape(frame)[1::-1], "RGB")
    return frame


game_fps = 60
debug = False

cam1 = cv2.VideoCapture(0)

pygame.init()
window_size = width, height = 640, 480
pygame.display.set_caption("CamPong")
screen = pygame.display.set_mode(window_size, DOUBLEBUF)
screen_rect = screen.get_rect()
black = 0, 0, 0
font = pygame.font.Font(None, 30)

speed = 20
sprites = J1, J2, JBall = init_sprites()
screen_rect.y, screen_rect.h = JBall.rect.h, screen_rect.h - 2 * JBall.rect.h
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT, 100)
running = True
0
ret1, frame1 = cam1.read()
frame1 = cv2_to_pygame(frame1)

while running:
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False
        if e.type == USEREVENT:
            ret1, frame1 = cam1.read()
            frame1 = cv2_to_pygame(frame1)
        if e.type == KEYDOWN:
            if e.key == K_COMMA:
                debug = not debug

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        running = False

    if keys[K_w]:
        if J1.rect.top - J1.speed > 0:
            J1.move('up')
    if keys[K_s]:
        if J1.rect.bottom + J1.speed < height:
            J1.move('down')
    if keys[K_UP]:
        if J2.rect.top - J2.speed > 0:
            J2.move('up')
    if keys[K_DOWN]:
        if J2.rect.bottom + J2.speed < height:
            J2.move('down')

    # debug
    if debug:
        if keys[K_k]:
            game_fps -= 1
        if keys[K_l]:
            game_fps += 1
        if keys[K_o]:
            JBall.set_speed(JBall.V + 1)
        if keys[K_i]:
            JBall.set_speed(JBall.V - 1)
    # debug

    if JBall.rect.colliderect(screen_rect):
        JBall.move()
    elif JBall.rect.x <= 0 or JBall.rect.x >= width:
        text = font.render("Game Over", 1, (255, 0, 255))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        time.wait(250)
        running = False
        break
    else:
        JBall.set_xy(JBall.rect.x, JBall.rect.y - JBall.Vy)
        JBall.set_speed_xy(JBall.Vx, -JBall.Vy)
    collide = pygame.sprite.spritecollideany(JBall, (J1, J2))
    if collide is J1:
        JBall.set_direction(1)
    elif collide is J2:
        JBall.set_direction(-1)

    screen.fill(black)
    screen.blit(frame1, Rect(0, 0, width // 2, height))
    pygame.draw.rect(screen, (100, 100, 100), screen_rect, 1)
    draw_sprites(screen)
    fps = font.render('fps: ' + str(clock.get_fps()), 1, (200, 200, 200))
    screen.blit(fps, (0,0))
    if debug:
        debug_fps = font.render('game fps: ' + str(game_fps), 1, (200, 200, 200))
        debug_speed = font.render('speed: ' + str(JBall.V), 1, (200, 200, 200))
        screen.blit(debug_fps, (0, font.get_height()))
        screen.blit(debug_speed, (0, 2 * font.get_height()))
    pygame.display.update()
    clock.tick(game_fps)
sys.exit()
