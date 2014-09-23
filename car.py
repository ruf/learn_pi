#!/usr/bin/python

import os, sys, select, termios, time, random

class NonBlockingConsole(object):
    def __enter__(self):
        self.old_settings = termios.tcgetattr(sys.stdin)
        newattr = self.old_settings[:]
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(sys.stdin, termios.TCSANOW, newattr)
        return self
    def __exit__(self, type, value, traceback):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)
    def getc(self):
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            k = sys.stdin.read(1) # if key pressed, return the key
            while select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
                k = sys.stdin.read(1)
            return k
        return False

rows, columns = os.popen('stty size', 'r').read().split()

with NonBlockingConsole() as nbc:
    width = int(columns) - 14
    road = width / 2
    left = (width - road) / 2
    car = road / 2
    d = 0
    for i in range(3000):
        e = {-1:'//', 0:'||', 1:'\\\\'}[d]
        print ('%4dm ' % i) + ' ' * left + e + ' ' * car + '-O-' + ' ' * (road - car) + e, '\r',
        sys.stdout.flush() # show this line ASAP
        if car < 0 or car > road: # PONG!
            break
        c = nbc.getc()
        if c == 'x' or c == 'q':
            break
        elif c == 'j' or c == '4':
            car -= 1
        elif c == 'l' or c == '6':
            car += 1
        r = random.random()
        if r < 0.4 and d >= 0:
            d -= 1
        elif r > 0.6 and d <= 0:
            d += 1
        if left == 0 and d < 0 or left + road == width and d > 0:
            d = 0
        time.sleep(0.04)
        print ' ' * (6 + left) + e + ' ' * (3 + road) + e
        left += d
        car -= d
        if r < 0.02:
            road -= 1
    print
