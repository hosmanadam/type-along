import os
import random
import string
import sys
import time

from text_formatting import bold, green

WAIT = 0.8


def tackle_number(length):
    os.system('clear')
    task = ''.join(random.choice(string.digits) for i in range(length))
    print(task, bold('← type this'), '(⌃C to quit)')
    entry = ''
    while task != entry:
        entry = input()


def quit_app(solve_count):
    os.system('clear')
    plural = '' if solve_count == 1 else 's'
    print(f"You've tackled {bold(green(solve_count))} number{plural}.")
    time.sleep(WAIT)
    print(f"See you tomorrow!", end='', flush=True)
    time.sleep(WAIT)
    print('')
    sys.exit(0)


def main():
    solve_count = 0
    while True:
        try:
            tackle_number(4)
            solve_count += 1
        except KeyboardInterrupt:
            quit_app(solve_count)


if __name__ == '__main__':
    main()
