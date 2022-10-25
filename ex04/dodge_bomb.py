import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん") #練習1
    scrn_sfc = pg.display.set_mode((1600,900))

    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg") #練習1
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("ex04/fig/6.png") #練習3
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() 
    tori_rct.center = 900,400 

    clock = pg.time.Clock() #練習1

    
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #練習2

        for event in pg.event.get(): #練習2
            if event.type == pg.QUIT:return
        
        key_stats = pg.key.get_pressed()
        if key_stats[pg.K_UP]: tori_rct.centery -=1#upの時こうかとんの座標を-1
        if key_stats[pg.K_DOWN]: tori_rct.centery +=1#downの時こうかとんの座標を+1
        if key_stats[pg.K_LEFT]: tori_rct.centerx -=1#leftの時こうかとんの座標を-1
        if key_stats[pg.K_RIGHT]: tori_rct.centerx +=1#rightの時こうかとんの座標を+1

        scrn_sfc.blit(tori_sfc, tori_rct) #練習3
        #blitの順番通りに表示される

        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()