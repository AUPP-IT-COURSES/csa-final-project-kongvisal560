import pygame
import random



screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Slot Machine")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.Font(None, 32)

symbol_images = {
    "A": pygame.image.load("A.png"),
    "B": pygame.image.load("B.png"),
    "C": pygame.image.load("C.png"),
    "D": pygame.image.load("D.png"),
}


def deposit():
    while True:
        amount_text = font.render("Enter deposit amount: ", True, WHITE)
        amount_rect = amount_text.get_rect(center=(400, 300))
        screen.fill(BLACK)
        screen.blit(amount_text, amount_rect)
        pygame.display.flip()

        amount_input = pygame.event.wait()
        if amount_input.type == pygame.KEYDOWN and amount_input.key == pygame.K_RETURN:
            amount_str = amount_input.unicode
            if amount_str.isdigit() and int(amount_str) > 0:
                break
            else:
                error_text = font.render("Invalid amount. Please enter a valid number.", True, RED)
                error_rect = error_text.get_rect(center=(400, 350))
                screen.blit(error_text, error_rect)
                pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    amount = int(amount_str)
    return amount


def get_number_of_lines():
    while True:
        lines_text = font.render("Enter number of lines: ", True, WHITE)
        lines_rect = lines_text.get_rect(center=(400, 300))
        screen.fill(BLACK)
        screen.blit(lines_text, lines_rect)
        pygame.display.flip()

        lines_input = pygame.event.wait()
        if lines_input.type == pygame.KEYDOWN and lines_input.key == pygame.K_RETURN:
            lines_str = lines_input.unicode
            if lines_str.isdigit() and 1 <= int(lines_str) <= MAX_LINES:
                break
            else:
                error_text = font.render("Invalid number of lines. Please enter a valid number between 1 and 3.", True, RED)
                error_rect = error_text.get_rect(center=(400, 350))
                screen.blit(error_text, error_rect)
                pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    lines = int(lines_str)
    return lines


def get_bet():
    while True:
        bet_text = font.render("Enter bet amount: ", True, WHITE)
        bet_rect = bet_text.get_rect(center=(400, 300))
        screen.fill(BLACK)
        screen.blit(bet_text, bet_rect)
        pygame.display.flip()

        bet_input = pygame.event.wait()
      

