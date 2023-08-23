import random
import time
import winsound
import turtle as a
import okan_module as mod

import face_recognition
import cv2
from collections import Counter
import pickle
from pathlib import Path


DEFAULT_ENCODINGS_PATH = Path("ai_models/encodings.pkl")
freq = 2500
dur = 500

def clear():
    a.pendown()
    a.color("white")
    a.goto(-500,-500)
    a.pendown()
    a.begin_fill()
    a.goto(-500,-500)
    a.goto(500,-500)
    a.goto(500,500)
    a.goto(-500,500)
    a.end_fill()
    a.penup()

def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding, tolerance=0.5
    )
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )    
    if votes:
        return votes.most_common(1)[0][0]

def test_from_stream(model: str = "hog", encodings_location: Path = DEFAULT_ENCODINGS_PATH):
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)
    cap = cv2.VideoCapture(0)

    
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    not_again = 0
    if not_again ==0:
        print("hi there, im Jank And Useless Nity Tools, or in short JAUNT ;)")
        print("if you need anything, just say what you want and i will do it :)")
        not_again += 1
    while True:
        okan_found = False
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb, model=model)
        encodings = face_recognition.face_encodings(rgb, face_locations)

        for bounding_box, unknown_encoding in zip(face_locations, encodings):
            name = _recognize_face(unknown_encoding, loaded_encodings)
            if not name:
                name = "Not Okan"
            else:
                okan_found = True

            top, right, bottom, left = bounding_box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        cv2.imshow('Input', frame)
        c = cv2.waitKey(1)
        if okan_found:
            print("okan found")
            break
        elif c == 27:
            print("only okan can use me, and you are not okan")
            exit(1)

    cap.release()

print("searching for okan")
test_from_stream()


