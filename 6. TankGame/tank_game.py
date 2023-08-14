import arcade
import random
from app_objects import Tank, Enemy

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Tank"

SPEED = 10

def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.rot_speed = 0.5
        self.speed = 10
        self.tank = Tank(700, 400, get_random_color())
        self.tank2 = Tank(50, 400, get_random_color())
        self.enemies = [
            Enemy(
                random.randrange(200, SCREEN_WIDTH-100),
                random.randrange(100, SCREEN_HEIGHT-150),
                20
            )
            for _ in range(10)
        ]
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.tank.shoot(20)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.tank.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.tank.speed = -SPEED

        if symbol == arcade.key.LEFT:
            self.tank.angular_speed = 1.5
        if symbol == arcade.key.RIGHT:
            self.tank.angular_speed = -1.5

        if symbol == arcade.key.W:
            self.tank2.speed = SPEED
        if symbol == arcade.key.S:
            self.tank2.speed = -SPEED

        if symbol == arcade.key.A:
            self.tank2.angular_speed = 1.5
        if symbol == arcade.key.D:
            self.tank2.angular_speed = -1.5
        
        if symbol == arcade.key.SPACE:
            self.tank2.shoot(20)
            
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.tank.speed = 0

        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.tank.angular_speed = 0

        if symbol in (arcade.key.W, arcade.key.S):
            self.tank2.speed = 0

        if symbol in (arcade.key.A, arcade.key.D):
            self.tank2.angular_speed = 0

    def on_update(self, delta_time: float):
        self.tank.update(delta_time)
        self.tank2.update(delta_time)

        for e in self.enemies:
            e.detect_collision(self.tank)
            e.detect_collision(self.tank2)

        
    def on_draw(self):
        arcade.start_render()
        self.tank.draw()
        self.tank2.draw()
        for e in self.enemies:
            e.draw()
    
    
if __name__ == "__main__":
    app = App()
    arcade.run()