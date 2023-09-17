import random
import arcade

class Cloud(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()

        self.texture = arcade.load_texture('pic/cloud.png')

        self.height = random.randint(70 , 100) #ابعاد به صورت رندوم
        self.width = random.randint(100 , 200) # ابعاد به صورت رندوم
        self.center_x = SCREEN_WIDTH # مختصات
        self.center_y = random.randint(SCREEN_HEIGHT // 3 , SCREEN_HEIGHT) # ارتفاع به صورت رندوم
        self.speed = 2 # سرعت
        self.change_x = -1 * self.speed # تغییر مختصات
