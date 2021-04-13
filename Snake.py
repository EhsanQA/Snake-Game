import curses
import random
def main():
    # the Window
    curses.initscr()

    window = curses.newwin(20, 60, 0, 0)

    window.keypad(1)

    curses.noecho()
    curses.curs_set(0)
    window.border(0)
    window.nodelay(1)
    # Snake Initial Coordinates
    snake = [(4, 10), (4, 9), (4, 8)]
    # Food Initial Coordinates
    food = (10, 20)
    window.addch(food[0], food[1], "#")

    ESC = 27
    key = curses.KEY_RIGHT
    win = False
    score = 0
    while key != ESC:
        if score == 50:
            win = True
            break
        window.addstr(0, 2, "Score: " + str(score) + " ")
        window.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)

        prev_key = key
        event = window.getch()
        key = event if event != -1 else prev_key
        if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
            key = prev_key

        y = snake[0][0]
        x = snake[0][1]
        
        if key == curses.KEY_DOWN:
            y += 1
        if key == curses.KEY_UP:
            y -= 1
        if key == curses.KEY_RIGHT:
            x += 1
        if key == curses.KEY_LEFT:
            x -= 1    
        
        snake.insert(0, (y, x))

        if y == 0 or y == 19 or x == 0 or x == 59: break
        

        if snake[0] in snake[1:]: break

        if snake[0] == food:
            score += 1
            food = ()
            while food == ():
                food = (random.randint(1, 18), random.randint(1, 58))
                if food in snake:
                    food = ()
            window.addch(food[0], food[1], "#")
        else:
            # move the snake
            last = snake.pop()
            window.addch(last[0], last[1], " ")

        window.addch(snake[0][0], snake[0][1], "*")
    curses.endwin()
    if win:
        print("YOU WIN!!!")
    print(f"Your Score: {score}")



if __name__ == "__main__":
    main()