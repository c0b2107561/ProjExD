import pygame as pg
from pygame.locals import *
import random
from random import randint


#画面サイズの設定（
WIDTH = 1200
HEIGHT = int(WIDTH * 0.7)

#色の設定
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 20, 40)
YELLOW = (250, 200, 0)
SKYBLUE = (0,50,150)

#フォントの設定
font_name = pg.font.match_font('MSゴシック')

#テキスト描画用の関数（別のゲームなどでも使いまわしできます）
def draw_text(screen,text,size,x,y,color):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface,text_rect)

#バックグラウンドクラス
class Background:
    def __init__(self):
        #画像をロードしてtransformでサイズ調整（画面サイズに合わせる）
        self.image = pg.image.load('ex06/fig/pg_bg.jpg').convert_alpha()
        self.image = pg.transform.scale(self.image,(WIDTH,HEIGHT))
        #画面のスクロール設定
        self.scroll = 0
        self.scroll_speed = 4
        self.x = 0
        self.y = 0
        #0と画面横サイズの二つをリストに入れておく
        self.imagesize = [0,WIDTH]

    #描画メソッド
    def draw_BG(self,screen): 
        #for文で２つの位置に１枚づつバックグラウンドを描画する（描画するx位置は上で指定したimagesizeリスト）
        for i in range(2):      
            screen.blit(self.image,(self.scroll + self.imagesize[i], self.y))
        self.scroll -= self.scroll_speed
        #画像が端まで来たら初期位置に戻す
        if abs(self.scroll) > WIDTH:
            self.scroll = 0

#こうかとんクラス
class Koukaton(pg.sprite.Sprite):
    def __init__(self,x,y):
        #スプライトクラスの初期化
        pg.sprite.Sprite.__init__(self)

        self.imgs = []
        for i in range(1,3):
            num = str(i)
            # if len(num) == 1:
            #     num = "0" + num   
            img = pg.image.load(f'ex06/fig/{num}.png').convert_alpha()         
            img = pg.transform.scale(img,(200,200))
            self.imgs.append(img)        
        
        #描画する画像を指定するための設定
        self.index = 0
        self.image = self.imgs[self.index]

        # self.imgs.set_colorkey(SKYBLUE)
        #画像のrectサイズを取得
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        #radiusは当たり判定の設定に必要
        self.radius = 40
        
        #現在の状態をture,falseで管理
        self.IDLE = True
        self.SHOT = False
        self.DEAD = False
        self.READY = False
        self.IMMORTAL = False

        self.dy = 20
        #無敵時間の設定 
        self.immortal_timer = 60

        #残機イメージの関連（左上に表示される）
        self.kkt_mini_img = pg.image.load('ex06/fig/0.png').convert_alpha()
        #サイズ調整で小さくする
        self.kkt_mini_img = pg.transform.scale(self.kkt_mini_img,(50,35))
        self.kkt_mini_img.set_colorkey((255,255,255))
        self.lives = 3
    
    #残機描画用メソッド      
    def draw_lives(self,screen,x,y):
        for i in range(self.lives):
            img_rect = self.kkt_mini_img.get_rect()
            img_rect.x = x + 55 * i
            img_rect.y = y
            screen.blit(self.kkt_mini_img,img_rect)

    
    #弾丸発射キーを押した場合に後に作成する弾丸クラスがインスタンス化される
    def create_fireball(self):
        return Fireball(self.rect.center[0] + 20,self.rect.center[1] + 20)

    #毎フレームの処理用メソッド
    def update(self):

        #キー操作関連
        key = pg.key.get_pressed()
        #墜落している状態で無ければ以下の入力を受け付ける
        if self.DEAD == False:
            #上下左右の移動
            if key[pg.K_a]:
                self.rect.x -= 10
                if self.rect.x <= 0: 
                    self.rect.x = 0 

            if key[pg.K_d]: 
                self.rect.x += 10 
                if self.rect.x >= WIDTH - 75:
                    self.rect.x = WIDTH - 75

            if key[pg.K_w]:
                self.rect.y -= 10
                if self.rect.y <= 0: 
                    self.rect.y = 0 

            if key[pg.K_s]: 
                self.rect.y += 10 
                if self.rect.y >= HEIGHT - 75:
                    self.rect.y = HEIGHT - 75

        #墜落中の場合、斜め下に移動していく
        if self.DEAD:
            self.rect.x += 3
            self.rect.y += 10 
      

