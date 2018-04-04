import os
import time
import pygame
import requests
import constants
from color import Color


def clean_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_dots(red=False, green=False, blue=False):
    if red:
        print(Color.RED + ".", end='')

    if green:
        print(Color.GREEN + ".", end='')

    if blue:
        print(Color.BLUE + ".", end='')

    print(Color.END)


def print_loading_message():
    loading_message = Color.BOLD + Color.YELLOW + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t     " + "loading "

    print(loading_message, end='')
    print_dots(True, False, False)
    time.sleep(1)
    clean_terminal()

    print(loading_message, end='')
    print_dots(True, True, False)
    time.sleep(1)
    clean_terminal()

    print(loading_message, end='')
    print_dots(True, True, True)
    time.sleep(1)
    clean_terminal()


def load():
    clean_terminal()
    os.system('mkdir -p ~/' + constants.tmp_dir)

    if os.path.isfile(bg_sound_path):
        print(bg_sound_path)
    else:
        print('downloading song')
        req = requests.get(bg_sound_url)
        file = open(bg_sound_path, 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()
        if 'background_music.mp3' not in os.listdir(tmp_path):
            while True:
                print_loading_message()
                if 'background_music.mp3' in os.listdir(tmp_path):
                    break
        print_loading_message()
        print_loading_message()
        pygame.mixer.init(44100, -16, 2, 2048)
        pygame.mixer.music.load(bg_sound_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
