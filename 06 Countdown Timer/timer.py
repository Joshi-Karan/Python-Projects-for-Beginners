import time

def timer(t):
    while t:
        min, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end = '\r')
        time.sleep(1)
        t -= 1
    print('COUTDOWN COMPLETE!!!')


if __name__ == "__main__":
    t = int(input('Enter time in seconds: '))
    timer(t)
