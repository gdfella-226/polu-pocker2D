import pygame
import subprocess

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        display.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

pygame.init()
display = pygame.display.set_mode((480, 320))
icon = pygame.image.load('./sourses/pics/m_icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('PoluPoker 2D')
bg = pygame.image.load('./sourses/pics/m_bg.png')
menu_font = pygame.font.Font(None, 40)
options = [Option("NEW GAME", (140, 105)), Option("LOAD GAME", (135, 155)),
           Option("OPTIONS", (145, 205))]
while True:
    pygame.event.pump()
    display.fill((0, 0, 0))
    display.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if options[0].rect.collidepoint(pygame.mouse.get_pos()):
                print('loading')
                subprocess.call('A_modern.py', shell=True)

    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()
    pygame.display.update()
