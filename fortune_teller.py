import pygame
import os
import random
from time import sleep
pygame.init()
pygame.mixer.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 1024
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
image_folder = "images"
image_files = [
    os.path.join(image_folder, "0.jpg"),
    os.path.join(image_folder, "1.jpg"),
    os.path.join(image_folder, "2.jpg"),
    os.path.join(image_folder, "3.jpg"),
    os.path.join(image_folder, "4.jpg"),
    os.path.join(image_folder, "5.jpg"),
]
images = [pygame.image.load(file) for file in image_files]
image_index = 0
image_timer = pygame.time.get_ticks()
clock = pygame.time.Clock()
running = True
image_sequence_running = True

audio_folder = "audio"
audio_files = [
    os.path.join(audio_folder, "0.mp3"),
    os.path.join(audio_folder, "1.mp3"),
    os.path.join(audio_folder, "2.mp3"),
    os.path.join(audio_folder, "3.mp3"),
    os.path.join(audio_folder, "4.mp3"),
]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                image_sequence_running = False
    if image_sequence_running:
        if pygame.time.get_ticks() - image_timer > 1000:
            image_index = (image_index + 1) % len(images)
            image_timer = pygame.time.get_ticks()
        screen.fill((0, 0, 0))
        current_image = images[image_index]
        screen.blit(current_image, ((SCREEN_WIDTH - current_image.get_width()) // 2, (SCREEN_HEIGHT - current_image.get_height()) // 2))
    pygame.display.flip()
    if not image_sequence_running:
        random_audio_file = random.choice(audio_files)
        pygame.mixer.music.load(random_audio_file)
        pygame.mixer.music.play()
        sleep(7)
        pygame.mixer.music.stop()
        image_sequence_running = True
pygame.quit()