import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん") #練習1
    scrn_sfc = pg.display.set_mode((1600,900))

    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg") #練習1
    bg_rct = bg_sfc.get_rect()

    clock = pg.time.Clock() #練習1

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #練習2
        pg.display.update()

        for event in pg.event.get(): #練習2
            if event.type == pg.QUIT:return

        clock.tick(0.5)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()