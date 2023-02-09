import pygame
import numpy as np

WIDTH = 800
HEIGHT = 800

BLACK = 0, 0, 0
WHITE = 255, 255, 255        

class Cube:
    def __init__(self, pos: np.ndarray, a: float) -> None:
        self.pos = pos
        self.angle = np.pi/4

        self.centerOffset = np.array([-a/2,-a/2,-a/2])

        self.edges = np.array([
            np.array([np.array([0,0,0]), np.array([a,0,0])]),
            np.array([np.array([a,0,0]), np.array([a,a,0])]),
            np.array([np.array([a,a,0]), np.array([0,a,0])]),
            np.array([np.array([0,a,0]), np.array([0,0,0])]),

            np.array([np.array([0,0,0]), np.array([0,0,a])]),
            np.array([np.array([a,a,0]), np.array([a,a,a])]),
            np.array([np.array([a,0,0]), np.array([a,0,a])]),
            np.array([np.array([0,a,0]), np.array([0,a,a])]),

            np.array([np.array([0,0,a]), np.array([a,0,a])]),
            np.array([np.array([a,0,a]), np.array([a,a,a])]),
            np.array([np.array([a,a,a]), np.array([0,a,a])]),
            np.array([np.array([0,a,a]), np.array([0,0,a])]),
        ])

    def draw(self, screen: pygame.surface.Surface, rotationRate: float) -> None:
        rotated_cube = np.add(self.edges, self.centerOffset)

        rotation_matrix_x = np.array([
            [1, 0, 0],
            [0, np.cos(self.angle), -np.sin(self.angle)],
            [0, np.sin(self.angle), np.cos(self.angle)]
        ])
        rotation_matrix_y = np.array([
            [np.cos(self.angle), 0, np.sin(self.angle)],
            [0, 1, 0],
            [-np.sin(self.angle), 0, np.cos(self.angle)]
        ])
        rotation_matrix_z = np.array([
            [np.cos(self.angle), -np.sin(self.angle), 0],
            [np.sin(self.angle), np.cos(self.angle), 0],
            [0, 0, 1],
        ])
        
        rotated_cube = np.matmul(rotated_cube, rotation_matrix_x)
        rotated_cube = np.matmul(rotated_cube, rotation_matrix_y)
        rotated_cube = np.matmul(rotated_cube, rotation_matrix_z)

        print(rotated_cube[11][1][2])
        moved_cube = np.add(self.pos, rotated_cube)

        for edge in moved_cube:
            color = WHITE
            
            start_pos = edge[0][0], edge[0][1]
            end_pos = edge[1][0], edge[1][1]
            pygame.draw.line(screen, color, start_pos, end_pos)

        self.angle += rotationRate


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Spinning Cube")

    cube = Cube(np.array([400, 400, 200]), 200)

    running = True
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        cube.draw(screen, 0.001)


        pygame.display.flip()

if __name__ == "__main__":
    main()