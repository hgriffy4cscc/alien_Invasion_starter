"""file to hold durable settings for Alien Invasion and related games"""

from pathlib import Path

class Settings:
    """class for game-wide settings"""

    def __init__(self) -> None:
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS: int = 60
        self.images_path: Path = Path.cwd() / 'Assets' / 'images'
        self.bg_file: Path = self.images_path / 'Starbasesnow.png'

        self.ship_file: Path = self.images_path / 'ship2(no bg).png'
        self.ship_w: int = 40
        self.ship_h: int = 60
        self.ship_speed: int = 5
        self.starting_ship_count = 3

        self.bullet_file: Path = self.images_path / 'laserBlast.png'
        self.bullet_sound_file: Path = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound_file: Path = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_count = 5

        self.alien_file: Path = self.images_path / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.alien_fleet_speed = 3
        self.alien_fleet_direction = 1
        self.alien_fleet_drop_speed = self.alien_h

        self.button_w = 300
        self.button_h = 75
        self.button_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'