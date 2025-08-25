from pynput import keyboard
from pynput.keyboard import Key
import pygame
import screen

# def on_key_release(key):
#     if key == Key.right:
#         print("Right key clicked")
#     elif key == Key.left:
#         print("Left key clicked")
#     elif key == Key.up:
#         print("Up key clicked")
#     elif key == Key.down:
#         print("Down key clicked")
#     elif key == Key.enter:
#         exit()
#
#
# with keyboard.Listener(on_release=on_key_release) as listener:
#     listener.join()

keepGameRunning = True
while keepGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           keepGameRunning = False
    screen.draw_screen()