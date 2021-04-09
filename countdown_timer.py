import time


def countdown(t):
    while t:
        minis, secs = divmod(t, 60)
        timer = f'{minis:02d} : {secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print('Timer completed!')


times = int(input('타이머 설정 (초): '))
countdown(times)
