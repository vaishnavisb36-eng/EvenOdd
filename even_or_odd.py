import sys

def even_odd(num):


    if num %2==0:
        return "Even Number"

    else:
        return "Odd Number"

    if __name__=="__main__":
    

     num = int(sys.argv[1])
    print(even_odd(num))












    import sys


def even_and_odd(number):
    if number % 2 == 0:
        return "Even number"
    return "Odd number"


if __name__ == "__main__":
    number = int(sys.argv[1])
    print(even_and_odd(number))
