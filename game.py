


import pygame
from settings import Settings
from button import Button
from player import Player
from bubble import Bubble
<<<<<<< HEAD
<<<<<<< HEAD
=======
from scoreboard import Scoreboard
from game_stats import GameStats
>>>>>>> play-button-and-game-score
=======
from scoreboard import Scoreboard
from game_stats import GameStats
>>>>>>> play-button-and-game-score
import game_functions as gf

def run_game():
    pygame.init()
    gm_settings = Settings()


    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)
    
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> play-button-and-game-score
    
    play_button = Button(gm_settings, screen, "Play")
    
    
   
    
    
    stats = GameStats()
    
    sb = Scoreboard(gm_settings, screen, stats)
    
<<<<<<< HEAD
>>>>>>> play-button-and-game-score
=======
>>>>>>> play-button-and-game-score
    clock = pygame.time.Clock()
    
    
    player = Player(screen)
    
    
    bubbles = pygame.sprite.Group()


<<<<<<< HEAD
<<<<<<< HEAD
    while True:
        gf.check_events(gm_settings, screen, player, bubbles)
        player.update()
        gf.update_bubbles(player, bubbles)
        bubbles.update()
        gf.update_screen(gm_settings, screen, player, bubbles, clock)
        
=======
=======
>>>>>>> play-button-and-game-score


    while True:
        gf.check_events(gm_settings, screen, player, bubbles, stats, play_button)
        if stats.game_active:
            player.update()
            gf.update_bubbles(player, bubbles, stats, sb)
            bubbles.update()
        else:
            bubbles.empty()
        gf.update_screen(gm_settings, screen, player, bubbles, clock, stats, play_button, sb)    
<<<<<<< HEAD
>>>>>>> play-button-and-game-score
=======
>>>>>>> play-button-and-game-score
run_game()