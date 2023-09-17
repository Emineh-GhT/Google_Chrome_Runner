import arcade

class Dinosaur(arcade.AnimatedWalkingSprite):
    def __init__(self, SCREEN_WIDTH , SCREEN_HEIGHT):
        super().__init__()
        self.stand_right_textures = [arcade.load_texture('pic/dinosaur.png')] # عکس در حالت ایستاده
        self.walk_right_textures = [arcade.load_texture('pic/dinosaur-walk.png')] # عکس در حالت حرکت
        self.walk_down_textures = [arcade.load_texture('pic/bending.png')] # عکس در حالت خمیده
        self.width = 150 # ابعاد
        self.height = 150 # ابعاد
        self.center_x = SCREEN_WIDTH // 3 # مختصات
        self.center_y = ( SCREEN_HEIGHT // 3 ) - 50 # مختصات
        self.score = 0 # امتیاز
        self.high_score = 0 # بیشترین امتیاز
        self.health_flag = True # سلامتی
