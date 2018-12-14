import sys
import pygame
from rocket import Rocket
from setting import Setting
import game_functions as gf
def run():
	pygame.init()
	ai_setting = Setting()
	screen =pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
	pygame.display.set_caption("Rocket")
	r = Rocket(ai_setting,screen)
	while True:
		gf.check_events(r)
		r.update()
		gf.update_screen(ai_setting,screen,r)
run()
