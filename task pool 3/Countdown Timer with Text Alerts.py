import time
start = input("input number to start counting from ")
step = input("input step for counting ")
alert_every = input("input True if you want alert of seconds often and Enter if you want to set in default ")

def countdown(start, step, alert_every):
    if alert_every != "":
        alert_skip = 0.5
    else: alert_skip = 5
    count = start
    alert_timer = start
    for i in range(start):
        print(count)
        if alert_skip <= alert_timer - count:
            print(f"{start-count} seconds left!")
            alert_timer -= alert_skip
        count -= step
        if count == 0:
            print("Time’s up!")
        time.sleep(0.5)
countdown(int(start), int(step), alert_every)