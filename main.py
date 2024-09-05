import pyautogui
import pygame
import time
from tools import blit_text
import threading

window = pygame.display.set_mode((250, 200), pygame.RESIZABLE)
pygame.display.set_caption("Auto Clicker")
clock = pygame.time.Clock()
fps = 30

run = True
click = False
start_time = time.time()
max_click_time = 10

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            click = not click
            start_time = time.time()
        if event.type == pygame.QUIT:
            run = False
    if max_click_time < time.time() - start_time: click = False
    if click: threading.Thread(target=pyautogui.click, args=(None, None, 1, 0, "left")).start()
    window.fill((30, 30, 30))
    blit_text(window, f"FPS: {round(clock.get_fps())}", (0, 0), (255, 255, 255))
    pygame.display.update()