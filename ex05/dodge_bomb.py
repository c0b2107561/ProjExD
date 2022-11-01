### インポート
import sys
import time
import random
from random import randint
import pygame
from pygame.locals import * 


### 砲台クラス
class Battery(pygame.sprite.Sprite):

    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
 
        ### ファイル読み込み
        self.image = pygame.image.load(name).convert_alpha()
 
        ### 画像サイズ変更
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.image = pygame.transform.rotozoom(self.image, 90, 1.0)
 
        ### 砲台オブジェクト生成
        self.rect = self.image.get_rect()
 
        ### 砲台位置
        self.rect.centerx = int(SURFACE.width / 2)
        self.rect.centery = SURFACE.bottom - BTY_H_POS
 
    ### 砲台描画
    def draw(self, surface):
        surface.blit(self.image, self.rect)
 
### ファイヤーボールクラス
class Fireball(pygame.sprite.Sprite):

    def __init__(self, name, battery, enemies):
        pygame.sprite.Sprite.__init__(self)
 
        ### ファイル読み込み
        self.image = pygame.image.load(name).convert()
 
        ### 画像サイズ変更
        self.image = pygame.transform.scale(self.image, (150,150))
        self.image = pygame.transform.rotozoom(self.image, 90, 0.5)
 
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
        self.rect.centery -= MSL_SPD
 
        ### 命中判定
        enemy_list = pygame.sprite.spritecollide(self, self.enemy, True)
 
        ### 命中した場合、画面にHITを表示
        if len(enemy_list) > 0:
            font = pygame.font.Font(None, FONT_SIZE)
            text = font.render("HIT", True, (96,255,96))
            surface.blit(text, [171,182])
            pygame.display.update()
            pygame.time.wait(MES_TIME)
 
        ### 命中したか画面外に出た場合、ミサイルを消去
        if len(enemy_list) > 0 or self.rect.top < 0:
            self.kill()
 

### エネミークラス
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
 
        ### ファイル読み込み
        self.image = pygame.image.load(name).convert()
 
        ### 画像サイズ変更
        self.image = pygame.transform.scale(self.image, (250,250))
        self.image = pygame.transform.rotozoom(self.image, 0, 0.3)
 
        ### エネミーオブジェクト生成
        self.rect = self.image.get_rect()
 
        ### エネミー初期位置
        self.rect.left = 0
        self.rect.top  = ENY_H_POS
 
    
    ### エネミー移動
    def update(self):
 
        ### エネミー速度
        self.rect.centerx += random.randint(30,60)
 
        ### 画面外に出たら消去
        if self.rect.left > SURFACE.width:
            self.kill()
 

### メイン関数 
def main():
 
    ### 画面初期化
    pygame.init()
    
    surface = pygame.display.set_mode(SURFACE.size) #クラス関数化するのが理想
    pygame.display.set_caption("頑張れ！鳥獣戯画") 
    # global scrn_sfc, scrn_rct, bg_rct
    # scrn_sfc = pygame.display.set_mode((1600,900))
    surfase_rct = surface.get_rect()

    #練習1
    bg_sfc = pygame.image.load("ex05/fig/background.png") 
    bg_sfc = pygame.transform.scale(bg_sfc,(1200,900))
    bg_rct = bg_sfc.get_rect()


    ### 砲台作成
    battery = Battery("ex05/fig/kamehameha.jpg")
 
    ### ファイヤーボールグループ
    fireball = pygame.sprite.Group()
 
    ### エネミーグループ
    enemies = pygame.sprite.Group()
 
    ### 時間オブジェクト生成
    clock = pygame.time.Clock()
 
    ### 無限ループ
    while True:
 
        ### フレームレート設定
        clock.tick(F_RATE)
 
        ### 背景色設定
        surface.fill((0,0,0))
        surface.blit(bg_sfc, bg_rct)
 
        ### エネミー出現
        if len(enemies) == 0:
            if random.randint(0,20) > 19:
                enemies.add(Enemy("ex05/fig/enemy.png"))
 
        ### スプライトを更新
        fireball.update(surface)
        enemies.update()
 
        ### スプライトを描画
        battery.draw(surface)
        fireball.draw(surface)
        enemies.draw(surface)
 
        ### 画面更新
        pygame.display.update()
        pygame.time.wait(W_TIME)
 
        ### イベント処理
        for event in pygame.event.get():
 
            ### 終了処理
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
 
                ### ファイヤーボール発射
                if event.key == K_SPACE:
                    fireball.add(Fireball("ex05/fig/fireball.png", battery, enemies))
 

### 終了関数
def exit():
    pygame.quit()
    sys.exit()
 
### メイン関数呼び出し
if __name__ == "__main__":
    ### 定数
    WIDTH      = 1200 # 画面横サイズ
    HEIGHT     = 900 # 画面縦サイズ
    BTY_W_SIZE = 50 # 砲台横サイズ
    BTY_H_SIZE = 50 # 砲台縦サイズ
    BTY_H_POS  = 50 # 砲台縦位置
    MSL_SPD    = 20 # ミサイル移動速度
    ENY_H_POS  = randint(51, HEIGHT) # エネミー縦位置
    F_RATE     = 30 # フレームレート
    W_TIME     = 10 # 待ち時間
    FONT_SIZE  = 50 # フォントサイズ
    MES_TIME   = 400 # メッセージ表示時間
 
    ### 画面定義(X軸,Y軸,横,縦)
    SURFACE = Rect(0, 0, WIDTH, HEIGHT)

    ### 処理開始
    main()
