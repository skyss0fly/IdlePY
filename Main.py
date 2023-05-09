import pygame as pg

class SoftwareRender:
  def __init__(self):
    self.RES = self.WIDTH, self.HEIGHT = 1600,900
    self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT //2
    self.FPS = 60
    self.screen = pg.display.set_mode(self.RES)
    self.clock = pg.time.Clock()
