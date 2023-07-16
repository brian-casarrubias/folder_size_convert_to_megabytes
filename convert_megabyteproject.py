
import pyautogui, win32api, win32con, keyboard, time, random, re, copy, pprint, os, shutil, send2trash, pygame, logging, traceback

# Megabytes = Bytes / (1024 * 1024)


FILE_PATH = 'C:\\Users\\Brian\\Desktop\\audio-game'

megabytes = 0


for song in os.listdir(FILE_PATH):
    megabytes += os.path.getsize(os.path.join(FILE_PATH, song))

convert_to_megabytes = megabytes / (1024 * 1024)
print(megabytes)
print(f'{convert_to_megabytes:.2f}mb')