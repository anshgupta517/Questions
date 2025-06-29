# Problem 1
# Consider an algorithm that takes as input a positive integer n. 
# If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. 


def collatz_sequence(n: int):

    print(n, end=" ")

    if n == 1:
        return
    elif n % 2 == 0:
        collatz_sequence(n//2)
    else:
        collatz_sequence((n*3)+1)
    
    
def main():
    try:    
        n = int(input("Enter a number: "))

        if n > 0 :
            collatz_sequence(n)
        else:
            print("Enter a valid positive integer")
    except ValueError:
        print("Enter a valid positive integer")

if __name__ == "__main__":
    main()