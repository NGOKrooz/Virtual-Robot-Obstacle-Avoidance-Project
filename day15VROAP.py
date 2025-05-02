import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Robot Simulator")
clock = pygame.time.Clock()

# Wall definition (more complex map)
walls =[
    pygame.Rect(100, 100, 600, 20),
    pygame.Rect(100, 480, 600, 20),
    pygame.Rect(100, 100, 20, 400),
    pygame.Rect(680, 100, 20, 400), 
    pygame.Rect(300, 200, 200, 20),
    pygame.Rect(300, 300, 20, 100) 
]

# Grid config
grid_color = (50, 50, 50)
grid_size = 40

# Game loop
running = True
while running:
    screen.fill((30, 30, 30))

     # Draw grid
    for x in range(0, 800, grid_size):
        pygame.draw.line(screen, grid_color, (x, 0), (x, 600))
    for y in range(0, 600, grid_size):
        pygame.draw.line(screen, grid_color, (0, y), (800, y))
    

    # Draw walls
    for wall in walls:
        pygame.draw.rect(screen, (100, 100, 100), wall)


    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.display.flip()    
    clock.tick(60)    

pygame.quit()       