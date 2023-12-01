import sched
import time

s = sched.scheduler(time.time, time.sleep)

def stand_up(msg):
    print(msg)

def schedule_standups(interval):
    stand_up("Time to stand up and take a break!")
    s.enter(interval, 1, schedule_standups, (interval,))

def start_standups(interval=3600):
    s.enter(0, 1, schedule_standups, (interval,))
    s.run()

if __name__ == "__main__":
    start_standups(3600)
