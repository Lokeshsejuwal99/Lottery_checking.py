#____________________________________________________________________________________________________________________________________________
#                                       _______________________________________________________
#                                               TAX calculation using Dictionary
#                                        _______________________________________________________
# _____________________________________________________________________________________________________________________________

def intitial_display():
    date = 1
    heading = f'''  TAX Calculator
                Kathmandu, Nepal
            {date}'''
    return heading

def input_info():
    customers_info = []
    num = int(input('Enter the number of customer:'))
    for i in range(num):
        customer_info = []
        name = input('Enter the name: ')
        address = input('Enter the Address: ')
        married_status = input('Married Status(M/U): ')
        monthly_income = int(input('Enter the monthly income: '))
        customer_info.append(name)
        customer_info.append(address)
        customer_info.append(married_status)
        customer_info.append(monthly_income)
        customers_info.append(customer_info)
    print(customers_info)
    return num, customers_info

def tax_Unmarried(annual_income):
    if annual_income <= 500000:
        tax_per = 1
        income_after_tax = (annual_income * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    elif annual_income > 500000 and annual_income <= 700000:
        tax_per = 10
        income_after_tax = (500000 * 1) / 100 + ((annual_income - 500000) * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    elif annual_income > 700000 and annual_income <= 1000000:
        tax_per = 20
        income_after_tax = (500000 * 1) / 100 + ((700000 - 500000) * 10) / 100 + (
                    (annual_income - 700000) * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    elif annual_income > 1000000 and annual_income <= 2000000:
        tax_per = 30
        income_after_tax = (500000 * 1) / 100 + ((700000 - 500000) * 10) / 100 + ((1000000 - 700000) * 20) / 100 + (
                    (annual_income - 1000000) * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    elif annual_income > 2000000 and annual_income <= 5000000:
        tax_per = 36
        income_after_tax = (500000 * 1) / 100 + ((700000 - 500000) * 10) / 100 + ((1000000 - 700000) * 20) / 100 + (
                    (2000000 - 1000000) * 1) / 100 + ((annual_income - 5000000) * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    else:
        tax_per = 39
        income_after_tax = (500000 * 1) / 100 + ((700000 - 500000) * 10) / 100 + ((1000000 - 700000) * 20) / 100 + (
                    (2000000 - 1000000) * 1) / 100 + ((5000000 - 2000000) * 36) / 100 + (
                                       (annual_income - 5000000) * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    return annual_income, income_after_tax, annual_income_after_tax

def tax_married(annual_income):
    if annual_income <= 600000:
        tax_per = 1
        income_after_tax = (annual_income * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    elif annual_income > 600000 and annual_income <= 800000:
        tax_per = 10
        income_after_tax = (600000 * 1) / 100 + ((annual_income - 600000) * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    elif annual_income > 800000 and annual_income <= 1100000:
        tax_per = 20
        income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + (
                    (annual_income - 800000) * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    elif annual_income > 1100000 and annual_income <= 2000000:
        tax_per = 30
        income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((1100000 - 800000) * 20) / 100 + (
                    (annual_income - 1100000) * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    elif annual_income > 2000000 and annual_income <= 5000000:
        tax_per = 36
        income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((1100000 - 800000) * 20) / 100 + (
                    (2000000 - 1100000) * 1) / 100 + ((annual_income - 5000000) * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    else:
        tax_per = 39
        income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((1100000 - 800000) * 20) / 100 + (
                    (2000000 - 1100000) * 1) / 100 + ((5000000 - 2000000) * 36) / 100 + (
                                       (annual_income - 5000000) * tax_per) / 100
        annual_income_after_tax = annual_income - income_after_tax
    return annual_income, income_after_tax, annual_income_after_tax

def tax_calculation(status, income):
    yearly_income = income * 12
    if status == 'U' or status == 'u':
        annual_income, income_after_tax, annual_income_after_tax = tax_Unmarried(yearly_income)
    elif status == 'M' or status == 'm':
        annual_income, income_after_tax, annual_income_after_tax = tax_married(yearly_income)
    return annual_income, income_after_tax, annual_income_after_tax


def value_print(cust_name, cust_address, cust_status, cust_annual_income, Income_after_tax, annual_income_a_tax):
    cust_info = f'''Name: {cust_name}\t\t
Address: {cust_address}
Married Status:{cust_status}
Total Annual Income: {cust_annual_income}
Tax Income:{Income_after_tax}
Income after tax: {annual_income_a_tax}'''
    return cust_info

def final_print():
    num, customers_Info = input_info()
    initial = intitial_display()
    for i in range(num):
        annual_income, income_after_tax, annual_income_after_tax = tax_calculation(customers_Info[i][2],
                                                                                   customers_Info[i][3])
        print(initial)
        value = value_print(customers_Info[i][0], customers_Info[i][1], customers_Info[i][2], annual_income,
                            income_after_tax, annual_income_after_tax)
        print(value)

        with open(file_path, 'w') as file:
            file.write(initial + "\n")
            file.write(value)

file_path = input('Enter a file name to save on directory: ')
final_print()


# ____________________________________________________________________________________________________________________________________________
#                                       _______________________________________________________
#                                               TAX calculation using Class and Object
#                                        _______________________________________________________
# ____________________________________________________________________________________________________________________________________________

class TaxCalculator:
    def __init__(self):
        self.company_name = ''
        self.date = "September 16, 2023"
        self.customers_info = []

    def initial_display(self):
        self.company_name = input("Enter the company name: ")
        display = f'''{self.company_name} TAX Calculator
        Maitidevi, Kathmandu
        {self.date}'''
        return display

    def input_info(self):
        num = int(input('Enter the number of customer: '))
        for i in range(num):
            cust_info = []
            name = input('Enter staff name: ')
            address = input('Enter staff address: ')
            married = input('Enter you marrial statues: ')
            monthly_income = int(input('Enter monthly income: '))
            self.customers_info.append(name)
            self.customers_info.append(address)
            self.customers_info.append(married)
            self.customers_info.append(monthly_income)
            self.customers_info.append(cust_info)
        print(self.customers_info)
        print(num, self.customers_info)
    def tax_Unmarried(self, annual_income):
        if annual_income <= 500000:
            tax_per = 1
            income_after_tax = annual_income * 0.01
            annual_income_after_tax = (annual_income - income_after_tax)
        elif annual_income > 500000 and annual_income <= 700000:
            tax_per = 10
            income_after_tax = 500000 * 0.01 + (annual_income - 500000) * 0.1
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 700000 and annual_income <= 1000000:
            tax_per = 20
            income_after_tax = 500000 * 0.01 + (700000 - 500000) * 0.1 + (annual_income - 700000) * 0.2
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 1000000 and annual_income <= 2000000:
            tax_per = 30
            income_after_tax = 500000 * 0.01 + (700000 - 500000) * 0.1 + (1000000 - 700000) * 0.2 + (annual_income - 1000000) * 0.3
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 2000000 and annual_income <= 5000000:
            tax_per = 36
            income_after_tax = 500000 * 0.01 + (700000 - 500000) * 0.1 + (1000000 - 700000) * 0.2 + (2000000 - 1000000) * 0.3 + (annual_income - 5000000) * 0.36
            annual_income_after_tax = annual_income - income_after_tax
        else:
            tax_per = 39
            income_after_tax = 500000 * 0.01 + (700000 - 500000) * 0.1 + (1000000 - 700000) * 0.2 + (2000000 - 1000000) * 0.3 + (5000000 - 2000000) * 0.36 + (annual_income - 5000000) * 0.39
            annual_income_after_tax = annual_income - income_after_tax

        return annual_income, income_after_tax, annual_income_after_tax

    def tax_married(self, annual_income):
        if annual_income <= 600000:
            tax_per = 1
            income_after_tax = (annual_income * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 600000 and annual_income <= 800000:
            tax_per = 10
            income_after_tax = (600000 * 1) / 100 + ((annual_income - 600000) * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 800000 and annual_income <= 1100000:
            tax_per = 20
            income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((annual_income - 800000) * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 1100000 and annual_income <= 2000000:
            tax_per = 30
            income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((1100000 - 800000) * 20) / 100 + (
                        (annual_income - 1100000) * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        elif annual_income > 2000000 and annual_income <= 5000000:
            tax_per = 36
            income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((1100000 - 800000) * 20) / 100 + (
                        (2000000 - 1100000) * 1) / 100 + ((annual_income - 5000000) * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax
        else:
            tax_per = 39
            income_after_tax = (600000 * 1) / 100 + ((800000 - 600000) * 10) / 100 + ((1100000 - 800000) * 20) / 100 + (
                        (2000000 - 1100000) * 1) / 100 + ((5000000 - 2000000) * 36) / 100 + (
                                       (annual_income - 5000000) * tax_per) / 100
            annual_income_after_tax = annual_income - income_after_tax

        return annual_income, income_after_tax, annual_income_after_tax

    def tax_calculation(self, income, status):
        yearly_income = income * 12
        if status == 'U' or status == 'u':
            annual_income, income_after_tax, annual_income_after_tax = tax_Unmarried(yearly_income)
        elif status =='M' or status =='m':
            annual_income, income_after_tax, annual_income_after_tax = tax_married(yearly_income)
        return annual_income, income_after_tax, annual_income_after_tax

    def valueprint(self, name, address, married_status, annual_income, income_after_tax, annual_income_after_tax):
        display = f'''Name: {name}\t\t Address: {address}
        Married Status:{married_status}
        Total Annual Income: {annual_income}
        Tax Income:{income_after_tax}
        Income after tax: {annual_income_after_tax}'''
        return display

    def finalDisplay(self):
        num, customers_info = self.initial_display()
        with open('incomeTax_data.txt', 'w') as f:
            for i in range(num):
                annual_income, income_after_tax, annual_income_after_tax = self.tax_calculation(customers_info[i][2], customers_info[i][3])
                value = self.valueprint(customers_info[i][0], customers_info[i][1], customers_info[i][2], annual_income, income_after_tax, annual_income_after_tax)
                f.write(self.initial_display() + "\n")
                f.write(value + "\n")

def main():
    tax_calculator = TaxCalculator()
    tax_calculator.finalDisplay()

if __name__ == "__main__":
    main()