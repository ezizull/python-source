import pygame
import neat
import time
import os
import random


WIN_WIDTH = 400
WIN_HEIGHT = 600

BIRD_WIDTH = 39
BIRD_HEIGHT = 29

BIRD_IMG = [pygame.transform.scale(pygame.image.load(os.path.join("asset/flappy_bird","bird1.png")), (BIRD_WIDTH,BIRD_HEIGHT)),pygame.transform.scale(pygame.image.load(os.path.join("asset/flappy_bird","bird2.png")), (BIRD_WIDTH,BIRD_HEIGHT)),pygame.transform.scale(pygame.image.load(os.path.join("asset/flappy_bird","bird3.png")), (BIRD_WIDTH,BIRD_HEIGHT))]
PIPE_IMG = pygame.transform.scale(pygame.image.load(os.path.join("asset/flappy_bird","pipe.png")), (WIN_WIDTH,WIN_HEIGHT))
BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join("asset/flappy_bird","bg.png")), (400,650))
BASE_IMG = pygame.transform.scale(pygame.image.load(os.path.join("asset/flappy_bird","base.png")), (406,182))


class Bird:
    IMGS = BIRD_IMG
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.miring = 0
        self.gerakan = 0
        self.kecepatan = 0
        self.tinggi = self.y
        self.no_img = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.kecepatan = -10.5
        self.gerakan = 0
        self.tinggi = self.y + 2

        if self.y < -20: # Atas = 0 , Atas != WIN_HEIGHT
            self. y = -20
    
    def move(self):
        self.gerakan += 1
        
        t = self.kecepatan*self.gerakan + 1.5*self.gerakan**2

        if t >= 16:
            t = 16

        if t < 0:
            t -= 2

        self.y = self.y + t

        if t < 0 or self.y < self.tinggi + 20:
            if self.miring < self.MAX_ROTATION:
                self.miring = self.MAX_ROTATION
        else:
            if self.miring > -90:
                self.miring -= self.ROT_VEL

    def  draw(self, win):
        self.no_img += 1

        if self.no_img < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.no_img < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.no_img < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.no_img < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.no_img < self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.no_img = 0
        
        if self.tinggi <= -80:
            self.img = self.IMGS[1]
            self.no_img = self.ANIMATION_TIME*2

        image_miring = pygame.transform.rotate(self.img, self.miring)
        new_rect = image_miring.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(image_miring, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.tinggi = 0
        self.gap = 100

        self.top = -20
        self.bottom = 620
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height - self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True
        
        return False


class Base:
    VEL = 6
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH 

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH 

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


def draw_window(win, bird, pipes, base):
    win.blit(BG_IMG, (0,0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)

    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird(180,250)
    base = Base(510)
    pipes = [Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    waktu = pygame.time.Clock()

    run = True
    while run:
        waktu.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # bird.move()
        base.move()
        draw_window(win, bird, pipes, base)

    pygame.quit()
    quit()

main()

