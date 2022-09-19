# --------Cab Service---------
import numpy as np

print('  ******************* Welcome to THE QUCIK CAB Service*******************')
print(' ')

# Create Super Class
class Vehicle:
    def __init__(self, vehicleNumber, driver, driverMobile, capacity):
        self.__vehicleNumber = vehicleNumber
        self.__driver = driver
        self.__driverMobile = driverMobile
        self.__capacity = capacity

    # Use getters and setters
    def getCapacity(self):
        return self.__capacity

    def setCapacity(self):
        return self.__capacity

    def getVehicleNumber(self):
        return self.__vehicleNumber

    def setVehicleNumber(self):
        return self.__vehicleNumber

    def getDriver(self):
        return self.__driver

    def setDriver(self):
        return self.__driver

    def getDriverMobile(self):
        return self.__driverMobile

    def setDriverMobile(self):
        return self.__driverMobile

# Create a sub class
class Car(Vehicle):
    cl = np.array([['WP SX 7325', 'Sarath', '0710002548', '3', 'non AC'], ['SP ABC 5465', 'Amila', '0775263687', '4', 'AC']])
    numberOfCars = int(len(cl))
    car1driver = cl[0, 1]

    # Inherit from the super class
    def __init__(self, vehicleNumber, driver, driverMobile, capacity, condition):
        super(Car, self).__init__(vehicleNumber, driver, driverMobile, capacity)
        self.__condition = condition

    def carAssign(self):
        return 'The assigned driver is ' + self.car1driver + '.'

    def carHire(self) -> cl:
        return "The available amount of cars are : " + str(self.numberOfCars - 1)

class Van(Vehicle):
    vl = np.array([['WP SX 7225', 'Kapila', '0710002548', '3', 'non AC'], ['SP ABC 5565', 'Kumara', '0775263687', '4', 'AC']])
    numberOfVans = int(len(vl))
    van1driver = vl[0, 1]

    def __init__(self, vehicleNumber, driver, driverMobile, capacity, condition):
        super(Van, self).__init__(vehicleNumber, driver, driverMobile, capacity)
        self.__condition = condition

    def vanAssign(self):
        return 'The assigned driver is ' + self.van1driver + '.'

    def vanHire(self) -> vl:
        return "The available amount of vans are : " + str(self.numberOfVans - 1)

class ThreeWheel(Vehicle):
    twl = np.array([['WP SX 7225', 'Amith', '0710002548', '3'], ['SP ABC 5565', 'Sisira', '0775263687', '3']])
    numberOfThreeWheels = int(len(twl))
    tw1driver = twl[0, 1]

    def __init__(self, vehicleNumber, driver, driverMobile, capacity):
        super(ThreeWheel, self).__init__(vehicleNumber, driver, driverMobile, capacity)

    def threeWheelAssign(self):
        return 'The assigned driver is ' + self.tw1driver + '.'

    def threeWheelHire(self) -> twl:
        return "The available amount of three wheels are : " + str(self.numberOfThreeWheels - 1)

class Truck(Vehicle):
    tl = np.array([['WP SX 7225', 'Shantha', '0710002548', '10ft'], ['SP ABC 5565', 'Sugath', '0775263687', '12ft']])
    numberOfTrucks = int(len(tl))
    t1driver = tl[0, 1]

    def __init__(self, vehicleNumber, driver, driverMobile, capacity):
        super(Truck, self).__init__(vehicleNumber, driver, driverMobile, capacity)

    def truckAssign(self):
        return 'The assigned driver is ' + self.t1driver + '.'

    def truckHire(self) -> tl:
        return "The available amount of trucks are : " + str(self.numberOfTrucks - 1)

class Lorry(Vehicle):
    lrl = np.array([['WP SX 7225', 'Ananda', '0710002548', '3000kg'], ['SP ABC 5565', 'Sujith', '0775263687', '3500kg']])
    numberOfLorries = int(len(lrl))
    l1driver = lrl[0, 1]

    def __init__(self, vehicleNumber, driver, driverMobile, capacity):
        super(Lorry, self).__init__(vehicleNumber, driver, driverMobile, capacity)

    def truckAssign(self):
        return 'The assigned driver is ' + self.l1driver + '.'

    def truckHire(self) -> lrl:
        return "The available amount of lorries are : " + str(self.numberOfLorries - 1)

