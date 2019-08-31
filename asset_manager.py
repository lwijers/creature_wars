import pygame

RESOURCES  = {
    'images' : [
        'enemy_base',
        'player_base',
        'neutral_base',
        'player_creature',
        'enemy_creature'
    ]
}


class AssetManager:
    def __init__(self):
        self.resources = {
            'images' : {}
        }
        self.load_images()

    def load_images(self):
        for image_name in RESOURCES['images']:
            self.resources['images'][image_name] = pygame.image.load(
                'resources/images/' +
                image_name +
                '.png'
            )

    def give_image(self, image_name):
        return self.resources['images'][image_name]


mngr = AssetManager()