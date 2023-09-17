import time
import arcade

from ground import Ground
from dinosaur import Dinosaur
from cactus import Cactus
from bird import Bird
from cloud import Cloud
from moon import Moon



SCREEN_WIDTH = 1000 # طول صفحه بازی
SCREEN_HEIGHT = 800 # ارتفاع صفحه بازی
GRAVITY = 0.1 #جاذبه
TITLE = 'Google Chrome Runner' # عنوان صفحه بازی



class Game(arcade.Window):
    def __init__(self):
        super().__init__( SCREEN_WIDTH , SCREEN_HEIGHT, TITLE)

        self.background_color = arcade.color.WHITE #رنگ بک گراند

        self.start_time = time.time()
        self.game_time = time.time()
        self.day_flag = True # مشخص کننده روز یا شب بودن بازی
        self.start_game_flag = False
        self.new_game_flag = False

        self.ground_list = arcade.SpriteList() # زمین
        self.ground_list.append(Ground(SCREEN_WIDTH, SCREEN_HEIGHT))

        self.cloud_list = arcade.SpriteList() # ابر
        self.cloud_list.append(Cloud(SCREEN_WIDTH, SCREEN_HEIGHT)) 

        self.moon = Moon(SCREEN_WIDTH , SCREEN_HEIGHT) # ماه

        self.me = Dinosaur(SCREEN_WIDTH , SCREEN_HEIGHT) # دانیاسور

        self.cactus_list = arcade.SpriteList() # کاکتوس
        self.cactus_time = time.time()
        self.cactus_speed = 2

        self.bird_list = arcade.SpriteList() # پرنده
        self.bird_time = time.time()
        self.bird_speed = 4


        self.my_physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.ground_list, gravity_constant= GRAVITY) #قوانین فیزیک 

    
    def start_new_game(self):
        self.start_time = time.time()
        self.me.health_flag = True
        self.start_game_flag = True
        self.new_game_flag = True
        self.me.score = 0
        self.cactus_speed = 2
        self.bird_speed = 4
        if self.me.score >= self.me.high_score:
            self.me.high_score = self.me.score

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.start_game_flag = True
            self.start_new_game()
        elif key == arcade.key.DOWN:
            self.me.change_x = 0
        elif key == arcade.key.UP:
            if self.my_physics_engine.can_jump():
                self.me.change_y = 10
                arcade.play_sound(arcade.sound.Sound(':resources:sounds/jump3.wav'))        

    def on_key_release(self, key, modifiers):
        self.me.change_x = 1
        self.me.change_y = 0

    def game_over(self):
            arcade.draw_text('GAME OVER !!!', 100 , SCREEN_HEIGHT//2, arcade.color.GRAY, 70)
            arcade.draw_text('please press space for start new game', 100 , SCREEN_HEIGHT//3, arcade.color.GRAY, 40)
        

    def on_draw(self): # رسم موجودات در صفحه بازی
        arcade.start_render()

        if self.me.health_flag : # سلامت بودن دانیاسور
           
            self.me.draw()

            if self.start_game_flag:

                if self.new_game_flag:

                    if self.day_flag: #روز بودن
                        arcade.draw_text(f'High Score: {self.me.high_score}', 50 , SCREEN_HEIGHT-100, arcade.color.GRAY, 30)
                    else: # شب بودن
                        arcade.draw_text(f'High Score: {self.me.high_score}', 50 , SCREEN_HEIGHT-100, arcade.color.GRAY, 30)
                        self.moon.draw()

                if self.day_flag: # روز بودن
                    arcade.draw_text(f'Score: {self.me.score}', SCREEN_WIDTH-200 , SCREEN_HEIGHT-100, arcade.color.GRAY, 30)
                else: # شب بودن
                    arcade.draw_text(f'Score: {self.me.score}', SCREEN_WIDTH-200 , SCREEN_HEIGHT-100, arcade.color.GRAY, 30)
                    
                for ground in self.ground_list:
                    ground.draw() # رسم زمین

                for cloud in self.cloud_list:
                     cloud.draw() # رسم ابر

                for cactus in self.cactus_list:
                    cactus.draw() # رسم کاکتوس

                for bird in self.bird_list:
                    bird.draw() # رسم پرنده

        else: # عدم سلامت دانیاسور
            self.game_over()


    def on_update(self , delta_time): # تمام منطق بازی
        
        self.end_time = time.time()

        self.me.update_animation()

        if self.start_game_flag:

            self.my_physics_engine.update()

            self.me.center_x = SCREEN_WIDTH // 3 # محل قرار گیری دانیاسور

            if self.end_time - self.cactus_time > 5: # فاصله زمانی بین ایجاد دو کاکتوس
                new_cactus = Cactus(SCREEN_WIDTH, SCREEN_HEIGHT, self.cactus_speed)
                self.cactus_list.append(new_cactus)
                self.cactus_time = time.time()

            if self.end_time - self.game_time > 10: # فاصله زمانی بین روز و شب شدن
                if self.background_color == arcade.color.WHITE:
                    self.day_flag = False
                    self.background_color = arcade.color.BLACK
                    self.game_time = time.time()
                elif self.background_color == arcade.color.BLACK:
                    self.day_flag = True
                    self.background_color = arcade.color.WHITE
                    self.game_time = time.time()

            if self.end_time - self.start_time > 0.003: # افزایش امتیاز
                self.me.score += 1
                self.start_time = time.time()

            if self.me.score > 1000: # امتیاز بیشتر از 1000
                if self.end_time - self.bird_time > 8: # فاصله بین ایجاد تو پرنده
                    new_bird = Bird(SCREEN_WIDTH, SCREEN_HEIGHT, self.bird_speed)
                    self.bird_list.append(new_bird)
                    self.bird_time = time.time()
                    self.cactus_time = time.time()
                    self.cactus_speed += 0.01  # افزایش سرعت به صورت تدریجی
                    self.bird_speed += 0.01

            for cloud in self.cloud_list: # ایجاد ابر
                cloud.update()
                if cloud.center_x < 0:
                    self.cloud_list.remove(cloud)
                    new_cloud = Cloud(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.cloud_list.append(new_cloud)
            
            if self.moon.center_x < 0: # ایجاد ماه
                self.moon.center_x = SCREEN_WIDTH
            self.moon.update()

            for ground in self.ground_list: # ایجاد زمین
                if ground.center_x < 0:
                    self.ground_list.remove(ground)
                    new_ground = Ground(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.ground_list.append(new_ground)
            
            for cactus in self.cactus_list: # ایجاد کاکتوس
                cactus.update()
                if cactus.center_x < 0 :
                    self.cactus_list.remove(cactus)

            for bird in self.bird_list: # ایجاد پرنده
                bird.update_animation()
                bird.update()
                if bird.center_x < 0:
                    self.bird_list.remove(bird)

            for cactus in self.cactus_list: # چک کردن برخورد دانیاسور با کاکتوس 
                if arcade.check_for_collision(self.me, cactus):
                    self.me.health_flag = False
                    self.start_game_flag = False
                    self.cactus_list.remove(cactus)
                    arcade.play_sound(arcade.sound.Sound(':resources:sounds/error1.wav'))

            for bird in self.bird_list: # چک کردن برخورد پنده با دانیاسور
                if arcade.check_for_collision(self.me, bird):
                    self.me.health_flag = False
                    self.start_game_flag = False
                    self.bird_list.remove(bird)
                    arcade.play_sound(arcade.sound.Sound(':resources:sounds/error1.wav'))


game = Game()
arcade.run() 