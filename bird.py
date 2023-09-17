import random
import arcade

class Bird(arcade.AnimatedWalkingSprite):
    def __init__(self, SCREEN_WIDTH , SCREEN_HEIGHT , bird_speed):
        super().__init__()
        self.walk_left_textures = [arcade.load_texture('pic/bird0.png'), arcade.load_texture('pic/bird1.png')]
        self.center_x = SCREEN_WIDTH # مختصات
        self.center_y = random.randint(SCREEN_HEIGHT // 3 , SCREEN_HEIGHT) # مختصات ارتفاع پرواز به صورت تصادفی
        self.speed = bird_speed  # سرعت
        self.change_x = -1 * self.speed # تغییر مختصات