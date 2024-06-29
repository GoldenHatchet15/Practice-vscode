#!/usr/bin/env python3
import time

def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!")

def main():
    minutes = int(input("Enter the time in minutes: "))
    seconds = int(input("Enter the time in seconds: "))
    countdown_timer(minutes, seconds)

if __name__ == "__main__":
    main()
