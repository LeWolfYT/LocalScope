import pygame as pg
pg.init()
pg.display.set_mode((100, 100))
one = pg.image.load("/Volumes/ExtraStorage/0t.png").convert_alpha()
twc = pg.image.load("/Volumes/ExtraStorage/0wc.png").convert_alpha()
al = pg.Surface((256, 256), pg.SRCALPHA)
al.fill((255, 255, 255, round(255/4*3)))
twc.blit(al, special_flags=pg.BLEND_RGBA_MULT)
one.blit(twc, (0, 0))
pg.image.save(one, "/Volumes/ExtraStorage/0ww.png")