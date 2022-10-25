import tkinter as tk
import tkinter.messagebox as tkm
import pygame as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct):
    # obj_rct:こうかとんrct又は爆弾rct
    # scr_rct:スクリーンrct
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def check_bound1(obj1_rct, scr1_rct):
    # obj_rct:こうかとんrct又は爆弾rct
    # scr_rct:スクリーンrct
    yoko1, tate1 = +1, +1
    if obj1_rct.left < scr1_rct.left or scr1_rct.right < obj1_rct.right: 
        yoko1 = -1
    if obj1_rct.top < scr1_rct.top or scr1_rct.bottom < obj1_rct.bottom:
        tate1 = -1
    return yoko1, tate1

def game_over_scr():
    bg1_sfc = pg.image.load("ex04/fig/gameover.png") 
    bg1_rct = bg1_sfc.get_rect()

    button = pg.Rect(30,30,50,50)
    font = pg.font.Font(None, 100)
    text_sfc = font.render("RESTERT?", True, "RED")
    # text_rct = text_sfc.get_rect()
    running1 = True
    while running1:
        pg.draw.rect(scrn_sfc, (255, 0, 0), button)
        scrn_sfc.blit(bg1_sfc, bg_rct)
        scrn_sfc.blit(text_sfc, (550,525))

        clock = pg.time.Clock()

        pg.display.update()
        clock.tick(20)

        for event in pg.event.get(): #練習2
            if event.type == pg.QUIT:return
            if event.type == pg.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    running1 = False
                    main()


def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん") 
    global scrn_sfc, scrn_rct, bg_rct
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    #練習1
    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg") 
    bg_rct = bg_sfc.get_rect()

    #練習3
    tori_sfc = pg.image.load("ex04/fig/6.png") 
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() 
    tori_rct.center = 900,400 


    #練習5
    bomb_sfc = pg.Surface((20,20)) 
    bomb_sfc.set_colorkey((0, 0, 0)) #四隅の黒い部分の透過
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery = randint(0, scrn_rct.width), randint(0, scrn_rct.height)

    bomb1_sfc = pg.Surface((20,20)) 
    bomb1_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb1_sfc, (0, 255, 0), (10, 10), 10)
    bomb1_rct = bomb1_sfc.get_rect()
    bomb1_rct.centerx, bomb1_rct.centery = randint(0, scrn_rct.width), randint(0, scrn_rct.height) 
    
    #練習6
    vx, vy = +1, -1
    vx1, vy1 = +3, -3
    clock = pg.time.Clock() #練習1
    
    running = True
    while running:
        scrn_sfc.blit(bg_sfc, bg_rct) #練習2

        for event in pg.event.get(): #練習2
            if event.type == pg.QUIT:return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:return
        
        key_stats = pg.key.get_pressed() #練習4
        if key_stats[pg.K_UP]: tori_rct.centery -=1#upの時こうかとんの座標を-1
        if key_stats[pg.K_DOWN]: tori_rct.centery +=1#downの時こうかとんの座標を+1
        if key_stats[pg.K_LEFT]: tori_rct.centerx -=1#leftの時こうかとんの座標を-1
        if key_stats[pg.K_RIGHT]: tori_rct.centerx +=1#rightの時こうかとんの座標を+1

        yoko, tate = check_bound(tori_rct, scrn_rct) #練習7
        if yoko == -1:
            if key_stats[pg.K_LEFT]:
                tori_rct.centerx +=1
            if key_stats[pg.K_RIGHT]:
                tori_rct.centerx -=1
        if tate == -1:
            if key_stats[pg.K_UP]:
                tori_rct.centery +=1
            if key_stats[pg.K_DOWN]:
                tori_rct.centery -=1

        scrn_sfc.blit(tori_sfc, tori_rct) #練習3
        #blitの順番通りに表示される

        yoko, tate = check_bound(bomb_rct, scrn_rct) #練習7
        vx *= yoko
        vy *=tate
        bomb_rct.move_ip(vx, vy) #練習6 #vx,vyは設定してある
        scrn_sfc.blit(bomb_sfc, bomb_rct) #練習5


        yoko1, tate1 = check_bound1(bomb1_rct, scrn_rct) #練習7
        vx1 *= yoko1
        vy1 *=tate1
        bomb1_rct.move_ip(vx1, vy1)
        scrn_sfc.blit(bomb1_sfc, bomb1_rct)
        
        #練習8
        if tori_rct.colliderect(bomb_rct):
            running = False
            game_over_scr()

        if tori_rct.colliderect(bomb1_rct):
            running = False
            game_over_scr()


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()