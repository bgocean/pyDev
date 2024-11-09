import time
import threading


def sleepTime(wait, name):
    print("Выводим текст: {}".format(name))
    time.sleep(wait)
    print("Выводим текст повторно: {}".format(name))


td = threading.Thread(target=sleepTime, name='SleepTime', args=(3, 'SleepTime'))
td.start()

# sleepTime(3, 'SleepTime')
print('Hello!')


# 07.00 video