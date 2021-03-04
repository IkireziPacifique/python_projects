#Author Pacifique Linda IKIREZI
#Question 2 Kigali height Elevator control system

# Importing class
from Elevator import Elevator

# Greeting the user & showing the state
print("Hey there")
print("The elevator is currently closed!")
# Calling method to open elevator
open = Elevator()
open.open_elevator()
# Calling method to move elevator
move = Elevator()
move.move_elevator()
