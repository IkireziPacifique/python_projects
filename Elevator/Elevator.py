# Creating Elevator Class
class Elevator:
    # Elevator Open method
    def open_elevator(self):
        enter_button = input("Enter Open if you want to use the elevator: ")
        if enter_button.lower() == "open":
            for x in range(3, 0, -1):
                print("floor" , x)
            print("Please Enter...the elevator is open now")
            self.close_elevator()
        else:
            exit('Next time enter a valid input')
    # Elevator Close method
    def close_elevator(self):
        print("Elevator closed")
    # Move Elevator method
    def move_elevator(self):
        # User input of the floor to go to
        floor = input("Please click on the number of the floor you are going to :")
        if floor:
            if floor == "1":
                print("We are going to floor 1")
                for x in range(1,1):
                    print("floor", x)
                print("Destination reached")
            if floor == "2":
                print("We are going to floor 2")
                x = 1
                for x in range(1, 3):
                    print("floor", x)
                print("Destination reached")
            if floor == "3":
                print("We are going to floor 3")
                for x in range(1, 4):
                    print("floor", x)
                print("Destination reached")




