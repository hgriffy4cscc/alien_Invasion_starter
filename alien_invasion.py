import sys
import pygame
from time import sleep
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
# from alien import Alien
from alien_fleet import AlienFleet
from button import Button

class AlienInvasion:

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)


        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_w,self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.bullet_sound_file)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound_file)
        self.impact_sound.set_volume(0.8)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.play_button = Button(self, 'Play')
        self.game_active = False

        self.pause_aliens = False
    
    def run_game(self):
        # Game Loop
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                if not self.pause_aliens:
                    self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        # check ship collisions viz aliens
        if self.ship.check_collisions( self.alien_fleet.fleet):
            self._check_game_status()
            # de-increment 1 life

            # check aliens viz bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()

    # check bullets viz aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

    def _check_game_status(self):
        if self.game_stats.ships_remaining > 0:
            self.game_stats.ships_remaining -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    def _reset_level(self):
        self.ship.arsenal.arsenal.remove()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self):
        # set up dynamic settings
        # reset Game stats
        # update HUD scores
        self._reset_level
        self.ship._center_ship
        self.game_active = True
        pygame.mouse.set_visible(False)


    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        if event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
        if event.key == pygame.K_p:
            if self.pause_aliens:
                self.pause_aliens = False
            else:
                self.pause_aliens = True


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
