
# form = 1

# user_guess = 0
# max_guess = 3
user_input = ''
car_started = 0
car_stopped = 0

while user_input.lower() != 'quit':
    user_input = input("> ").lower()
    if user_input == "help":
        print('''
    start - to start the car
    stop - to stop the car
    quit - to exit
        ''')
    elif user_input == "start":

        if car_started < 1:
            print("Car started...Ready to go!")
        else:
            print("Car already started... man")
        car_started += 1
    elif user_input == "stop":
        if car_stopped < 1:
            print("Car stopped.")
        else:
            print("Car already stopped... man")
        car_stopped += 1
    elif user_input == 'quit':
        break
    else:
        print('''
    I don't understand what you typed...
    type 'help' for more 
        ''')
        # user_guess += 1
