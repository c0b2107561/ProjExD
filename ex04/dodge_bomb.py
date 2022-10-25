import pygame as pg
import sys
from random import randint

def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん") 
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
    
    #練習6
    vx, vy = +1, -1

    clock = pg.time.Clock() #練習1
    
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #練習2

        for event in pg.event.get(): #練習2
            if event.type == pg.QUIT:return
        
        key_stats = pg.key.get_pressed() #練習4
        if key_stats[pg.K_UP]: tori_rct.centery -=1#upの時こうかとんの座標を-1
        if key_stats[pg.K_DOWN]: tori_rct.centery +=1#downの時こうかとんの座標を+1
        if key_stats[pg.K_LEFT]: tori_rct.centerx -=1#leftの時こうかとんの座標を-1
        if key_stats[pg.K_RIGHT]: tori_rct.centerx +=1#rightの時こうかとんの座標を+1

        scrn_sfc.blit(tori_sfc, tori_rct) #練習3
        #blitの順番通りに表示される

        bomb_rct.move_ip(vx, vy) #練習6 #vx,vyは設定してある
        scrn_sfc.blit(bomb_sfc, bomb_rct) #練習5
        
        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()