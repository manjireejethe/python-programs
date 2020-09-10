num=int(input('Enter a number:'))

def fun():
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                print(num,"is not a prime number")
                return

        print(num,"is a prime number")
        return
