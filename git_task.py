import pygame
import random

# --- Constante pentru configurarea aplicației ---
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_ROWS = 10
GRID_COLS = 10
CELL_WIDTH = WINDOW_WIDTH // GRID_COLS
CELL_HEIGHT = WINDOW_HEIGHT // GRID_ROWS
UPDATE_INTERVAL_MS = 5000  # 5000 milisecunde = 5 secunde

def generate_color_grid():
    """
    Generează o matrice de culori RGB aleatorii pentru grilă.
    Returnează o listă 2D (10x10) conținând tupluri (R, G, B).
    """
    grid = []
    for _ in range(GRID_ROWS):
        row = []
        for _ in range(GRID_COLS):
            # Generăm o culoare aleatorie (Red, Green, Blue) între 0 și 255
            random_color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            row.append(random_color)
        grid.append(row)
        
    return grid

def main():
    # Inițializarea modulului pygame
    pygame.init()

    # Setarea ferestrei și a titlului
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Procedural Color Grid (Regenerare automată la 5s sau SPACE)")

    # Generarea inițială a grilei de culori
    color_grid = generate_color_grid()

    # Variabilă pentru a urmări momentul ultimei regenerări
    last_update_time = pygame.time.get_ticks()

    # Variabilă de control pentru bucla principală
    running = True

    # Bucla principală a programului
    while running:
        # 1. Gestionarea evenimentelor (input de la utilizator)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Regenerare manuală la apăsarea tastei SPACE
                    color_grid = generate_color_grid()
                    last_update_time = pygame.time.get_ticks() # Resetăm cronometrul

        # 2. Logica de actualizare automată pe bază de timp
        current_time = pygame.time.get_ticks()
        if current_time - last_update_time >= UPDATE_INTERVAL_MS:
            color_grid = generate_color_grid()
            last_update_time = current_time

        # 3. Desenarea graficii
        screen.fill((0, 0, 0))  # Curățăm ecranul cu fundal negru

        for y in range(GRID_ROWS):
            for x in range(GRID_COLS):
                # Calculăm coordonatele de desenare pentru fiecare celulă
                rect_x = x * CELL_WIDTH
                rect_y = y * CELL_HEIGHT
                
                # Extragem culoarea din matrice și desenăm dreptunghiul
                cell_color = color_grid[y][x]
                pygame.draw.rect(screen, cell_color, (rect_x, rect_y, CELL_WIDTH, CELL_HEIGHT))

        # Actualizăm ecranul pentru a afișa noul cadru
        pygame.display.flip()

    # Închiderea corectă a programului la ieșirea din buclă
    pygame.quit()

# Punctul de intrare în program
if __name__ == "__main__":
    main()
