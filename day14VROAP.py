import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

walls = [pygame.Rect(300, 100, 200, 20), pygame.Rect(100, 400, 400, 20), pygame.Rect(700, 200, 20, 200)]

running = True
while running:
    screen.fill((30, 30, 30))
    
    for wall in walls:
        pygame.draw.rect(screen, (100, 100, 100), wall)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.display.flip()    
    clock.tick(60)    

pygame.quit()       