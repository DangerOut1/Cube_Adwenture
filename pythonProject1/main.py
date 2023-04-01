import pygame

ticks = 40
movis_mov_obs_list = []
obs_list = []
obgects = []
pygame.mixer.pre_init(44100, -16, 512)
pygame.init()
window = pygame.display.set_mode((500, 260))
clock = pygame.time.Clock()
n_c_t = 10
end = False
sound1 = pygame.mixer.Sound('gluhoy-korotkiy-zvuk.wav')
pygame.mixer.music.load('48bb90af8e1e401.mp3')
pygame.mixer.music.play(-1)

class Rects():
    def __init__(self, x, y, width, height, color=(0, 0, 0)):
        self.color2 = color
        self.rect = pygame.Rect(x, y, width, height)
        self.set_color = color
        obgects.append(self)

    def fill(self):
        pygame.draw.rect(window, self.set_color, self.rect)

    def set_new_color(self, color):
        self.set_color = color

    def set_new_color2(self, color):
        self.set_color = color
        self.color2 = color

    def new_view(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)


class Hero(Rects):
    def __init__(self, x, y, width, height, color, speed=10):
        self.flW = False
        self.flA = False
        self.flS = False
        self.flD = False
        self.speed = speed
        self.new_color = False
        super().__init__(x, y, width, height, color)
        self.is_chitcode = False
        self.new_color_time = False

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.flW = True
                if event.key == pygame.K_a:
                    self.flA = True
                if event.key == pygame.K_s:
                    self.flS = True
                if event.key == pygame.K_d:
                    self.flD = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.flW = False
                if event.key == pygame.K_a:
                    self.flA = False
                if event.key == pygame.K_s:
                    self.flS = False
                if event.key == pygame.K_d:
                    self.flD = False
        if self.flW:
            self.rect.y -= self.speed
        if self.flA:
            self.rect.x -= self.speed
        if self.flS:
            self.rect.y += self.speed
        if self.flD:
            self.rect.x += self.speed







    def is_colliderect(self, obstacle):
        return self.rect.colliderect(obstacle.rect)

    def game_mov(self, x, y):
        while self.is_chitcode != True:
            self.is_win = False
            clock.tick(ticks)
            for obgect in obgects:
                obgect.fill()
            pygame.display.update()
            self.movement()
            if self.is_colliderect(win) == False:
                for i in obs_list:
                    if self.is_colliderect(i) == True:
                        i.new_color = True
                        i.set_new_color((70, 70, 70))
                        i.new_color_time = n_c_t
                        self.new_color = True
                        self.set_new_color((255, 0, 0))
                        self.new_color_time = n_c_t
                        self.rect.x = x
                        self.rect.y = y
                        sound1.play()

                if len(movis_mov_obs_list) != 0:  # _________________
                    for i in movis_mov_obs_list:
                        if i.rect.x != i.x2:
                            if i.rect.x > i.x2:
                                if i.rect.x - i.speed < i.x2:
                                    i.rect.x = i.x2
                                else:
                                    i.rect.x -= i.speed
                            else:
                                if i.rect.x + i.speed > i.x2:
                                    i.rect.x = i.x2
                                else:
                                    i.rect.x += i.speed

                        if i.rect.y != i.y2:
                            if i.rect.y > i.y2:
                                if i.rect.y - i.speed < i.y2:
                                    i.rect.y = i.y2
                                else:
                                    i.rect.y -= i.speed
                            else:
                                if i.rect.y + i.speed > i.y2:
                                    i.rect.y = i.y2
                                else:
                                    i.rect.y += i.speed

                        if i.rect.x == i.x2 and i.rect.y == i.y2:
                            i.new_color = True
                            i.set_new_color((70, 70, 70))
                            i.new_color_time = n_c_t
                            i.y2 = i.y3
                            i.x2 = i.x3

                            i.x3 = i.rect.x
                            i.y3 = i.rect.y
            else:
                self.rect.x = x
                break
            window.fill((255, 255, 255))
            for obgect in obgects:
                if obgect.new_color != False:
                    if obgect.new_color_time == 0:
                        obgect.set_new_color(obgect.color2)
                        obgect.new_color = False
                    else:
                        obgect.new_color_time -= 1
                obgect.fill()
        self.is_chitcode = False


class Obstacles(Rects):
    def __init__(self, x, y, width, height, color, is_mov=False, speed=0, x2=0, y2=0):
        super().__init__(x, y, width, height, color)
        self.new_color = False
        self.is_mov = is_mov
        self.speed = speed
        self.x3 = x
        self.y3 = y
        self.x2 = x2
        self.y2 = y2
        if self.is_mov == True:
            movis_mov_obs_list.append(self)
        obs_list.append(self)


obs1 = Obstacles(125, 10, 50, 100, (0, 0, 0))
obs2 = Obstacles(250, 150, 50, 100, (0, 0, 0))
obs3 = Obstacles(400, 10, 50, 100, (0, 0, 0))
hero = Hero(25, 25, 50, 50, (0, 0, 255), 4)
ceiling = Obstacles(0, 0, 500, 10, (0, 0, 0))
floor = Obstacles(0, 250, 500, 10, (0, 0, 0))
wall = Obstacles(0, 10, 11, 240, (0, 0, 0))
win = Obstacles(490, 10, 10, 240, (255, 0, 0))

win = Obstacles(490, 10, 10, 240, (255, 0, 0))
while True:
    clock.tick(ticks)
    hero.game_mov(25, 25)
    window.fill((255, 255, 255))
    # lvl 2
    obs1.new_view(200, 155, 50, 105)
    obs2.new_view(200, 10, 50, 85)
    obs3.new_view(0, 0, 0, 0)
    wall.set_new_color2((255, 255, 255))
    mov_obs1 = Obstacles(310, 10, 50, 50, (0,0,0), True, 9, 310, 200)
    mov_obs2 = Obstacles(450, 100, 50, 50, (0,0,0), True, 4, 0, 100)
    hero.game_mov(25, 25)
    font1 = pygame.font.Font(None, 70)

    end = font1.render(
        "You won!", True, (0, 0, 0))
    window.fill((255, 255, 255))
    window.blit(end, (150, 100))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(3000)
    break