#Select the user is customer of staff
customer = input('Do you want to hire a vehicle (yes/no)? ')
print(' ')
if customer == 'yes':
    #select the category
    print('Which type of vehicle do you want? ')
    print(str(1) + ' - CAR')
    print(str(2) + ' - VAN')
    print(str(3) + ' - THREE WHEEL')
    print(str(4) + ' - TRUCKS')
    print(str(5) + ' - LORRY')

    vehicleType = input('Give me the number : ')
    print(' ')
    if vehicleType == '1':
        #Show available cabs in the system
        print('Available Cars : ' + str(Car.numberOfCars))
        print(' ')
        #assign a hire
        hire = input('Do you want to hire a cab? ')
        if hire == 'yes':
            #call the array
            print('Your cab driver is ' + str(Car.cl[0, 1]) + ' and cab number is ' + str(Car.cl[0, 0]))
            #remove the hire cab from available cabs total
            Car.numberOfCars = Car.numberOfCars - 1
            print('Current Available cabs are : ' + str(Car.numberOfCars))
            print('')

            end = input('Do you end the ride? ')
            if end == 'yes':
                print('Thank you customer. Stay safe. Have a Nice Day...')
                # Add the hire cab from available cabs total
                Car.numberOfCars = Car.numberOfCars + 1
                print('Current Available cabs are : ' + str(Car.numberOfCars))

            else:
                pass

        elif hire == 'no':
            print('Thank you for visiting. Have a Nice Day.')

        else:
            pass

    elif vehicleType == '2':
        print('Available Vans : ' + str(Van.numberOfVans))
        print(' ')
        # assign a hire
        hire = input('Do you want to hire a cab? ')
        if hire == 'yes':
            # call the array
            print('Your cab driver is ' + str(Van.vl[0, 1]) + ' and cab number is ' + str(Van.vl[0, 0]))
            # remove the hire cab from available cabs total
            Van.numberOfVans = Van.numberOfVans - 1
            print('Current Available cabs are : ' + str(Van.numberOfVans))
            print('')

            end = input('Do you end the ride? ')
            if end == 'yes':
                print('Thank you customer. Stay safe. Have a Nice Day...')
                # Add the hire cab from available cabs total
                Van.numberOfVans = Van.numberOfVans + 1
                print('Current Available cabs are : ' + str(Van.numberOfVans))

        elif hire == 'no':
            print('Thank you for visiting. Have a Nice Day.')

        else:
            pass

    elif vehicleType == '3':
        print('Available Three Wheels : ' + str(ThreeWheel.numberOfThreeWheels))
        print(' ')
        # assign a hire
        hire = input('Do you want to hire a cab? ')
        if hire == 'yes':
            # call the array
            print('Your cab driver is ' + str(ThreeWheel.twl[0, 1]) + ' and cab number is ' + str(ThreeWheel.twl[0, 0]))
            # remove the hire cab from available cabs total
            ThreeWheel.numberOfThreeWheels = ThreeWheel.numberOfThreeWheels - 1
            print('Current Available cabs are : ' + str(ThreeWheel.numberOfThreeWheels))
            print('')

            end = input('Do you end the ride? ')
            if end == 'yes':
                print('Thank you customer. Stay safe. Have a Nice Day...')
                # Add the hire cab from available cabs total
                ThreeWheel.numberOfThreeWheels = ThreeWheel.numberOfThreeWheels + 1
                print('Current Available cabs are : ' + str(ThreeWheel.numberOfThreeWheels))

        elif hire == 'no':
            print('Thank you for visiting. Have a Nice Day.')

        else:
            pass

    elif vehicleType == '4':
        print('Available Trucks : ' + str(Truck.numberOfTrucks))
        print(' ')
        # assign a hire
        hire = input('Do you want to hire a cab? ')
        if hire == 'yes':
            # call the array
            print('Your cab driver is ' + str(Truck.tl[0, 1]) + ' and cab number is ' + str(Truck.tl[0, 0]))
            # remove the hire cab from available cabs total
            Truck.numberOfTrucks = Truck.numberOfTrucks - 1
            print('Current Available cabs are : ' + str(Truck.numberOfTrucks))
            print('')

            end = input('Do you end the ride? ')
            if end == 'yes':
                print('Thank you customer. Stay safe. Have a Nice Day...')
                # Add the hire cab from available cabs total
                Truck.numberOfTrucks = Truck.numberOfTrucks + 1
                print('Current Available cabs are : ' + str(Truck.numberOfTrucks))

        elif hire == 'no':
            print('Thank you for visiting. Have a Nice Day.')

        else:
            pass

    elif vehicleType == '5':
        print('Available Lorries : ' + str(Lorry.numberOfLorries))
        print(' ')
        # assign a hire
        hire = input('Do you want to hire a cab? ')
        if hire == 'yes':
            # call the array
            print('Your cab driver is ' + str(Lorry.lrl[0, 1]) + ' and cab number is ' + str(Lorry.lrl[0, 0]))
            # remove the hire cab from available cabs total
            Lorry.numberOfLorries = Lorry.numberOfLorries - 1
            print('Current Available cabs are : ' + str(Lorry.numberOfLorries))
            print('')

            end = input('Do you end the ride? ')
            if end == 'yes':
                print('Thank you customer. Stay safe. Have a Nice Day...')
                # Add the hire Lorry to available Lorries total
                Lorry.numberOfLorries = Lorry.numberOfLorries + 1
                print('Current Available Lorries are : ' + str(Lorry.numberOfLorries))

        elif hire == 'no':
            print('Thank you for visiting. Have a Nice Day.')

        else:
            pass

    else:
        print('Sorry customer, there is no vehicle type. Please enter the correct vehicle type again...')

