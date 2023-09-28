# _____________________________________________________________
        # Supermarket bill calculation using Class and object
# _____________________________________________________________
class SUPERMARKETBILL:
    def __init__(self):
        self.customer_info = {
            'customerName': None,
            'customerId': None,
            'address': None,
            'items': None,
            'priceList': [],
            'quantityList': [],
            'amountList': [],
            'totalAmount': 0,
            'discountPercentage': None,
            'discountedValue': None,
            'finalAmount': None
        }

    def initialDisplay(self):
        display = '''
        ******************************************************************
                            Supermarket Billing system
                              Kathmandu, Nepal
        ******************************************************************
        '''
        return display

    def userinput(self):
        self.customer_info['customerName'] = input("Enter the customer Name: ")
        self.customer_info['customerId'] = input("Enter the customer Id: ")
        self.customer_info['address'] = input("Enter the customer Address: ")
        self.customer_info['items'] = int(input('Enter the number of items: '))

        for i in range(self.customer_info['items']):
            price = int(input(f"Enter the price of {i+1} items: Rs."))
            quantity = int(input(f"Enter the quantity of {i+1}: "))
            amount = price * quantity
            self.customer_info['priceList'].append(price)
            self.customer_info['quantityList'].append(quantity)
            self.customer_info['amountList'].append(amount)
            self.customer_info['totalAmount'] += amount

    def calculateDiscount(self):
        totalAmount = self.customer_info['totalAmount']
        if totalAmount <= 500:
            discountPercentage = 1
        elif totalAmount <= 1000:
            discountPercentage = 3
        elif totalAmount <= 1500:
            discountPercentage = 5
        elif totalAmount <= 2000:
            discountPercentage = 8
        else:
            discountPercentage = 10

        discountedValue = (totalAmount * discountPercentage) / 100
        finalAmount = totalAmount - discountedValue

        self.customer_info['discountPercentage'] = discountPercentage
        self.customer_info['discountedValue'] = discountedValue
        self.customer_info['finalAmount'] = finalAmount

    def outputData(self):
        customer_info = self.customer_info
        a = ''
        for i in range(customer_info['items']):
            a += f'''
            {str(i + 1)} product = Rs.{customer_info['priceList'][i]} * {customer_info['quantityList'][i]} items
            Amount : Rs.{customer_info['amountList'][i]}
            '''

        display = f'''
        {self.initialDisplay()}
        ------------------------------------------------------------------------------------------------------------------------
        Customer Name : {customer_info['customerName']}
        Customer Id : {customer_info['customerId']}
        Customer Address : {customer_info['address']}
        Total Amount : {str(customer_info['totalAmount'])}
        {a}
        # Mr/Mrs. {customer_info['customerName']}, you have purchased {customer_info['items']} items whose total price is {customer_info['totalAmount']} and discount is Rs.{customer_info['discountedValue']} \nwith discount rate {customer_info['discountPercentage']}%. So, You have to pay Rs.{customer_info['finalAmount']}
        ------------------------------------------------------------------------------------------------------------------------
        '''
        print(display)
        return display

    def saveToFile(self, file_path):
        with open(file_path, 'a') as file:
            file.write(self.outputData())

file_path = input('Enter a path of a file: ')
number_of_users = int(input("Enter the number of users: "))

for _ in range(number_of_users):
    bill_system = SUPERMARKETBILL()
    bill_system.userinput()
    bill_system.calculateDiscount()
    bill_system.outputData()
    bill_system.saveToFile('supermarketbill.txt')

# _______________________________________________________
        # Supermarket bill calculation using Dictionary
# ________________________________________________________
import datetime

heading = '''
        Supermarket Billing system
            Maitidevi, kathmandu
'''

customer = {}

def initialdisplay(heading):
    print(heading)

def inputinformation():
    n = int(input('Enter the number of customer: '))
    customer_data = {}
    for i in range(n):
        customer_data[i] = {}
        customer_data[i]['name'] = input(f'Enter customer name: [{i+1}] = ')
        customer_data[i]['email']  = input(f'Enter customer email: [{i+1}] = ')
        customer_data[i]['phone_no']  = int(input(f"Enter the phone number of a customer: [{i+1}] ="))
        itemno = int(input("Enter the number of item customer purchased: "))
        customer_data[i]['items'] = {}
        customer_data[i]['total'] = 0

        for j in range(itemno):
            itemname = input(f'Enter the name of an item: [{j+1}] = ')
            itemprice = int(input(f'Enter the price of item: [{j+1}] = '))
            itemqty = int(input(f'Enter the quantity of an item: [{j+1}] = '))
            customer_data[i]['items'][j] = {'itemname': itemname, 'itemprice': itemprice, 'itemqty': itemqty, 'total': itemprice * itemqty}
            customer_data[i]['total'] += itemprice * itemqty
        return customer_data

def calculatebill(customer_data):
    for i in range(len(customer_data)):
        totalprice = customer_data[i]['total']

        discount = 0
        if totalprice <= 5000:
            discount = (totalprice-5000) * 0.05
        elif totalprice <= 7000:
            discount = (5000*0.05)+(totalprice-5000)*0.08
        elif totalprice <= 10000:
            discount = (5000*0.05)+(2000*0.08)+(totalprice-7000)*0.10
        else:
            discount = (5000*0.05)+(2000*0.08)+(3000*0.10)+(totalprice-10000)*0.15

        net_amount = totalprice - discount
        customer_data[i]['net_total'] = net_amount
        customer_data[i]['discount'] = discount
    return customer_data

def display_bill(customer_data):
    for i in range(len(customer_data)):
        print("Customer Name: ", customer_data[i]['name'])
        print("Customer phone_no: ", customer_data[i]['phone_no'])
        print("Customer Email: ", customer_data[i]['email'])
        print("\n")
        print("{:<20} {:>10} {:>15} {:>15}".format("Item Name", "Item Price", "Item Quantity", "Total Price"))
        for j in range(len(customer_data[i]['items'])):
            print("{:<20} {:>10} {:>15} {:>15}".format(customer_data[i]['items'][j]['itemname'],
                                                       customer_data[i]['items'][j]['itemprice'],
                                                       customer_data[i]['items'][j]['itemqty'],
                                                       customer_data[i]['items'][j]['total']))
        print("\nDiscount: ", customer_data[i]['discount'])
        print("Net Total: ", customer_data[i]['net_total'])
        print("\n")
#
def main():
    initialdisplay(heading)
    customer_data = inputinformation()
    customer_data = calculatebill(customer_data)
    initialdisplay(heading)
    display_bill(customer_data)


if __name__ == "__main__":
    main()
