import playsound
import time

def alarmclock(seconds):
    time_elapsed=0

    CLEAR="\033[2J"
    CLEAR_AND_RETURN="\033["

    print(CLEAR)
    for _ in range(seconds):
        time.sleep(1)
        time_elapsed+=1

        time_left= seconds-time_elapsed

        minutes_left= time_left//60
        seconds_left= time_left%60

        print(f"{CLEAR_AND_RETURN}TTime left for alarm-> {minutes_left:02d}:{seconds_left:02d}")


def main():
    print("Set the timer now!")
    minutes=int(input("Enter minutes"))
    seconds=int(input("Enter seconds"))
    total= minutes*60+seconds

    alarmclock(total)


if __name__=="__main__":
    main()