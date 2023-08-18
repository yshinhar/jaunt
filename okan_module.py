import time
import winsound


freq = 2500
dur = 500


def party_time():
    print("\nparty time in...")
    for i in range(10):
        print(10-i)
        winsound.Beep(freq, dur)
        time.sleep(1)
    winsound.Beep(freq, dur*6)
    print("PaRtY tImE!!!"*1000001)
def bomb():
    for i in range(30):
        winsound.Beep(freq, 500 - i*15)
    winsound.Beep(freq, dur*6)
    print("\n"*6 + "boom")
    time.sleep(3)
    print("what did you expect?...")
def easter_eggs():
        print("\nEASTER EGGS / PARTY TIME / BOMB!!! / im to weak... / who is yonathan? / no... / all hail the magic conch shell!")
def spongebob():
    print("\n\nloo looo looo looo looo loo loo loo loo loo loo loo loo loo loo\n")
    for i in range(15):
        winsound.Beep(freq, 100)
def star_wars():
        print("\n UNLIMTED POWER !!! \n")
        for i in range(15):
                winsound.Beep(freq, 100)
def me():
    print("\nahh yonathan...my creator, a very creative and talented boy")
def no():
    print("okay...")
    time.sleep(2)
    exit


