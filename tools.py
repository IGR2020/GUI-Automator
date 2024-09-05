import pygame as pg

pg.font.init()


def blit_text(
    win,
    text,
    pos,
    colour=(0, 0, 0),
    size=30,
    font="arialblack",
    blit=True,
    centerx=False,
    centery=False,
    center=False,
):
    text = str(text)
    x, y = pos
    font_style = pg.font.SysFont(font, size)
    text_surface = font_style.render(text, True, colour)
    if center:
        x -= text_surface.get_width() // 2
        y -= text_surface.get_height() // 2
    else:
        if centerx:
            x -= text_surface.get_width() // 2
        if centery:
            y -= text_surface.get_height() // 2
    if blit:
        win.blit(text_surface, (x, y))
    return text_surface