### ファイヤーボールクラス
class Fireball(pg.sprite.Sprite):

    def __init__(self, name, battery, enemies):
        pg.sprite.Sprite.__init__(self)
 
        ### ファイル読み込み
        self.image = pg.image.load(name).convert()
 
        ### 画像サイズ変更
        self.image = pg.transform.scale(self.image, (150,150))
        self.image = pg.transform.rotozoom(self.image, 90, 0.5)
 
        ### ファイヤーボールオブジェクト生成
        self.rect = self.image.get_rect()
 
        ### 他オブジェクト保存
        self.battery = battery
        self.enemy = enemies
 
        ### ミサイル初期位置
        self.rect.centerx = self.battery.rect.centerx
        self.rect.bottom  = self.battery.rect.top
 
    ### ファイヤーボール移動
    def update(self, surface):
 
        ### ファイヤーボール速度
        self.rect.centery -= 20
 
        ### 命中判定
        enemy_list = pg.sprite.spritecollide(self, self.enemy, True)
 
        ### 命中した場合、画面にHITを表示
        if len(enemy_list) > 0:
            font = pg.font.Font(None, 25)
            text = font.render("HIT", True, (96,255,96))
            surface.blit(text, [171,182])
            pg.display.update()
            pg.time.wait(400)
 
        ### 命中したか画面外に出た場合、ミサイルを消去
        if len(enemy_list) > 0 or self.rect.top < 0:
            self.kill()
# #弾丸クラス                      
# class Bullet(pg.sprite.Sprite):
#     def __init__(self,x,y):
#         #スプライトクラスの初期化
#         pg.sprite.Sprite.__init__(self)

#         #イメージを空のリストに格納
#         self.bullet_images = []
#         for i in range(1,6):
#             img = pg.image.load(f'ex06/Bullet/{i}.png').convert_alpha()
#             img = pg.transform.scale(img,(30,30))
#             self.bullet_images.append(img)
        
#          #描画する画像を指定するための設定
#         self.index = 0
#         self.image = self.bullet_images[self.index]
#         self.rect = self.image.get_rect()
#         self.rect.center = [x,y]        
        
#     #毎フレームの処理用メソッド   
#     def update(self):        
#         self.rect.x += 40
#         #位置が右端までいった場合の処理（killで自分自身をスプライトグループから削除する）
#         if self.rect.x >= WIDTH:
#             self.kill() 

#         #毎フレーム画像を切り替える処理
#         self.index += 1
#         if self.index >= len(self.bullet_images):
#             self.index = 0
#         self.image = self.bullet_images[self.index]


