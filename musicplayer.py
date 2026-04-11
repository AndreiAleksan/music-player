import pygame
pygame.mixer.init()
notes = {
    "C" : pygame.mixer.Sound("notes/A3.wav"),
    "D" : pygame.mixer.Sound("notes/D3.wav"),
    "E" : pygame.mixer.Sound("notes/E3.wav"),
    "F" : pygame.mixer.Sound("notes/F3.wav"),
    "G" : pygame.mixer.Sound("notes/G3.wav"),
    "A" : pygame.mixer.Sound("notes/A3.wav"),
    "B" : pygame.mixer.Sound("notes/B3.wav")
}

file_name = input("Please input the path of the text file you wish to play \n")