# Car_gamming......
command = ""
while True: # command != "quite" :
    command = input("> ").lower()
    if command == "start" :
        print("Car started.......")
    elif command == "stop" :
        print("Car stop..........")
    elif command == "help" :
        print("""
        Start - to start the car
        Stop  - to stop the car
        Quite - to quite
        """)
    elif command == "quite" :
        break
    else:
        print('Sorry, i dont understand that...')