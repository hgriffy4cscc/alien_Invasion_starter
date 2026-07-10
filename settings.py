"""file to hold durable settings for Alien Invasion and related games"""

from pathlib import Path

class Settings:
    """class for game-wide settings"""

    def __init__(self) -> None:
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS: int = 60
        self.images_path = Path.cwd() / 'Assets' / 'images'
        self.bg_file = self.images_path / 'Starbasesnow.png'