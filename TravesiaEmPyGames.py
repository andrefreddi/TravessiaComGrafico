import pygame
import random

pygame.init()
wn = pygame.display.set_mode((600, 600))
font = pygame.font.SysFont('Arial', 25)
people = []

class Person():
    def __init__(self, name, x, y, color, side='UP', w=20, h=20, hate=[], like=[], alone=None):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.alone = alone
        self.hate = hate
        self.like = like
        self.side = side
        self.obj = pygame.Rect(x, y, w, h)
        people.append(self)
        conditions = []

        self.conditions = conditions

    def draw(self):
        self.obj = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(wn, self.color, self.obj)

    def entrar_no_barco(self, boat):
        self.x = random.randint(boat.x, boat.x+boat.w-self.w)
        self.y = random.randint(boat.y, boat.y+boat.h-self.h)
        self.side = boat.side

    def condicoes_de_gravacao(self, x, y):
        text = font.render(f"{self.name} {'; '.join(self.conditions)}", True, (0, 0, 0))
        wn.blit(text, (x, y))

    def sair_do_barco(self, boat):
        self.x += random.randint(50, 200)

    def no_barco(self, boat):
        return boat.x+boat.w-self.w >= self.x >= boat.x and boat.y+boat.h-self.h >= self.y >= boat.y

class Boat():
    def __init__(self, room, x=280, y=200, color=(140, 140, 140), w=40, h=60, side='UP'):
        self.room = room
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.trips = 0
        self.color = color
        self.obj = pygame.Rect(x, y, w, h)
        self.side = side
        self.aboard = []
        
    def navegar(self):
        hated = [name for person in boat.aboard for name in person.hate]
        liked = [name for person in boat.aboard for name in person.like]
        no = False
        if any(person.alone == True for person in self.aboard) and len(self.aboard) > 1:
            no = True
        elif any(person.alone == False for person in self.aboard) and len(self.aboard) == 1:
            no = True
        elif any(person.name == name for person in self.aboard for name in hated):
            no = True
        elif liked:
            if any(person.name == name for person in self.aboard for name in liked):
                no = False
            else:
                no = True
        else:
            no = False
        if not no:
            if self.side == 'UP':
                self.y += 300
                self.side = 'DOWN'
            else:
                self.y -= 300
                self.side = 'UP'
            self.obj.y = self.y

    def draw(self):
        pygame.draw.rect(wn, self.color, self.obj)


boat = Boat(2)

ladrao = Person('ladrao', boat.x-100, boat.y, (139,69,19), like=['policial'], hate=['pai', 'mae', 'filho_01', 'filho_02', 'filha_01', 'filha_02']) # Viaja_Sozinho = MARROM
policial = Person('policial', boat.x-70, boat.y, (255, 0, 0)) # policial = VERMELHO

pai = Person('pai', boat.x+70, boat.y, (0,0,255), like=['filho_01', 'filho_02', 'mae', 'policial', 'pai']) # pai = AZUL
mae = Person('mae', boat.x+100, boat.y, (255,0,255), like=['filho_01', 'filho_02', 'pai', 'policial', 'mae']) # mae = ROSA 

filho_01 = Person('filho_01', boat.x+130, boat.y, (34,139,34), like=['pai', 'policial'], hate=['mae']) # filho_01 = VERDE CLARO
filho_02 = Person('filho_02', boat.x+160, boat.y, (0,100,0), like=['pai', 'policial'], hate=['mae']) # filho_02 = VERDE ESCURO

filha_01 = Person('filha_01', boat.x+190, boat.y, (138,43,226), like=['mae', 'policial'], hate=['pai']) # filha_01 = VIOLETA
filha_02 = Person('filha_02', boat.x+220, boat.y, (148,0,211), like=['mae', 'policial'], hate=['pai']) # filha_02 = VIOLETA ESCURO

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for person in people:
                if person.obj.collidepoint(pygame.mouse.get_pos()):
                    if person in boat.aboard:
                        person.sair_do_barco(boat)
                        boat.aboard.remove(person)
                        boat.room += 1
                    else:
                        if boat.room and person.side == boat.side:
                            person.entrar_no_barco(boat)
                            boat.aboard.append(person)
                            boat.room -= 1

            if not any(person.obj.collidepoint(pygame.mouse.get_pos()) for person in people):
                if boat.obj.collidepoint(pygame.mouse.get_pos()):
                    if boat.aboard and boat.room >= 0:
                        boat.navegar()
                        for person in boat.aboard:
                            person.entrar_no_barco(boat)
                        boat.trips += 1
                    
    wn.fill((255, 255, 255))
    pygame.draw.rect(wn, (100, 200, 255), (0, 290, 600, 180))
    boat.draw()
    for i, person in enumerate(people):
        person.draw()
        person.condicoes_de_gravacao(0, i*25)
    

    pygame.display.update()
