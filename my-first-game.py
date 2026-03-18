import pygame
import sys
import random
import time

pygame.init()

# 해상도
WIDTH = 1200
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Game")

# 색상
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)
big_font = pygame.font.SysFont(None, 120)

# 상태
game_state = "start"

# 플레이어
player_radius = 40
player_speed = 10

def reset_game():
    return {
        "player_x": WIDTH // 2,
        "lives": 3,
        "score": 0,
        "enemies": [],
        "start_time": time.time()
    }

game = reset_game()

player_y = HEIGHT - 80
enemy_radius = 25

# 적 생성
def spawn_enemy():
    return {
        "x": random.randint(0, WIDTH),
        "y": 0,
        "speed": random.uniform(4, 8)
    }

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == "start":
                if event.key == pygame.K_SPACE:
                    game = reset_game()
                    game_state = "play"

            elif game_state == "game_over":
                if event.key == pygame.K_r:
                    game = reset_game()
                    game_state = "start"

    keys = pygame.key.get_pressed()

    # ---------------- 플레이 ----------------
    if game_state == "play":
        # 이동
        if keys[pygame.K_LEFT]:
            game["player_x"] -= player_speed
        if keys[pygame.K_RIGHT]:
            game["player_x"] += player_speed

        # 화면 제한
        if game["player_x"] < player_radius:
            game["player_x"] = player_radius
        if game["player_x"] > WIDTH - player_radius:
            game["player_x"] = WIDTH - player_radius

        # 시간
        elapsed_time = int(time.time() - game["start_time"])

        # 적 증가
        if len(game["enemies"]) < 1 + elapsed_time // 5:
            game["enemies"].append(spawn_enemy())

        # 적 이동 + 충돌
        for enemy in game["enemies"]:
            enemy["y"] += enemy["speed"]

            # 바닥 도달
            if enemy["y"] > HEIGHT:
                enemy["y"] = 0
                enemy["x"] = random.randint(0, WIDTH)
                game["score"] += 1

            # 충돌
            dx = game["player_x"] - enemy["x"]
            dy = player_y - enemy["y"]
            distance = (dx**2 + dy**2) ** 0.5

            if distance < player_radius + enemy_radius:
                game["lives"] -= 1
                enemy["y"] = 0
                enemy["x"] = random.randint(0, WIDTH)

                if game["lives"] <= 0:
                    game_state = "game_over"

    # ---------------- 화면 ----------------
    screen.fill(WHITE)

    if game_state == "start":
        title = big_font.render("DODGE GAME", True, BLUE)
        start_text = font.render("Press SPACE to Start", True, BLACK)

        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 150))
        screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2 + 20))

    elif game_state == "play":
        # 플레이어
        pygame.draw.circle(screen, BLUE, (int(game["player_x"]), player_y), player_radius)

        # 적
        for enemy in game["enemies"]:
            pygame.draw.circle(screen, RED, (int(enemy["x"]), int(enemy["y"])), enemy_radius)

        # UI
        elapsed_time = int(time.time() - game["start_time"])

        score_text = font.render(f"Score: {game['score']}", True, BLACK)
        lives_text = font.render(f"Lives: {game['lives']}", True, BLACK)
        time_text = font.render(f"Time: {elapsed_time}s", True, BLACK)

        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (20, 80))
        screen.blit(time_text, (20, 140))

    elif game_state == "game_over":
        over_text = big_font.render("GAME OVER", True, RED)
        score_text = font.render(f"Score: {game['score']}", True, BLACK)
        time_text = font.render(f"Time: {int(time.time() - game['start_time'])}s", True, BLACK)
        restart_text = font.render("Press R to Restart", True, BLACK)

        screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 150))
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 + 20))
        screen.blit(time_text, (WIDTH//2 - time_text.get_width()//2, HEIGHT//2 + 80))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 160))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()