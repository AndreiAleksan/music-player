import pygame
import time

pygame.mixer.init()

notes = {
    "C" : pygame.mixer.Sound("notes/C3.wav"),
    "D" : pygame.mixer.Sound("notes/D3.wav"),
    "E" : pygame.mixer.Sound("notes/E3.wav"),
    "F" : pygame.mixer.Sound("notes/F3.wav"),
    "G" : pygame.mixer.Sound("notes/G3.wav"),
    "A" : pygame.mixer.Sound("notes/A3.wav"),
    "B" : pygame.mixer.Sound("notes/B3.wav"),
}


print("Hello! Please input the path of the text file you wish to play.")
file_path = input("But remember, for it to work, it must only contain notes, or a '-' pause character!\n ")


with open(file_path, "r") as file:
    read_file = file.read().upper()


for character in read_file:

    if character in notes:
        notes[character].play()
        time.sleep(0.3)

    elif character == '-':
        time.sleep(0.5)