elif customer == 'no':
    staff = input('Are you a staff member? ')
    print(' ')
    pw = 'abc@123'
    password = input('Please Enter The Password : ')

    if password == pw:
        print('What is the category do you want to add a vehicle? ')
        print(str(1) + ' - CAR')
        print(str(2) + ' - VAN')
        print(str(3) + ' - THREE WHEEL')
        print(str(4) + ' - TRUCKS')
        print(str(5) + ' - LORRY')
        category = input('Please give me the category number : ')
        print(' ')

        if category == '1':
            carList = []
            n = int(input('How many vehicles do you want to add : '))
            for i in range(0, n):
                cl = [input('Vehicle Number : '), input('Driver : '), input('Driver Mobile : '),
                      input('Capacity : '), input('Condition : ')]
                carList.append(cl)
                Car.numberOfCars = len(carList)
                print('The car added successfully...')
                print('The number of cars available is : ' + str(Car.numberOfCars))
                print(cl)

                #remove the enter value
                remove = input('Do you want to remove a vehicle? ')
                if remove == 'yes':
                    print(cl)
                    el = int(input('Which  element of vehicle do you want to remove from the above list (consider first element as 0 ? '))
                    carList.pop(el)
                    print('The number of cars available is : ' + str(Car.numberOfCars))
                    print(cl)
                else:
                    print('The number of cars available is : ' + str(Car.numberOfCars))
                    print(cl)

        elif category == '2':
            vanList = []
            n = int(input('How many vehicles do you want to add : '))
            for i in range(0, n):
                vl = [input('Vehicle Number : '), input('Driver : '), input('Driver Mobile : '),
                      input('Capacity : '), input('Condition : ')]
                vanList.append(vl)
                Van.numberOfVans = len(vanList)
                print('The van added successfully...')
                print('The number of vans available is : ' + str(Van.numberOfVans))
                print(vl)

                remove = input('Do you want to remove a vehicle? ')
                if remove == 'yes':
                    print(vl)
                    el = int(input('Which  element of vehicle do you want to remove from the above list(consider first element as 0? '))
                    vanList.pop(el)
                    print('The number of vans available is : ' + str(Van.numberOfVans))
                    print(vl)

                else:
                    print('The number of vans available is : ' + str(Van.numberOfVans))
                    print(vl)

        elif category == '3':
            threeWheelList = []
            n = int(input('How many vehicles do you want to add : '))
            for i in range(0, n):
                twl = [input('Vehicle Number : '), input('Driver : '), input('Driver Mobile : '),
                       input('Capacity : ')]
                threeWheelList.append(twl)
                ThreeWheel.numberOfThreeWheels = len(threeWheelList)
                print('The three wheel added successfully...')
                print('The number of three wheels available is : ' + str(ThreeWheel.numberOfThreeWheels))
                print(twl)

                remove = input('Do you want to remove a vehicle? ')
                if remove == 'yes':
                    print(twl)
                    el = int(input(
                        'Which  element of vehicle do you want to remove from the above list(consider first element as 0? '))
                    threeWheelList.pop(el)
                    print('The number of three wheels available is : ' + str(ThreeWheel.numberOfThreeWheels))
                    print(twl)
                else:
                    print('The number of three wheels available is : ' + str(ThreeWheel.numberOfThreeWheels))
                    print(twl)

        elif category == '4':
            truckList = []
            n = int(input('How many vehicles do you want to add : '))
            for i in range(0, n):
                tl = [input('Vehicle Number : '), input('Driver : '), input('Driver Mobile : '),
                      input('Capacity : ')]
                truckList.append(tl)
                Truck.numberOfTrucks = len(truckList)
                print('The Truck added successfully...')
                print('The number of trucks available is : ' + str(Truck.numberOfTrucks))
                print(tl)

                remove = input('Do you want to remove a vehicle? ')
                if remove == 'yes':
                    print(tl)
                    el = int(input(
                        'Which  element of vehicle do you want to remove from the above list(consider first element as 0? '))
                    truckList.pop(el)
                    print('The number of trucks available is : ' + str(Truck.numberOfTrucks))
                    print(tl)
                else:
                    print('The number of trucks available is : ' + str(Truck.numberOfTrucks))
                    print(tl)

        elif category == '5':
            lorryList = []
            n = int(input('How many vehicles do you want to add : '))
            for i in range(0, n):
                lrl = [input('Vehicle Number : '), input('Driver : '), input('Driver Mobile : '),
                       input('Capacity : ')]
                lorryList.append(lrl)
                Lorry.numberOfLorries = len(lorryList)
                print('The lorry added successfully...')
                print('The number of lorries available is : ' + str(Lorry.numberOfLorries))
                print(lrl)

                remove = input('Do you want to remove a vehicle? ')
                if remove == 'yes':
                    print(lrl)
                    el = int(input(
                        'Which  element of vehicle do you want to remove from the above list(consider first element as 0? '))
                    lorryList.pop(el)
                    print('The number of lorries available is : ' + str(Lorry.numberOfLorries))
                    print(lrl)
                else:
                    print('The lorry added successfully...')
                    print('The number of lorries available is : ' + str(Lorry.numberOfLorries))

        else:
            print('Please select the correct category again...')

    else:
        print('Sorry, Access Denied...')

else:
    print('Sorry Customer, There are no vehicle to hire as your preference. Thank you for visiting. Have a Nice Day')
