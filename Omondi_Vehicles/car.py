# Calling the parent class
from vehicle import Vehicle

#Creating the child class
class Car(Vehicle):
    # method to calculate the carbon footprint
    def carbon_footprint(self, all_vehicles):
        car_to_see = input("Please enter the plate number of a car you want: ")
        if car_to_see:
            for x in all_vehicles:
                if car_to_see == x.plate_number:
                    years_old = 2020 - x.release_year
                    miles = int(input("Miles it has covered: "))
                    gallons = int(input("gallons per mile: "))
                    co2 = int(input("grams of co2 per gallon: "))
                    calculator = years_old * 12000 * miles * 15 * gallons * 9 * co2
                    print("Carbon Footprint of", x.brand , x.model , "with" , x.plate_number ,
                          "Plate number is:" , calculator)