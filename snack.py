import random
import curses

screen = curses.initscr()
curses.curs_set(0)
screen_height, screen_width = screen.getmaxyx()
window = curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1)
window.timeout(100)
snake_x = screen_width // 4
snake_y = screen_height // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]
food = [screen_height // 2, screen_width // 2]
window.addch(food[0], food[1], curses.ACS_PI)