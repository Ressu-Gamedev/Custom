#Sprite Functions
import pygame as pg
#Cannon
def generateCannon(x,y):
    pg.draw.rect(self.screen, BLACK, (x, y, 20, 20))
    pg.draw.rect(self.screen, WHITE, (x, y, 18, 18))
    pg.draw.rect(self.screen, BLACK, (x, y+10, 5, 30))
    pg.draw.rect(self.screen, WHITE, (x, y+10, 3, 28))

def generatePanel(x,y):
    pg.draw.polygon(self.screen, BLACK, [[x+10,y+10],[x-10,y-10],[x+8,y+12]], 2)
