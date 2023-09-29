# _________________________________________________________________________________
#               Temperature checking using class and object
# _________________________________________________________________________________


class Electricitybillcalculator:
    def __init__(self, customer_name, unit):
        self.customer_name = customer_name
        self.unit = unit
        self.base_amount = 1
        self.additional_price_per_unit = 8.60

    def calculateprice(self):
        if self.unit <= 1:
            total_cost = self.base_amount
        else:
            additional_unit = self.unit - 1
            additional_cost = additional_unit * self.additional_price_per_unit
            total_cost = self.base_amount + additional_cost
        return total_cost

try:
    num_customer = int(input("Enter the number of customer: "))
    if num_customer <= 0:
        print('Number of customer should be greater than 1.')
    else:
        with open("Bidudhkofile.txt", 'w')as file:
            for i in range(num_customer):
                customer_name = input(f'Enter the name of customer {i+1} = ')
                consumed_unit = float(input(f'Enter the consumed unit by {customer_name}: '))

                if consumed_unit >= 0:
                    bill_calculator = Electricitybillcalculator(
                        customer_name, consumed_unit)
                    bill_amount = bill_calculator.calculateprice()
                    output = f'{customer_name}, electricity bill is {bill_amount:.2f}\n'
                    print(output)
                    file.write(output)
                else:
                    print(
                        'Invalid input, please input positive number.')

except ValueError:
    print('Invalid input. Please input valid number of customer.')


# _____________________________________________________________________________________
#               Temperature checking using class and Dictionary
# _____________________________________________________________________________________


class Temperaturetracker():
    def __init__(self):
        self.company_name = ""
        self.company_address = " "
        self.num_days = 0
        self.temperature_record = []
        self.temperature_category = {'very_hot': 0, 'plesant': 0, 'very_cold': 0}
        self.temperature_range = {'very_hot': range(60,101), 'plesant': range(30,60), 'very_cold': range(0,30)}

    def initialDisplay(self, company_name, company_address):
        self.company_name = company_name
        self.company_address = company_address
        print(f'{self.company_name},--Temperature Tracking System \n{self.company_address}')

    def inputinformation(self):
        self.num_days = int(input("Enter a number of days to record: "))
        print(f"Input the temperature for {self.num_days} days.")
        for i in range(self.num_days):
            temperature = int(input(f"Input temperature for day: [{i + 1}] = "))
            self.temperature_record.append(temperature)

    def Calculatetemperature(self):
        total_temp = sum(self.temperature_record)
        average_temp = round(total_temp/self.num_days)
        for temp in self.temperature_record:
            for category, temp_range in self.temperature_range.items():
                if temp in temp_range:
                    self.temperature_category[category]+= 1
                    break
        return average_temp

    def Categorycheck(self, temp):
        if temp in self.temperature_range['very_hot']:
            return 'very_hot'
        elif temp in self.temperature_range['plesant']:
            return 'plesant'
        elif temp in self.temperature_range['very_cold']:
            return 'very_cold'
        else:
            return 'Tempreture out of range.'

    def displayInformation(self):
        print("_"*40)
        print('Daily Temperature Record system: ')
        for i, temp in enumerate(self.temperature_record):
            category = self.Categorycheck(temp)
            print(f'The temperature of day [{i+1}] = {temp} celcuis {category} ')
        print(f'The average temperature for {self.num_days} days = {self.Calculatetemperature()} celsius. ')

    def finaldisplay(self):
        print(f'\n Number of hot days = {self.temperature_category["very_hot"]} days.')
        print(f'\n Number of plesant days = {self.temperature_category["plesant"]} days. ')
        print(f'\n Number of cold days = {self.temperature_category["very_cold"]} days.')

#functioncall
tt = Temperaturetracker()
tt.initialDisplay('Unicampus', 'Maitidevi, Kathmandu')
tt.inputinformation()
tt.displayInformation()
tt.finaldisplay()
