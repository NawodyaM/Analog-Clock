from calendar import calendar, month

import pygame
from math import pi,cos,sin
import datetime

WIDTH , HEIGHT = 800,800
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Digital Clock")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (173, 216, 230)
DARKBLUE = (0, 0, 139)
GRAY = (128, 128, 128)
LIGHTGRAY = (211, 211, 211)
DARKGRAY = (169, 169, 169)
CYAN = (0, 255, 255)

def numbers(number, size, position):
    font = pygame.font.SysFont("Times New Roman", size, True, False)
    text = font.render(number,True, DARKGRAY)
    text_rect = text.get_rect(center = (position))
    screen.blit(text, text_rect)

def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x +WIDTH / 2, -(y - HEIGHT / 2 )

def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        day = current_time.day
        month = current_time.month
        year = current_time.year
        weekday = current_time.today().isoweekday()
        calendar = current_time.today().isocalendar()

        weekdays_abbr = {1: "Mo", 2: "Tu", 3: "We", 4: "Th", 5: "Fr", 6: "Sa", 7: "Su"}
        weekday_abbr = weekdays_abbr.get(weekday)

        months_abbr = {1: "JAN", 2: "FEB", 3: "MAR", 4: "APR", 5: "MAY", 6: "JUN", 7: "JUL", 8: "AUG", 9: "SEP", 10: "OCT", 11: "NOV", 12: "DEC"}
        month_abbr = months_abbr.get(month)

        screen.fill(BLACK)
        pygame.draw.circle(screen, CYAN, center, clock_radius - 10, 10)
        pygame.draw.circle(screen, CYAN, center, 12)
        pygame.draw.rect(screen,WHITE , [WIDTH / 2 - 260, HEIGHT / 2 -30, 80, 60], 3)
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 - 180, HEIGHT / 2 -30, 80, 60], 3)
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 + 100, HEIGHT / 2 -30, 80, 60], 3)
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 + 180, HEIGHT / 2 -30, 80, 60], 3)
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 - 50, HEIGHT / 2 -30 + 160, 100, 60], 3)

        numbers(str(weekday_abbr), 40, (WIDTH / 2 - 220, HEIGHT / 2))
        numbers(str(calendar[1]), 40, (WIDTH / 2 - 140, HEIGHT / 2))
        numbers(str(month_abbr), 40, (WIDTH / 2 + 140, HEIGHT / 2))
        numbers(str(day), 40, (WIDTH / 2 + 220, HEIGHT / 2))
        numbers(str(year), 40, (WIDTH / 2, HEIGHT / 2 + 160))

        for number in range(1,13):
            numbers(str(number), 80, polar_to_cartesian(clock_radius - 80, number * 30))

        for number in range(0, 360, 6):
            if number % 5:
                pygame.draw.line(screen, WHITE, polar_to_cartesian(clock_radius - 15, number), polar_to_cartesian(clock_radius - 30, number), 4)
            else:
                pygame.draw.line(screen, WHITE, polar_to_cartesian(clock_radius - 15, number), polar_to_cartesian(clock_radius - 35, number), 8)

        #hour
        r = 225
        theta = (hour + minute / 60 + second / 3600) * (360 / 12)
        pygame.draw.line(screen, WHITE, center, polar_to_cartesian(r, theta), 15)

        #minute
        r = 295
        theta = (minute + second / 60) * (360 / 60)
        pygame.draw.line(screen, WHITE, center, polar_to_cartesian(r, theta), 10)

        #second
        r = 345
        theta = second * (360 / 60)
        pygame.draw.line(screen, RED, center, polar_to_cartesian(r, theta), 4)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()

main()
