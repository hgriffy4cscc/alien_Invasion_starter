import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
# from alien import Alien
from alien_fleet import AlienFleet

class AlienInvasion:

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

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

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.bullet_sound_file)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound_file)
        self.impact_sound.set_volume(0.8)

        self.pause_aliens = False
    
    def run_game(self):
        # Game Loop
        while self.running:
            self._check_events()
            self.ship.update()
            if not self.pause_aliens:
                self.alien_fleet.update_fleet()
            self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        # check ship collisions viz aliens
        if self.ship.check_collisions( self.alien_fleet.fleet):
            self._reset_level()
            # de-increment 1 life

        # check bullets viz aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

    def _reset_level(self):
        self.ship.arsenal.arsenal.remove()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

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