while True:
    winsound.Beep(freq, 200)
    print("\n\n\n\n\n\n\n\n\n\n\n                 JAUNT")
    print("bye ( close )")
    print("play1 ( rock, paper, scissors )")
    print("play2 ( tic-tac-toe )")
    print("time ( CLICK & CLOCK  )")
    print("note ( write a note )")
    print("1 ( ULTIMATE RANDOM GENERATOR )")
    print("2 ( SHAPE MASTER )")
    print("3 ( cut string )")
    print("4 ( X equation )")
    op = input("JAUNT, ")

    if op =='bye' or op ==' bye':
        break
    elif op =='1' or op ==' 1':      
        print ("\nwelcome to the ULTIMATE RANDOM GENERATOR!!! ;)")
        while True:
            chosen = input("\n\nplease choose a generator:\n1)exit\n2)random number\n3)coin toss\n4)1-10\n5)roll dice\n6)magic conch shell\n7)gen 2 pokemon\n8)random timer\n\nuse generator number: ")
            if chosen == '1':
                break
            elif chosen == '2':
                again = 's'
                count = 0
                while again == 'y' or again == 's':
                    if again == 's':
                        try:
                            mini=int(input("\npick the lowest number: "))
                        except ValueError:
                            print("\ninput needs to be a number not this :(")
                            count += 1
                            if count == 2:
                                print("\nyou are too stupid to use this program... bye bye")
                                time.sleep(3)
                                break
                            continue
                        try:
                            maxi=int(input("\npick the highest number: "))
                        except ValueError:
                            print("\ninput needs to be a number :(")
                            count += 1
                            if count == 2:
                                print("\nyou are too stupid to use this program... bye bye")
                                time.sleep(3)
                                break
                            continue
                    
                    print(random.randint(min(mini, maxi), max(maxi, mini)))
             
                    while True:
                        again = input("go again? y/n ")
                        if again in ['n', 'y']:
                            break
                        elif count == 2:
                            print("\nyou are too stupid to use this program... bye bye")
                            time.sleep(3)
                            break
                        else:
                            count += 1
                            print("\מinput error, please try again :(")
            elif chosen == "PARTY TIME":
                print("\nparty time in...")
                for i in range(10):
                    print(10-i)
                    winsound.Beep(freq, dur)
                    time.sleep(1)
                winsound.Beep(freq, dur*6)
                print("PaRtY tImE!!!"*1000001)
            elif chosen == "BOMB!!!":
                for i in range(30):
                    winsound.Beep(freq, 500 - i*15)
                winsound.Beep(freq, dur*6)
                print("\n"*6 + "boom")
                time.sleep(3)
                print("what did you expect?...")
                time.sleep(4)
            elif chosen == "EASTER EGGS":
                print("\nEASTER EGGS / PARTY TIME / BOMB!!! / im to weak... / who is yonathan? / no... / all hail the magic conch shell!")
            elif chosen == '3':
                lst = ["heads", "tails"]
                print("\n\n", lst[random.randint(0, len(lst)-1)])
            elif chosen =='4':
                print("\n\n", random.randint(1, 10))
            elif chosen =='5':
                print("\n\n", random.randint(1, 6))
            elif chosen =='6':
                lst = ["yes", "yes", "yes", "yes", "no", "nothing", "neither", "maybe", "maybe someday", "i don't think so", "try asking again"]
                text_in = input("\noh magic conch shell...")
                if text_in == "all hail the magic conch shell!":
                    print("\n\nloo looo looo looo looo loo loo loo loo loo loo loo loo loo loo\n")
                    for i in range(15):
                        winsound.Beep(freq, 100)
                else:
                    print("\n\n", lst[random.randint(0, len(lst)-1)], "\n")
            elif chosen =='7':
                lst = ["chikorita", "bayleef", "meganium", "cyndaquil", "quilava", "typhlosion", "totodile", "croconaw", "feraligatr", "sentret", "furret", "hoothoot", "noctowl", "ledyba", "ledian", "spinarak", "ariados", "crobat", "chinchou", "lanturn", "pichu", "cleffa", "igglybuff", "togepi", "togetic", "natu", "xatu", "mareep", "flaaffy", "ampharos", "bellossom", "marill", "azumarill", "sudowoodo", "politoed", "hoppip", "skiploom", "jumpluff", "aipom", "sunkern", "sunflora", "yanma", "wooper", "quagsire", "espeon", "umbreon", "murkrow", "slowking", "misdreavus", "unown", "wobbuffet", "girafarig", "pineco", "forretress", "dunsparce", "gligar", "steelix", "snubbull", "granbull", "qwilfish", "scizor", "shuckle", "heracross", "sneasel", "teddiursa", "ursaring", "slugma", "magcargo", "swinub", "piloswine", "corsola", "remoraid", "octillery", "delibird", "mantine", "skarmory", "houndour", "houndoom", "kingdra", "phanpy", "donphan", "porygon2", "stantler", "smeargle", "tyrogue", "hitmontop", "smoochum", "elekid", "magby", "miltank", "blissey", "raikou", "entei", "suicune", "larvitar", "pupitar", "tyranitar", "lugia", "ho-oh", "celebi"]
                print("\n\n", lst[random.randint(0, len(lst)-1)], "\n")
            elif chosen == "im to weak...":
                print("\n UNLIMTED POWER !!! \n")
                for i in range(15):
                        winsound.Beep(freq, 100)
            elif chosen =='8':
                        for i in range(random.randint(0,60)):
                         winsound.Beep(freq, 100)
            elif chosen == "who is yonathan?":
                print("\nahh yonathan...my creator, a very creative and talented boy")
            elif chosen =="no...":
                print("okay...")
                time.sleep(2)
                break
            else:
                print("\nplease choose something form the list :(\n")

    elif op =='2' or op ==' 2':
        

        def shape_master():
                bones =input("what is the shape (ribs)? - ")
                long_boy =input("how long is the ribs? - ")
                fool =input("do you want to fill it up? (n\y) - ")

                if fool =='y':
                        a.begin_fill()
                        for k in range(int(bones)): 
                                a.forward(int(long_boy))
                                a.left(360/(int(bones)))
                        a.end_fill()
                elif fool =='n':
                        for k in range(int(bones)):
                                a.forward(int(long_boy))
                                a.left(360/(int(bones)))


        def controler():
            while FOREVER <1000002:
                    movement =input("how to move? (f/b/r/l/noop) - ")
                    if movement =='f':
                        how_f =input("how much to move forward? - ")
                        a.forward(int(how_f))
                    elif movement =='b':
                        how_b =input("how much to move backward? - ")
                        a.backward(int(how_b))
                    elif movement =='r':
                        how_r =input("how much to turn right? - ")
                        a.right(int(how_r))
                    elif movement =='l':
                        how_l =input("how much to turn left? - ")
                        a.left(int(how_b))
                    else:
                        break
                
        def Pen_MAN():
            THICK =input("how THICK is your pen? - ")
            a.pensize(int(THICK))
            print(f"\npensize is{THICK}\n")
        def coolar():
            cool =input("what is the color? - ")
            a.color(cool)
            print(f"\ncolor is {cool}\n")

        def woop_weep():
            up_or_down =input("do you want your pen up or down? (u/d/noop) - ")
            if up_or_down =='u':
                a.penup()
                print("\nyour pen is up\n")
            elif up_or_down =='d':
                a.pendown()
                print("\nyour pen is down\n")
            else:
                exit
        def fill_it_UP():
                fill_or_not =input("do you want to start or end the fill (s/e/noop) - ")
                if fill_or_not =='s':
                        a.begin_fill()
                        print("\nyou begin the filling\n")
                elif fill_or_not =='e':
                        a.end_fill()
                        print("\nyou end the filling\n")
                else:
                        exit
        def who():
                whox =input("where to go? x - ")
                whoy =input("where to go? y - ")
                a.goto(int(whox),int(whoy))
        FOREVER = 1000001
        print("WELCOME TO SHAPE MASTER made by jonathan shinhar\n\n")
        while FOREVER < 1000002:
                what_to_do =input("\nwhat do you want to do?\n1) shape\n2) controler\n3) color\n4) pen size\n5) fill\n6) pen up\down\n7) goto\n8) noop\n")
                if what_to_do =='1':
                        shape_master()
                elif what_to_do =='2':
                        controler()
                elif what_to_do =='3':
                        coolar()
                elif what_to_do =='4':
                        pen_MAN()
                elif what_to_do =='5':
                        fill_it_UP()
                elif what_to_do =='6':
                        woop_weep()
                elif what_to_do =='7':
                        who()
                elif what_to_do =='PARTY TIME':
                        mod.party_time()
                elif what_to_do =='BOMB!!!':
                        mod.bomb()
                elif what_to_do =='EASTER EGGS':
                        mod.easter_eggs()
                elif what_to_do =='im to weak...':
                        mod.star_wars()
                elif what_to_do =='no...':
                        mod.no()
                elif what_to_do =='who is yonathan?':
                        mod.me()
                elif what_to_do =='all hail the magic conch shell!':
                        mod.spongebob()
                else:
                        break
    elif op =='3' or op ==' 3':
        while True:
            do_you = input("do you want to cut a str? (no/yes) - ")
            if do_you =='yes':   
                name =input("enter a str -")
                start =input("chose the number latter to start-")
                end =input("chose the number latter to end(-1)-")
                jump =input("what is the jump-")
                print(name[int(start):int(end):int(jump)])
            elif do_you =='no':
                break
            else:
                ''
    elif op =='4' or op ==' 4':
        while True:
            cont =input("do you want the answer of your equation? (y/n) - ")
            if cont =='y':
                
                answer = int(input("what is the answer - "))
                print("\nADD NUMBERS TO X\n")
                while True:
                    aopa = input('+/-/*/ "/" / finish -')
                    if aopa =="+":
                        how_much = input("how_much - ")
                        answer -= int(how_much)
                    if aopa =="-":
                        how_much = input("how_much - ")
                        answer += int(how_much)
                    if aopa =="*":
                        how_much = input("how_much - ")
                        answer = int(answer) / int(how_much)
                    if aopa =="/":
                        how_much = input("how_much - ")
                        answer = int(answer) * int(how_much)
                    if aopa =="finish":
                        break
                    else:
                        ""
                print("x =",answer)
            elif cont =='n':
                break
    if op =='play1' or op ==' play1':
        won = 0
        won_ai = 0
        while True:
            print("\nNEW GAME !")
            print(f"JAUNT won {won_ai} times")
            print(f"you won {won} times")
            more = input("play? (y/n) - ")
            if more =='y':
                point = 0
                point_ai = 0
                while True:
                    print(f"\nyour points - {point}")
                    print(f"JAUNT points - {point_ai}")
                    chose =input("\nchose(r/p/s) - ")

                    chose_ai = random.randint(1, 3)
                    if chose_ai ==1:
                        chose_ai ="r"
                    elif chose_ai ==2:
                        chose_ai ="p"
                    elif chose_ai ==3:
                        chose_ai ="s"
                    print(f"\nyou used {chose}")
                    print(f"JAUNT used {chose_ai}\n")
                    if chose =="r" and chose_ai =="s":
                        point += 1
                        print("YOU GOT A POINT")
                    elif chose =="p" and chose_ai =="r":
                        point += 1
                        print("YOU GOT A POINT")
                    elif chose =="s" and chose_ai =="p":
                        point += 1
                        print("YOU GOT A POINT")
                        
                    elif chose_ai =="r" and chose =="s":
                        point_ai += 1
                        print("JAUNT GOT A POINT")
                    elif chose_ai =="p" and chose =="r":
                        point_ai += 1
                        print("JAUNT GOT A POINT")
                    elif chose_ai =="s" and chose =="p":
                        point_ai += 1
                        print("JAUNT GOT A POINT")
                    else:
                        print("DREW")
                    
                    if point ==3:
                        print("YOU WON !")
                        won += 1
                        break
                    if point_ai ==3:
                        print("JAUNT WON...")
                        won_ai += 1
                        break
            elif more =='n':
                break
            else:
                ''
    if op =="note" or op ==" note":
        name = input('what is the name of the note? - ')
        try:
            f = open(f"{name}.txt", "r")
            f.close()
            print("\n     YOU HAVE A NOTE WITH THIS NAME ALREADY\n")
        except FileNotFoundError:
            the_note = ""
            print('           write the note (write "jaunt, close" to finish)\n\n')
            f = open(f"{name}.txt", "w")
            while "jaunt, close" not in the_note:
                
                f = open(f"{name}.txt", "a")
                the_note = input()
                if the_note != "jaunt, close":
                    f.write(f"\n{the_note}")
                f.close()
            while 1==1:
                break
            
    elif op =="time" or op ==" time":
        a.speed(1000000000000000000000000000000000000000000000000000000000000000001)
        print("           welcome to CLICK & CLOCK")
        phan =input('what "time" fanction do you want? (2020 / timer) - ')
        if phan =="2020" or phan ==" 2020":
            while True:
                the_timer = 20
                while the_timer > 0:
                    clear()
                    a.goto(-300,-300)
                    a.pendown()
                    a.color("black")
                    a.write(the_timer, font=("Arial", 400, "normal"))
                    time.sleep(60)
                    the_timer -= 1
                for k in range(20):
                    winsound.Beep(1800,250)
                the_timer = 20
                while the_timer > 0:
                    time.sleep(1)
                    winsound.Beep(2000,300)
                    the_timer -= 1
        if phan =="timer" or phan ==" timer":
            while True:
                hours = int(input("set number of HOURS - "))
                minit = int(input("set number of MINUTES - "))
                sec = int(input("set number of SECENDS - "))
                while sec > 0:
                    clear()
                    a.goto(-300,-50)
                    a.pendown()
                    a.color("black")
                    a.write(hours, font=("Arial", 100, "normal"))
                    a.penup()
                    a.goto(-100,-50)
                    a.pendown()
                    a.color("black")
                    a.write(minit, font=("Arial", 100, "normal"))
                    a.penup()
                    a.goto(100, -50)
                    a.pendown()
                    a.color("black")
                    a.write(sec, font=("Arial", 100, "normal"))
                    time.sleep(0.5)
                    sec -= 1
                while minit > 0:
                    minit -= 1
                    sec = 59
                    while sec > 0:
                        clear()
                        a.goto(-300,-50)
                        a.pendown()
                        a.color("black")
                        a.write(hours, font=("Arial", 100, "normal"))
                        a.penup()
                        a.goto(-100,-50)
                        a.pendown()
                        a.color("black")
                        a.write(minit, font=("Arial", 100, "normal"))
                        a.penup()
                        a.goto(100, -50)
                        a.pendown()
                        a.color("black")
                        a.write(sec, font=("Arial", 100, "normal"))
                        time.sleep(0.5)
                        sec -= 1
                while hours > 0:
                    hours -= 1
                    minit = 60
                    while minit > 0:
                        minit -= 1
                        sec = 59
                        while sec > 0:
                            clear()
                            a.goto(-300,-50)
                            a.pendown()
                            a.color("black")
                            a.write(hours, font=("Arial", 100, "normal"))
                            a.penup()
                            a.goto(-100,-50)
                            a.pendown()
                            a.color("black")
                            a.write(minit, font=("Arial", 100, "normal"))
                            a.penup()
                            a.goto(100, -50)
                            a.pendown()
                            a.color("black")
                            a.write(sec, font=("Arial", 100, "normal"))
                            time.sleep(0.5)
                            sec -= 1
                for k in range(20):
                    winsound.Beep(1800,250)
                break

    elif op =="play2" or op ==" play2":
        x_won = 0
        o_won = 0

        lst = [1, 2]
        lst_x = [1, 1, 2]
        lst_o = [1, 2, 2]
        print("1) vs friend\n2) vs JAUNT")
        opa = input("number ")
        if opa =="1" or opa ==" 1":
            while True:
                thx_oy = "1"
                thx_ty = "2"
                thx_thy = "3"
                lst_th = [thx_oy,thx_ty,thx_thy]
                tx_oy = "4"
                tx_ty = "5"
                tx_thy = "6"
                lst_t = [tx_oy,tx_ty,tx_thy]
                ox_oy = "7"
                ox_ty = "8"
                ox_thy = "9"
                lst_o = [ox_oy,ox_ty,ox_thy]
                print(f"\n\nplayer X won {x_won} times")
                print(f"player O won {o_won} times\n\n")
                again = input("do you want to play? (y/n) - ")
                if again =='n':
                    break
                elif again =='y':
                    if x_won == o_won:
                        oorx = lst[random.randint(0, len(lst)-1)]
                    elif x_won > o_won:
                        oorx = lst_o[random.randint(0, len(lst_o)-1)]
                    elif o_won > x_won:
                        oorx = lst_x[random.randint(0, len(lst_x)-1)]
                    if oorx == 1:
                        print(thx_oy,"|",thx_ty,"|",thx_thy)
                        print("-","-","-","-","-")
                        print(tx_oy,"|",tx_ty,"|",tx_thy)
                        print("-","-","-","-","-")
                        print(ox_oy,"|",ox_ty,"|",ox_thy)
                        while True:
                            while True:
                                place_x =int(input("chose a place for X (1-9): "))
                                if place_x ==1 and thx_oy =="1":
                                    thx_oy = "X"
                                    break
                                elif place_x ==2 and thx_ty =="2":
                                    thx_ty = "X"
                                    break
                                elif place_x ==3 and thx_thy =="3":
                                    thx_thy = "X"
                                    break
                                elif place_x ==4 and tx_oy =="4":
                                    tx_oy = "X"
                                    break
                                elif place_x ==5 and tx_ty =="5":
                                    tx_ty = "X"
                                    break
                                elif place_x ==6 and tx_thy =="6":
                                    tx_thy = "X"
                                    break
                                elif place_x ==7 and ox_oy =="7":
                                    ox_oy = "X"
                                    break
                                elif place_x ==8 and ox_ty =="8":
                                    ox_ty = "X"
                                    break
                                elif place_x ==9 and ox_thy =="9":
                                    ox_thy = "X"
                                    break
                                else:
                                    print("you cant do that...")
                            lst_o = [ox_oy,ox_ty,ox_thy]
                            lst_t = [tx_oy,tx_ty,tx_thy]
                            lst_th = [thx_oy,thx_ty,thx_thy]

                            print(thx_oy,"|",thx_ty,"|",thx_thy)
                            print("-","-","-","-","-")
                            print(tx_oy,"|",tx_ty,"|",tx_thy)
                            print("-","-","-","-","-")
                            print(ox_oy,"|",ox_ty,"|",ox_thy)
                            
                            if lst_th == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif lst_t == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif lst_o == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy =='X' and tx_ty =='X' and ox_thy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_thy =='X' and tx_ty =='X' and ox_oy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy =='X' and tx_oy =='X' and ox_oy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_ty =='X' and tx_ty =='X' and ox_ty =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_thy =='X' and tx_thy =='X' and ox_thy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy != "1" and thx_ty != "2" and thx_thy != "3" and tx_oy != "4" and tx_ty != "5" and tx_thy != "6" and ox_oy != "7" and ox_ty != "8" and ox_thy != "9":
                                print("neither player won...")
                                break
                            while True:
                                place_o =int(input("chose a place for O (1-9): "))
                                if place_o ==1 and thx_oy =="1":
                                    thx_oy = "O"
                                    break
                                elif place_o ==2 and thx_ty =="2":
                                    thx_ty = "O"
                                    break
                                elif place_o ==3 and thx_thy =="3":
                                    thx_thy = "O"
                                    break
                                elif place_o ==4 and tx_oy =="4":
                                    tx_oy = "O"
                                    break
                                elif place_o ==5 and tx_ty =="5":
                                    tx_ty = "O"
                                    break
                                elif place_o ==6 and tx_thy =="6":
                                    tx_thy = "O"
                                    break
                                elif place_o ==7 and ox_oy =="7":
                                    ox_oy = "O"
                                    break
                                elif place_o ==8 and ox_ty =="8":
                                    ox_ty = "O"
                                    break
                                elif place_o ==9 and ox_thy =="9":
                                    ox_thy = "O"
                                    break
                                else:
                                    print("you cant do that...")
                            lst_o = [ox_oy,ox_ty,ox_thy]
                            lst_t = [tx_oy,tx_ty,tx_thy]
                            lst_th = [thx_oy,thx_ty,thx_thy]

                            print(thx_oy,"|",thx_ty,"|",thx_thy)
                            print("-","-","-","-","-")
                            print(tx_oy,"|",tx_ty,"|",tx_thy)
                            print("-","-","-","-","-")
                            print(ox_oy,"|",ox_ty,"|",ox_thy)
                            
                            if lst_th == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif lst_t == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif lst_o == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy =='O' and tx_ty =='O' and ox_thy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_thy =='O' and tx_ty =='O' and ox_oy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy =='O' and tx_oy =='O' and ox_oy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_ty =='O' and tx_ty =='O' and ox_ty =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_thy =='O' and tx_thy =='O' and ox_thy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy != "1" and thx_ty != "2" and thx_thy != "3" and tx_oy != "4" and tx_ty != "5" and tx_thy != "6" and ox_oy != "7" and ox_ty != "8" and ox_thy != "9":
                                print("neither player won...")
                                break
                        for k in range(10):
                            winsound.Beep(1800, 200)    
                        time.sleep(5)
                        thx_oy = "1"
                        thx_ty = "2"
                        thx_thy = "3"
                        lst_th = [thx_oy,thx_ty,thx_thy]
                        tx_oy = "4"
                        tx_ty = "5"
                        tx_thy = "6"
                        lst_t = [tx_oy,tx_ty,tx_thy]
                        ox_oy = "7"
                        ox_ty = "8"
                        ox_thy = "9"
                        lst_o = [ox_oy,ox_ty,ox_thy]
                    elif oorx == 2:
                        print(thx_oy,"|",thx_ty,"|",thx_thy)
                        print("-","-","-","-","-")
                        print(tx_oy,"|",tx_ty,"|",tx_thy)
                        print("-","-","-","-","-")
                        print(ox_oy,"|",ox_ty,"|",ox_thy)
                        while True:
                            while True:
                                place_o =int(input("chose a place for O (1-9): "))
                                if place_o ==1 and thx_oy =="1":
                                    thx_oy = "O"
                                    break
                                elif place_o ==2 and thx_ty =="2":
                                    thx_ty = "O"
                                    break
                                elif place_o ==3 and thx_thy =="3":
                                    thx_thy = "O"
                                    break
                                elif place_o ==4 and tx_oy =="4":
                                    tx_oy = "O"
                                    break
                                elif place_o ==5 and tx_ty =="5":
                                    tx_ty = "O"
                                    break
                                elif place_o ==6 and tx_thy =="6":
                                    tx_thy = "O"
                                    break
                                elif place_o ==7 and ox_oy =="7":
                                    ox_oy = "O"
                                    break
                                elif place_o ==8 and ox_ty =="8":
                                    ox_ty = "O"
                                    break
                                elif place_o ==9 and ox_thy =="9":
                                    ox_thy = "O"
                                    break
                                else:
                                    print("you cant do that...")
                            lst_o = [ox_oy,ox_ty,ox_thy]
                            lst_t = [tx_oy,tx_ty,tx_thy]
                            lst_th = [thx_oy,thx_ty,thx_thy]

                            print(thx_oy,"|",thx_ty,"|",thx_thy)
                            print("-","-","-","-","-")
                            print(tx_oy,"|",tx_ty,"|",tx_thy)
                            print("-","-","-","-","-")
                            print(ox_oy,"|",ox_ty,"|",ox_thy)
                            
                            if lst_th == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif lst_t == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif lst_o == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy =='O' and tx_ty =='O' and ox_thy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_thy =='O' and tx_ty =='O' and ox_oy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy =='O' and tx_oy =='O' and ox_oy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_ty =='O' and tx_ty =='O' and ox_ty =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_thy =='O' and tx_thy =='O' and ox_thy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy != "1" and thx_ty != "2" and thx_thy != "3" and tx_oy != "4" and tx_ty != "5" and tx_thy != "6" and ox_oy != "7" and ox_ty != "8" and ox_thy != "9":
                                print("neither player won...")
                                break
                            while True:
                                place_x =int(input("chose a place for X (1-9): "))
                                if place_x ==1 and thx_oy =="1":
                                    thx_oy = "X"
                                    break
                                elif place_x ==2 and thx_ty =="2":
                                    thx_ty = "X"
                                    break
                                elif place_x ==3 and thx_thy =="3":
                                    thx_thy = "X"
                                    break
                                elif place_x ==4 and tx_oy =="4":
                                    tx_oy = "X"
                                    break
                                elif place_x ==5 and tx_ty =="5":
                                    tx_ty = "X"
                                    break
                                elif place_x ==6 and tx_thy =="6":
                                    tx_thy = "X"
                                    break
                                elif place_x ==7 and ox_oy =="7":
                                    ox_oy = "X"
                                    break
                                elif place_x ==8 and ox_ty =="8":
                                    ox_ty = "X"
                                    break
                                elif place_x ==9 and ox_thy =="9":
                                    ox_thy = "X"
                                    break
                                else:
                                    print("you cant do that...")
                            lst_o = [ox_oy,ox_ty,ox_thy]
                            lst_t = [tx_oy,tx_ty,tx_thy]
                            lst_th = [thx_oy,thx_ty,thx_thy]

                            print(thx_oy,"|",thx_ty,"|",thx_thy)
                            print("-","-","-","-","-")
                            print(tx_oy,"|",tx_ty,"|",tx_thy)
                            print("-","-","-","-","-")
                            print(ox_oy,"|",ox_ty,"|",ox_thy)
                            
                            if lst_th == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif lst_t == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif lst_o == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy =='X' and tx_ty =='X' and ox_thy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_thy =='X' and tx_ty =='X' and ox_oy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy =='X' and tx_oy =='X' and ox_oy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_ty =='X' and tx_ty =='X' and ox_ty =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_thy =='X' and tx_thy =='X' and ox_thy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy != "1" and thx_ty != "2" and thx_thy != "3" and tx_oy != "4" and tx_ty != "5" and tx_thy != "6" and ox_oy != "7" and ox_ty != "8" and ox_thy != "9":
                                print("neither player won...")
                                break
                        for k in range(10):
                            winsound.Beep(1800, 200)
                        time.sleep(5)
                        thx_oy = "1"
                        thx_ty = "2"
                        thx_thy = "3"
                        lst_th = [thx_oy,thx_ty,thx_thy]
                        tx_oy = "4"
                        tx_ty = "5"
                        tx_thy = "6"
                        lst_t = [tx_oy,tx_ty,tx_thy]
                        ox_oy = "7"
                        ox_ty = "8"
                        ox_thy = "9"
                        lst_o = [ox_oy,ox_ty,ox_thy]
                else:
                    print("you cant do that...")    



        elif opa =="2" or opa ==" 2":
            while True:
                thx_oy = "1"
                thx_ty = "2"
                thx_thy = "3"
                lst_th = [thx_oy,thx_ty,thx_thy]
                tx_oy = "4"
                tx_ty = "5"
                tx_thy = "6"
                lst_t = [tx_oy,tx_ty,tx_thy]
                ox_oy = "7"
                ox_ty = "8"
                ox_thy = "9"
                lst_o = [ox_oy,ox_ty,ox_thy]
                print(f"\n\nplayer X won {x_won} times")
                print(f"JAUNT (O) won {o_won} times\n\n")
                again = input("do you want to play? (y/n) - ")
                if again =='n':
                    break
                elif again =='y':
                    if x_won == o_won:
                        oorx = lst[random.randint(0, len(lst)-1)]
                    elif x_won > o_won:
                        oorx = lst_o[random.randint(0, len(lst_o)-1)]
                    elif o_won > x_won:
                        oorx = lst_x[random.randint(0, len(lst_x)-1)]
                    if oorx == 1:
                        print(thx_oy,"|",thx_ty,"|",thx_thy)
                        print("-","-","-","-","-")
                        print(tx_oy,"|",tx_ty,"|",tx_thy)
                        print("-","-","-","-","-")
                        print(ox_oy,"|",ox_ty,"|",ox_thy)
                        while True:
                            while True:
                                place_x =int(input("chose a place for X (1-9): "))
                                if place_x ==1 and thx_oy =="1":
                                    thx_oy = "X"
                                    break
                                elif place_x ==2 and thx_ty =="2":
                                    thx_ty = "X"
                                    break
                                elif place_x ==3 and thx_thy =="3":
                                    thx_thy = "X"
                                    break
                                elif place_x ==4 and tx_oy =="4":
                                    tx_oy = "X"
                                    break
                                elif place_x ==5 and tx_ty =="5":
                                    tx_ty = "X"
                                    break
                                elif place_x ==6 and tx_thy =="6":
                                    tx_thy = "X"
                                    break
                                elif place_x ==7 and ox_oy =="7":
                                    ox_oy = "X"
                                    break
                                elif place_x ==8 and ox_ty =="8":
                                    ox_ty = "X"
                                    break
                                elif place_x ==9 and ox_thy =="9":
                                    ox_thy = "X"
                                    break
                                else:
                                    print("you cant do that...")
                            lst_o = [ox_oy,ox_ty,ox_thy]
                            lst_t = [tx_oy,tx_ty,tx_thy]
                            lst_th = [thx_oy,thx_ty,thx_thy]

                            print(thx_oy,"|",thx_ty,"|",thx_thy)
                            print("-","-","-","-","-")
                            print(tx_oy,"|",tx_ty,"|",tx_thy)
                            print("-","-","-","-","-")
                            print(ox_oy,"|",ox_ty,"|",ox_thy)
                            
                            if lst_th == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif lst_t == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif lst_o == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy =='X' and tx_ty =='X' and ox_thy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_thy =='X' and tx_ty =='X' and ox_oy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy =='X' and tx_oy =='X' and ox_oy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_ty =='X' and tx_ty =='X' and ox_ty =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_thy =='X' and tx_thy =='X' and ox_thy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy != "1" and thx_ty != "2" and thx_thy != "3" and tx_oy != "4" and tx_ty != "5" and tx_thy != "6" and ox_oy != "7" and ox_ty != "8" and ox_thy != "9":
                                print("neither player won...")
                                break
        ####
                            print("JAUNT move...")
                            if lst_th == ['O', '2', 'O']:
                                place_o = 2
                            elif lst_th == ['1', 'O', 'O']:
                                place_o = 1
                            elif lst_th == ['O', 'O', '3']:
                                place_o = 3
                                
                            elif lst_t == ['O', '5', 'O']:
                                place_o = 5
                            elif lst_t == ['4', 'O', 'O']:
                                place_o = 4
                            elif lst_t == ['O', 'O', '6']:
                                place_o = 6
                                
                            elif lst_o == ['O', '8', 'O']:
                                place_o = 8
                            elif lst_o == ['7', 'O', 'O']:
                                place_o = 7
                            elif lst_o == ['O', 'O', '9']:
                                place_o = 9
                                
                            elif thx_oy =='1' and tx_ty =='O' and ox_thy =='O':
                                place_o = 1
                            elif thx_oy =='O' and tx_ty =='5' and ox_thy =='O':
                                place_o = 5
                            elif thx_oy =='O' and tx_ty =='O' and ox_thy =='9':
                                place_o = 9
                                
                            elif thx_thy =='3' and tx_ty =='O' and ox_oy =='O':
                                place_o = 3
                            elif thx_thy =='O' and tx_ty =='5' and ox_oy =='O':
                                place_o = 5
                            elif thx_thy =='O' and tx_ty =='O' and ox_oy =='7':
                                place_o = 7
                                
                            elif thx_oy =='1' and tx_oy =='O' and ox_oy =='O':
                                place_o = 1
                            elif thx_oy =='O' and tx_oy =='4' and ox_oy =='O':
                                place_o = 4
                            elif thx_oy =='O' and tx_oy =='O' and ox_oy =='7':
                                place_o = 7
                                
                            elif thx_ty =='2' and tx_ty =='O' and ox_ty =='O':
                                place_o = 2
                            elif thx_ty =='O' and tx_ty =='5' and ox_ty =='O':
                                place_o = 5
                            elif thx_ty =='O' and tx_ty =='O' and ox_ty =='8':
                                place_o = 8
                                
                            elif thx_thy =='3' and tx_thy =='O' and ox_thy =='O':
                                place_o = 3
                            elif thx_thy =='O' and tx_thy =='6' and ox_thy =='O':
                                place_o = 6
                            elif thx_thy =='O' and tx_thy =='O' and ox_thy =='9':
                                place_o = 9


                            elif lst_th == ['X', '2', 'X']:
                                place_o = 2
                            elif lst_th == ['1', 'X', 'X']:
                                place_o = 1
                            elif lst_th == ['X', 'X', '3']:
                                place_o = 3
                                
                            elif lst_t == ['X', '5', 'X']:
                                place_o = 5
                            elif lst_t == ['4', 'X', 'X']:
                                place_o = 4
                            elif lst_t == ['X', 'X', '6']:
                                place_o = 6
                                
                            elif lst_o == ['X', '8', 'X']:
                                place_o = 8
                            elif lst_o == ['7', 'X', 'X']:
                                place_o = 7
                            elif lst_o == ['X', 'X', '9']:
                                place_o = 9
                                
                            elif thx_oy =='1' and tx_ty =='X' and ox_thy =='X':
                                place_o = 1
                            elif thx_oy =='X' and tx_ty =='5' and ox_thy =='X':
                                place_o = 5
                            elif thx_oy =='X' and tx_ty =='X' and ox_thy =='9':
                                place_o = 9
                                
                            elif thx_thy =='3' and tx_ty =='X' and ox_oy =='X':
                                place_o = 3
                            elif thx_thy =='X' and tx_ty =='5' and ox_oy =='X':
                                place_o = 5
                            elif thx_thy =='X' and tx_ty =='X' and ox_oy =='7':
                                place_o = 7
                                
                            elif thx_oy =='1' and tx_oy =='X' and ox_oy =='X':
                                place_o = 1
                            elif thx_oy =='X' and tx_oy =='4' and ox_oy =='X':
                                place_o = 4
                            elif thx_oy =='X' and tx_oy =='X' and ox_oy =='7':
                                place_o = 7
                                
                            elif thx_ty =='2' and tx_ty =='X' and ox_ty =='X':
                                place_o = 2
                            elif thx_ty =='X' and tx_ty =='5' and ox_ty =='X':
                                place_o = 5
                            elif thx_ty =='X' and tx_ty =='X' and ox_ty =='8':
                                place_o = 8
                                
                            elif thx_thy =='3' and tx_thy =='X' and ox_thy =='X':
                                place_o = 3
                            elif thx_thy =='X' and tx_thy =='6' and ox_thy =='X':
                                place_o = 6
                            elif thx_thy =='X' and tx_thy =='X' and ox_thy =='9':
                                place_o = 9
                            
                            elif tx_ty =='5':
                                place_o = 5
                                
                            elif thx_oy =='1' or thx_thy =='3' or ox_oy =='7' or ox_thy =='9':
                                while True:
                                    corn = random.randint(1, 4)
                                    if corn == 1 and thx_oy =='1':
                                        place_o = 1
                                        break
                                    elif corn == 2 and thx_thy =='3':
                                        place_o = 3
                                        break
                                    elif corn == 3 and ox_oy =='7':
                                        place_o = 7
                                        break
                                    elif corn == 4 and ox_thy =='9':
                                        place_o = 9
                                        break
                                    else:
                                        break
                                    
                            elif 1 ==1:
                                while True:
                                    ran = random.randint(1, 9)
                                    if ran == 1 and thx_oy =='1':
                                        place_o = 1
                                        break
                                    
                                    elif ran == 2 and thx_ty =='2':
                                        place_o = 2
                                        break
                                    
                                    elif ran == 3 and thx_thy =='3':
                                        place_o = 3
                                        break
                                    
                                    elif ran == 4 and tx_oy =='4':
                                        place_o = 4
                                        break
                                    
                                    if ran == 5 and tx_ty =='5':
                                        place_o = 5
                                        break
                                    
                                    elif ran == 6 and tx_thy =='6':
                                        place_o = 6
                                        break
                                    
                                    elif ran == 7 and ox_oy =='7':
                                        place_o = 7
                                        break
                                    
                                    elif ran == 8 and ox_ty =='8':
                                        place_o = 8
                                        break

                                    elif ran == 9 and ox_thy =='9':
                                        place_o = 9
                                        break
                                    
                                    else:
                                        break

                            while True:
                                if place_o ==1 and thx_oy =="1":
                                    thx_oy = "O"
                                    break
                                elif place_o ==2 and thx_ty =="2":
                                    thx_ty = "O"
                                    break
                                elif place_o ==3 and thx_thy =="3":
                                    thx_thy = "O"
                                    break
                                elif place_o ==4 and tx_oy =="4":
                                    tx_oy = "O"
                                    break
                                elif place_o ==5 and tx_ty =="5":
                                    tx_ty = "O"
                                    break
                                elif place_o ==6 and tx_thy =="6":
                                    tx_thy = "O"
                                    break
                                elif place_o ==7 and ox_oy =="7":
                                    ox_oy = "O"
                                    break
                                elif place_o ==8 and ox_ty =="8":
                                    ox_ty = "O"
                                    break
                                elif place_o ==9 and ox_thy =="9":
                                    ox_thy = "O"
                                    break
                                else:
                                    print("you cant do that...")
                            lst_o = [ox_oy,ox_ty,ox_thy]
                            lst_t = [tx_oy,tx_ty,tx_thy]
                            lst_th = [thx_oy,thx_ty,thx_thy]

                            print(thx_oy,"|",thx_ty,"|",thx_thy)
                            print("-","-","-","-","-")
                            print(tx_oy,"|",tx_ty,"|",tx_thy)
                            print("-","-","-","-","-")
                            print(ox_oy,"|",ox_ty,"|",ox_thy)
                            
                            if lst_th == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif lst_t == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif lst_o == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy =='O' and tx_ty =='O' and ox_thy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_thy =='O' and tx_ty =='O' and ox_oy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy =='O' and tx_oy =='O' and ox_oy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_ty =='O' and tx_ty =='O' and ox_ty =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_thy =='O' and tx_thy =='O' and ox_thy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy != "1" and thx_ty != "2" and thx_thy != "3" and tx_oy != "4" and tx_ty != "5" and tx_thy != "6" and ox_oy != "7" and ox_ty != "8" and ox_thy != "9":
                                print("neither player won...")
                                break
                        for k in range(10):
                            winsound.Beep(1800, 200)    
                        time.sleep(5)
                        thx_oy = "1"
                        thx_ty = "2"
                        thx_thy = "3"
                        lst_th = [thx_oy,thx_ty,thx_thy]
                        tx_oy = "4"
                        tx_ty = "5"
                        tx_thy = "6"
                        lst_t = [tx_oy,tx_ty,tx_thy]
                        ox_oy = "7"
                        ox_ty = "8"
                        ox_thy = "9"
                        lst_o = [ox_oy,ox_ty,ox_thy]

                    elif oorx == 2:
                        print(thx_oy,"|",thx_ty,"|",thx_thy)
                        print("-","-","-","-","-")
                        print(tx_oy,"|",tx_ty,"|",tx_thy)
                        print("-","-","-","-","-")
                        print(ox_oy,"|",ox_ty,"|",ox_thy)
                        while True:
                            print("JAUNT move...")
                            if lst_th == ['O', '2', 'O']:
                                place_o = 2
                            elif lst_th == ['1', 'O', 'O']:
                                place_o = 1
                            elif lst_th == ['O', 'O', '3']:
                                place_o = 3
                                
                            elif lst_t == ['O', '5', 'O']:
                                place_o = 5
                            elif lst_t == ['4', 'O', 'O']:
                                place_o = 4
                            elif lst_t == ['O', 'O', '6']:
                                place_o = 6
                                
                            elif lst_o == ['O', '8', 'O']:
                                place_o = 8
                            elif lst_o == ['7', 'O', 'O']:
                                place_o = 7
                            elif lst_o == ['O', 'O', '9']:
                                place_o = 9
                                
                            elif thx_oy =='1' and tx_ty =='O' and ox_thy =='O':
                                place_o = 1
                            elif thx_oy =='O' and tx_ty =='5' and ox_thy =='O':
                                place_o = 5
                            elif thx_oy =='O' and tx_ty =='O' and ox_thy =='9':
                                place_o = 9
                                
                            elif thx_thy =='3' and tx_ty =='O' and ox_oy =='O':
                                place_o = 3
                            elif thx_thy =='O' and tx_ty =='5' and ox_oy =='O':
                                place_o = 5
                            elif thx_thy =='O' and tx_ty =='O' and ox_oy =='7':
                                place_o = 7
                                
                            elif thx_oy =='1' and tx_oy =='O' and ox_oy =='O':
                                place_o = 1
                            elif thx_oy =='O' and tx_oy =='4' and ox_oy =='O':
                                place_o = 4
                            elif thx_oy =='O' and tx_oy =='O' and ox_oy =='7':
                                place_o = 7
                                
                            elif thx_ty =='2' and tx_ty =='O' and ox_ty =='O':
                                place_o = 2
                            elif thx_ty =='O' and tx_ty =='5' and ox_ty =='O':
                                place_o = 5
                            elif thx_ty =='O' and tx_ty =='O' and ox_ty =='8':
                                place_o = 8
                                
                            elif thx_thy =='3' and tx_thy =='O' and ox_thy =='O':
                                place_o = 3
                            elif thx_thy =='O' and tx_thy =='6' and ox_thy =='O':
                                place_o = 6
                            elif thx_thy =='O' and tx_thy =='O' and ox_thy =='9':
                                place_o = 9


                            elif lst_th == ['X', '2', 'X']:
                                place_o = 2
                            elif lst_th == ['1', 'X', 'X']:
                                place_o = 1
                            elif lst_th == ['X', 'X', '3']:
                                place_o = 3
                                
                            elif lst_t == ['X', '5', 'X']:
                                place_o = 5
                            elif lst_t == ['4', 'X', 'X']:
                                place_o = 4
                            elif lst_t == ['X', 'X', '6']:
                                place_o = 6
                                
                            elif lst_o == ['X', '8', 'X']:
                                place_o = 8
                            elif lst_o == ['7', 'X', 'X']:
                                place_o = 7
                            elif lst_o == ['X', 'X', '9']:
                                place_o = 9
                                
                            elif thx_oy =='1' and tx_ty =='X' and ox_thy =='X':
                                place_o = 1
                            elif thx_oy =='X' and tx_ty =='5' and ox_thy =='X':
                                place_o = 5
                            elif thx_oy =='X' and tx_ty =='X' and ox_thy =='9':
                                place_o = 9
                                
                            elif thx_thy =='3' and tx_ty =='X' and ox_oy =='X':
                                place_o = 3
                            elif thx_thy =='X' and tx_ty =='5' and ox_oy =='X':
                                place_o = 5
                            elif thx_thy =='X' and tx_ty =='X' and ox_oy =='7':
                                place_o = 7
                                
                            elif thx_oy =='1' and tx_oy =='X' and ox_oy =='X':
                                place_o = 1
                            elif thx_oy =='X' and tx_oy =='4' and ox_oy =='X':
                                place_o = 4
                            elif thx_oy =='X' and tx_oy =='X' and ox_oy =='7':
                                place_o = 7
                                
                            elif thx_ty =='2' and tx_ty =='X' and ox_ty =='X':
                                place_o = 2
                            elif thx_ty =='X' and tx_ty =='5' and ox_ty =='X':
                                place_o = 5
                            elif thx_ty =='X' and tx_ty =='X' and ox_ty =='8':
                                place_o = 8
                                
                            elif thx_thy =='3' and tx_thy =='X' and ox_thy =='X':
                                place_o = 3
                            elif thx_thy =='X' and tx_thy =='6' and ox_thy =='X':
                                place_o = 6
                            elif thx_thy =='X' and tx_thy =='X' and ox_thy =='9':
                                place_o = 9
                            
                            elif tx_ty =='5':
                                place_o = 5
                                
                            elif thx_oy =='1' or thx_thy =='3' or ox_oy =='7' or ox_thy =='9':
                                while True:
                                    corn = random.randint(1, 4)
                                    if corn == 1 and thx_oy =='1':
                                        place_o = 1
                                        break
                                    elif corn == 2 and thx_thy =='3':
                                        place_o = 3
                                        break
                                    elif corn == 3 and ox_oy =='7':
                                        place_o = 7
                                        break
                                    elif corn == 4 and ox_thy =='9':
                                        place_o = 9
                                        break
                                    else:
                                        break
                                    
                            elif 1 ==1:
                                while True:
                                    ran = random.randint(1, 9)
                                    if ran == 1 and thx_oy =='1':
                                        place_o = 1
                                        break
                                    
                                    elif ran == 2 and thx_ty =='2':
                                        place_o = 2
                                        break
                                    
                                    elif ran == 3 and thx_thy =='3':
                                        place_o = 3
                                        break
                                    
                                    elif ran == 4 and tx_oy =='4':
                                        place_o = 4
                                        break
                                    
                                    if ran == 5 and tx_ty =='5':
                                        place_o = 5
                                        break
                                    
                                    elif ran == 6 and tx_thy =='6':
                                        place_o = 6
                                        break
                                    
                                    elif ran == 7 and ox_oy =='7':
                                        place_o = 7
                                        break
                                    
                                    elif ran == 8 and ox_ty =='8':
                                        place_o = 8
                                        break

                                    elif ran == 9 and ox_thy =='9':
                                        place_o = 9
                                        break
                                    
                                    else:
                                        break

                            while True:
                                if place_o ==1 and thx_oy =="1":
                                    thx_oy = "O"
                                    break
                                elif place_o ==2 and thx_ty =="2":
                                    thx_ty = "O"
                                    break
                                elif place_o ==3 and thx_thy =="3":
                                    thx_thy = "O"
                                    break
                                elif place_o ==4 and tx_oy =="4":
                                    tx_oy = "O"
                                    break
                                elif place_o ==5 and tx_ty =="5":
                                    tx_ty = "O"
                                    break
                                elif place_o ==6 and tx_thy =="6":
                                    tx_thy = "O"
                                    break
                                elif place_o ==7 and ox_oy =="7":
                                    ox_oy = "O"
                                    break
                                elif place_o ==8 and ox_ty =="8":
                                    ox_ty = "O"
                                    break
                                elif place_o ==9 and ox_thy =="9":
                                    ox_thy = "O"
                                    break
                                else:
                                    print("you cant do that...")
                            lst_o = [ox_oy,ox_ty,ox_thy]
                            lst_t = [tx_oy,tx_ty,tx_thy]
                            lst_th = [thx_oy,thx_ty,thx_thy]

                            print(thx_oy,"|",thx_ty,"|",thx_thy)
                            print("-","-","-","-","-")
                            print(tx_oy,"|",tx_ty,"|",tx_thy)
                            print("-","-","-","-","-")
                            print(ox_oy,"|",ox_ty,"|",ox_thy)
                            
                            if lst_th == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif lst_t == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif lst_o == ['O', 'O', 'O']:
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy =='O' and tx_ty =='O' and ox_thy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_thy =='O' and tx_ty =='O' and ox_oy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy =='O' and tx_oy =='O' and ox_oy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_ty =='O' and tx_ty =='O' and ox_ty =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_thy =='O' and tx_thy =='O' and ox_thy =='O':
                                print("\n\nplayer O won\n\n")
                                o_won += 1
                                break
                            elif thx_oy != "1" and thx_ty != "2" and thx_thy != "3" and tx_oy != "4" and tx_ty != "5" and tx_thy != "6" and ox_oy != "7" and ox_ty != "8" and ox_thy != "9":
                                print("neither player won...")
                                break    

                            while True:
                                place_x =int(input("chose a place for X (1-9): "))
                                if place_x ==1 and thx_oy =="1":
                                    thx_oy = "X"
                                    break
                                elif place_x ==2 and thx_ty =="2":
                                    thx_ty = "X"
                                    break
                                elif place_x ==3 and thx_thy =="3":
                                    thx_thy = "X"
                                    break
                                elif place_x ==4 and tx_oy =="4":
                                    tx_oy = "X"
                                    break
                                elif place_x ==5 and tx_ty =="5":
                                    tx_ty = "X"
                                    break
                                elif place_x ==6 and tx_thy =="6":
                                    tx_thy = "X"
                                    break
                                elif place_x ==7 and ox_oy =="7":
                                    ox_oy = "X"
                                    break
                                elif place_x ==8 and ox_ty =="8":
                                    ox_ty = "X"
                                    break
                                elif place_x ==9 and ox_thy =="9":
                                    ox_thy = "X"
                                    break
                                else:
                                    print("you cant do that...")
                            lst_o = [ox_oy,ox_ty,ox_thy]
                            lst_t = [tx_oy,tx_ty,tx_thy]
                            lst_th = [thx_oy,thx_ty,thx_thy]

                            print(thx_oy,"|",thx_ty,"|",thx_thy)
                            print("-","-","-","-","-")
                            print(tx_oy,"|",tx_ty,"|",tx_thy)
                            print("-","-","-","-","-")
                            print(ox_oy,"|",ox_ty,"|",ox_thy)
                            
                            if lst_th == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif lst_t == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif lst_o == ['X', 'X', 'X']:
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy =='X' and tx_ty =='X' and ox_thy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_thy =='X' and tx_ty =='X' and ox_oy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy =='X' and tx_oy =='X' and ox_oy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_ty =='X' and tx_ty =='X' and ox_ty =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_thy =='X' and tx_thy =='X' and ox_thy =='X':
                                print("\n\nplayer X won\n\n")
                                x_won += 1
                                break
                            elif thx_oy != "1" and thx_ty != "2" and thx_thy != "3" and tx_oy != "4" and tx_ty != "5" and tx_thy != "6" and ox_oy != "7" and ox_ty != "8" and ox_thy != "9":
                                print("neither player won...")
                                break
                        for k in range(10):
                            winsound.Beep(1800, 200)    
                        time.sleep(5)
                        thx_oy = "1"
                        thx_ty = "2"
                        thx_thy = "3"
                        lst_th = [thx_oy,thx_ty,thx_thy]
                        tx_oy = "4"
                        tx_ty = "5"
                        tx_thy = "6"
                        lst_t = [tx_oy,tx_ty,tx_thy]
                        ox_oy = "7"
                        ox_ty = "8"
                        ox_thy = "9"
                        lst_o = [ox_oy,ox_ty,ox_thy]  










        
    elif op =='PARTY TIME':
                        mod.party_time()
    elif op =='BOMB!!!':
                        mod.bomb()
    elif op =='EASTER EGGS':
                        mod.easter_eggs()
    elif op =='im to weak...':
                        mod.star_wars()
    elif op =='no...':
                        mod.no()
    elif op =='who is yonathan?':
                        mod.me()
    elif op =='all hail the magic conch shell!':
                        mod.spongebob()            
    else: 
        print("\n\ni dont know how to do that, yet... :)\n\n")
        
winsound.Beep(freq, 200)
