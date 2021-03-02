
def collatz(starting_value):
    temp = starting_value
    counter = 0
    while temp != 1:
        if temp%2 == 0:
            temp = temp/2
        else:
            temp = 3*temp + 1
        counter += 1
    
    return counter

if __name__ == "__main__":
    max = 0
    for i in range(1, 10000):
        series = collatz(i)
        if series > max:
            max = series
            print(i)
