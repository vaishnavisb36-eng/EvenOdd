import sys

def even_odd(num):


    if num %2==0:
        return "Even Number"

    else:
        return "Odd Number"

    if __name__=="__main__":
     num = int(sys.argv[1])
     print(f"{num} is even_odd(num)")











import sys

def even_odd(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

if __name__ == "__main__":
    num = int(sys.argv[1])
    print(num, "is", even_odd(num))


    