import pygame
import math

# Initialize Pygame - SETUP
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Robot Simulator")
clock = pygame.time.Clock()

# Grid config
grid_color = (50, 50, 50)
grid_size = 40

# Wall definition (more complex map)
walls =[
    pygame.Rect(100, 100, 600, 20),
    pygame.Rect(100, 480, 600, 20),
    pygame.Rect(100, 100, 20, 400),
    pygame.Rect(680, 100, 20, 400), 
    pygame.Rect(300, 200, 200, 20),
    pygame.Rect(300, 300, 20, 100) 
]

robot_pos = [200, 150]
robot_angle = 0
robot_color = (0, 255, 0)

def draw_robot(pos, angle):
    pygame.draw.circle(screen, robot_color, (int(pos[0]), int(pos[1])), 10)

    # Draw direction line
    dx = math.cos(angle) * 20
    dy = math.sin(angle) * 20
    end_pos = (pos[0] + dx, pos[1] + dy)
    pygame.draw.line(screen, (255, 0, 0), pos, end_pos, 2)


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

    # Draw robot 
    draw_robot(robot_pos, robot_angle)   


    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.display.flip()    
    clock.tick(60)    

pygame.quit()       