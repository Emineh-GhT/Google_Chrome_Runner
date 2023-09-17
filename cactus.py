import arcade

class Cactus(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH , SCREEN_HEIGHT , cactus_speed):
        super().__init__()
        self.texture = arcade.load_texture('pic/cactus.png')
        self.width = 60 # ابعاد
        self.height = 150 # ابعاد
        self.center_x = SCREEN_WIDTH #مختصات
        self.center_y = ( SCREEN_HEIGHT // 3 ) - 50 # مختصات
        self.speed = cactus_speed # سرعت
        self.change_x = -1 * self.speed # تغییر مختصات