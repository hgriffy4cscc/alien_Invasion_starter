from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():

    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        
        self.reset_stats()
        self.max_score = 0

    def reset_stats(self):
        self.ships_remaining = self.settings.starting_ship_count
        self.game_level = 1
        self.score = 0
    
    def update(self, collisions):
        # update score
        self._update_score(collisions)

        # update max_score
        self._update_max_score()

        # update high_score

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f'Max: {self.max_score}')

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points
        # print(f'Score: {self.score}')

    def update_level(self):
        self.game_level += 1
        print(f'Level: {self.game_level}')