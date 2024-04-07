import pygame
pygame.init()

# Загрузка музыкального файла
pygame.mixer.music.load('mus.mp3')

class Knopka():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        # Получаем текущее положение мыши
        pos = pygame.mouse.get_pos()
        # Проверяем, находится ли курсор мыши над кнопкой
        over_or_not = self.rect.collidepoint(pos)

        # Проверяем условия наведения мыши и нажатия кнопки
        action = False
        if over_or_not and pygame.mouse.get_pressed()[0]:
            action = True
            pygame.mixer.music.play()  # Проигрываем музыку

        # Отображаем кнопку на экране
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action
