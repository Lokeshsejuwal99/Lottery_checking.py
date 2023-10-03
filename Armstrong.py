# -------------------------------------------------------------
# check the number whether it is armstrong or not
# -------------------------------------------------------------
try:
    num = int(input('Enter a number to check armstrong number: '))

    def Armstrong(num):
        if num in range(1,10):
            return True
        sum = 0
        order = len(str(num))
        temp = num

        while(num > 0):
            digit = num % 10
            sum = sum+digit**order
            num = num // 10

        if sum == temp:
            return 'The number you have input is an armstrong number'
        else:
            return 'It is not an Armstrong number'

    display = Armstrong(num)
    print(display)
except ValueError:
    print('Please only include integer.')