class Enemy(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
 
        ### ファイル読み込み
        self.image = pg.image.load(f'ex06/fig/enemy1.png').convert_alpha()
 
        ### 画像サイズ変更
        self.imagesize = [(244,192),(208,169)]
        random_num = random.choice(self.imagesize)
        self.image = pg.transform.scale(self.image, random_num)
        self.image = pg.transform.rotozoom(self.image, 0, 1.0)
 
        ### エネミーオブジェクト生成
        self.rect = self.image.get_rect()
 
        ### エネミー初期位置
        self.dx = random.randint(1,15)
        self.dy = random.randint(-6,6)
        # self.dy = 0
    
    ### エネミー移動
    def update(self):
 
        ### エネミー速度
        self.rect.centerx += random.randint(2,4)
 
        ### 画面外に出たら消去
        self.rect.x -= self.dx
        self.rect.y -= self.dy
        #move範囲
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.dy *= -1 

        if self.rect.right < 0:
            self.rect.x = WIDTH
        


#ゲームクラス（メイン処理のクラス）
class Game():
    def __init__(self) -> None:
        #pygameの初期化
        pg.init()
        #サウンドミキサーの初期化
        #クロック/FPS設定
        self.clock = pg.time.Clock()
        # self.fps = 30       

        #画面設定
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption('PlaneGame')
        #マウスのポインターを削除
        pg.mouse.set_visible(False)


        #BGインスタンス化
        self.BG = Background()

        #プレイヤーインスタンス化
        self.kkt_group = pg.sprite.Group()
        self.kkt = Koukaton(150, HEIGHT/ 2)
        self.kkt_group.add(self.kkt)
        
        #弾丸関連インスタンス化
        self.fireball_group = pg.sprite.Group()        
        self.explo_group = pg.sprite.Group()       
        
        #モブ１インスタンス化        
        self.enemy_group = pg.sprite.Group()
        for i in range(10):
            self.enemy = Enemy(WIDTH * 2,randint(100,800))
            self.enemy_group.add(self.enemy)    

           
        #スコア
        self.score = 0
        self.hiscore = 0

        #フラグ
        self.BOSS_appear = False
        self.game_over = False
        self.game_clear = False
        self.game_start = True

    #スタート画面の描画用メソッド
    def game_start_screen(self):
        draw_text(self.screen,"ENTERを押してゲームスタート!", 70, WIDTH / 2, HEIGHT - 500, BLACK)
        draw_text(self.screen,"ESCAPE(終了)", 50, WIDTH / 2, HEIGHT - 400, BLACK)
        # draw_text(self.screen,"BULLET: mouse left click", 50, WIDTH / 2, HEIGHT - 300, BLACK)
        # draw_text(self.screen,"MOVE: WASD key", 50, WIDTH / 2, HEIGHT - 200, BLACK)


    #GAMEOVER画面の描画用メソッド
    def game_over_screen(self):
        draw_text(self.screen,"Game Over", 100, WIDTH / 2, HEIGHT / 2, RED)
        draw_text(self.screen,"SPACEを押してリスタート!", 36, WIDTH / 2, HEIGHT - 200, BLACK)
    
    #GAMECLEAR画面の描画用メソッド
    def game_clear_screen(self):
        draw_text(self.screen,"Congratulations!", 100, WIDTH / 2, HEIGHT / 4, YELLOW)
        if self.hiscore < self.score:
            self.hiscore = self.score
        draw_text(self.screen,f"SCORE : {self.score}", 40, WIDTH / 2, int(HEIGHT * 0.4), BLACK)
        draw_text(self.screen,f"HISCORE : {self.hiscore}", 36, WIDTH / 2, int(HEIGHT * 0.5), BLACK)
        draw_text(self.screen,"Press ENTER KEY TO RESTART", 36, WIDTH / 2, int(HEIGHT * 0.8), BLACK)
        draw_text(self.screen,"Press ESCAPE KEY TO EXIT", 36, WIDTH / 2, int(HEIGHT * 0.85), BLACK)
    
    def collide(self, character, opponent):
        if isinstance(character, Koukaton) and isinstance(opponent, Enemy):
            if character.isTrampling(opponent):
                opponent.defeated()
            else:
                character.defeated()
        elif isinstance(character, Enemy) and isinstance(opponent, Koukaton):
            if opponent.isTrampling(character):
                character.defeated()
            else:
                character.defeated()
    #メインループ
    def main(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.fireball_group.add(Fireball("ex05/fig/fireball.png", self.kkt_group, self.enemy_group))

                #キー入力の受付
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                    if self.game_start:
                        if event.key == K_RETURN:
                            self.game_start = False


                    #リスタート処理  gameover時　色々初期値に戻す
                    if event.key == pg.K_SPACE:
                        if self.kkt.lives == 0:
                            #emptyでグループを空にする
                            self.enemy_group.empty()
                            # self.boss_group.empty()
                            # self.BOSS_appear = False
                            self.game_over = False
                            self.kkt.IMMORTAL = False
                            self.kkt.lives = 3
                            self.score = 0
                            #プレイヤーのインスタンス化
                            self.kkt = Koukaton(50,HEIGHT / 10)
                            self.kkt_group.add(self.kkt)
                            #self.BGM.play(-1)

                            
                            #モブどものインスタンス化
                            for i in range(10):
                                self.enemy = Enemy(WIDTH,random.randint(100,800))
                                self.enemy_group.add(self.enemy)
                            
                    #リスタート処理　gameClear時
                    if event.key == K_RETURN:
                        if self.game_clear:
                            self.game_clear = False
                            self.kkt_group.empty()
                            # self.boss_group.empty()
                            # self.BOSS_appear = False
                            
                            self.kkt.lives = 3
                            self.score = 0

                            #登場キャラクターのインスタンス化
                            self.kkt =Koukaton(150,HEIGHT / 2)
                            self.kkt_group.add(self.kkt)
                                                        
                            # self.boss = Boss(WIDTH - 1, HEIGHT / 4)
                            # self.boss_group.add(self.boss)
                            
                            for i in range(10):
                                self.enemy = Enemy(WIDTH,random.randint(150,int(HEIGHT - 150) ))
                                self.enemy_group.add(self.enemy)
                            
                #弾丸発射キー操作
                if self.game_clear == False and self.game_start == False:
                    if event.type == MOUSEBUTTONDOWN:
                        if self.kkt.DEAD == False:
                            self.kkt.SHOT,self.kkt.IDLE  = True,False
                            self.fireball_group.add(self.kkt.create_fireball())
                            # self.shoot_sound.play()
                    
                    #マウスボタンを放した時の処理  
                    if event.type == MOUSEBUTTONUP:
                        if self.kkt.DEAD == False:             
                            self.kkt.IDLE,self.kkt.SHOT = True,False
                            self.fireball_READY = True
                            # self.shoot_sound.stop()
                    
                   
            #バックグラウンド表示
            self.BG.draw_BG(self.screen)
            if self.game_start:
                self.game_start_screen()
                # self.kkt_group.draw(self.screen)
            #残機表示
            if self.game_start == False:
                self.kkt.draw_lives(self.screen,20,30)
                self.kkt_group.draw(self.screen)

                #モブキャラ表示
                self.enemy_group.draw(self.screen)
                #爆破描画 
                # self.explo_group.draw(self.screen)
                #各クラスアップデートメソッド実行
                self.kkt_group.update()
                self.fireball_group.update()            
                self.enemy_group.update()          
                # self.mob2_group.update()          
                self.explo_group.update()            
                                                
                #プレイヤーとモブの接触時処理
                if self.kkt.DEAD == False and self.kkt.IMMORTAL == False:
                    enemy_collision =  pg.sprite.groupcollide(self.kkt_group,self.enemy_group,False,True)
                    for collision in enemy_collision:                
                        self.kkt.DEAD = True
                        self.kkt.IDLE, self.kkt.SHOT, self.fireball_READY = False, False, False
                        # self.explo = Explosion(collision.rect.x,collision.rect.y)
                        # self.explo_group.add(self.explo)
                        self.kkt.lives -= 1
                    
                #プレイヤー死亡時処理
                if self.kkt.DEAD == True:
                    if self.kkt.rect.top >= HEIGHT:
                        if self.kkt.lives == 0:
                            self.kkt.kill()
                            self.game_over = True     
                        else:
                            self.kkt.IDLE = True
                            self.kkt.DEAD = False
                            self.kkt.rect.x = 100
                            self.kkt.rect.y = HEIGHT / 2
                            # self.BGM.play(-1)
                            self.kkt.IMMORTAL = True
                
                #モブキャラと弾丸のヒット時の処理
                enemyhits = pg.sprite.groupcollide(self.enemy_group,self.fireball_group,True,True)
                if enemyhits:
                    self.score += 100
                    # self.hit_sound.play()


                #モブ弾丸/ヒット時の処理
                for hit in enemyhits:
                    if self.score <= 5000:               
                        self.enemy = Enemy(WIDTH,random.randint(100,800))
                        self.enemy_group.add(self.mob)
                        # self.explo = Explosion(hit.rect.x,hit.rect.y)
                        # self.explo_group.add(self.explo)
                    # else:
                        # self.explo = Explosion(hit.rect.x,hit.rect.y)
                        # self.explo_group.add(self.explo)



                #スコア表示              
                draw_text(self.screen, f'SCORE: {str(self.score)}', 50, WIDTH / 2, 10, BLACK)
                draw_text(self.screen, f'HISCORE: {str(self.hiscore)}', 50, WIDTH - 140, 10, BLACK)
                
                #GAMEOVER　
                if self.game_over:
                    self.game_over_screen()
                
                #GAME CLEAR
                if self.game_clear:
                    self.enemy_group.empty()  
                    # self.mob2_group.empty()               
                    self.kkt.IMMORTAL =True
                    self.game_clear_screen()
                
                #無敵時間カウンター   
                # if self.game_clear == False:
                #     if self.plane.IMMORTAL:
                #         self.plane.immortal_timer -= 1
                #     if self.plane.immortal_timer <= 0:
                #         self.plane.IMMORTAL = False
                #         self.plane.immortal_timer = 60

            #FPS設定
            # self.clock.tick(self.fps)
                
            pg.display.update()
        pg.quit()

game = Game()

game.main()