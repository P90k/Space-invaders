

class GameObjects:
    """Basic class to represent objects in game engine and on screen"""

    def __init__(self, screen, space):
        super().__init__()
        self.screen = screen
        self.space = space


    def update(self):
        pass


class Tank(GameObjects):

    def __init(self):
        super().__init__()


class Bullet(GameObjects):

    def __init__(self):
        super().__init__()


class GlobalVars(GameObjects):
    """Class to store all variables within game"""

    def __init__(self, screen, space):
        super().__init__(screen, space)
        # Should I have one list with all objects or
        # several lists to increase readability?
        self.objects = {
            'game_objects_list': [],
        }

    def key_exists(self, key) -> True:
        """Predicate function to check if key exists in objects attr"""
        return key in self.objects

    def add_var(self, key, value) -> str:
        """Add key, value pair to objects attr"""
        if not self.key_exists(key):
            self.objects[key] = value
            return "Key stored"
        else:
            return "Key already stored"

    def add_game_object(self, obj):
        """Add element to game objects list"""
        self.objects['game_objects_list'].append(obj)

    def remove_game_object(self):
        """Remove element from game obj sequence"""
        # When we have real objects, find shape.parent
        # and remove that specific object to avoid removing
        # similar objects that should not be removed.
        self.objects['game_objects_list'].remove(obj)

    def get_key(self, key):
        """Get value of key from objects"""
        if self.key_exists(key):
            return self.objects[key]
