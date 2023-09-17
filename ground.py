import arcade

class Ground(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH , SCREEN_HEIGHT):
        super().__init__()
        self.texture = arcade.load_texture('pic/ground.png')
        self.center_x = SCREEN_WIDTH # مختصات
        self.center_y = ( SCREEN_HEIGHT // 3 ) - 100 # مختصات
        self.speed = 2 # سرعت
        self.change_x = -1 * self.speed # تغییر مختصات
