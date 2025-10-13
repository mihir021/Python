#  Write a program to take 10 values from keyboard using loop and print their average on the screen

n = 10
sum_numbers = 0
while n > 0:
    sum_numbers += int(input("Enter Number :"))
    n -= 1
print("Avg is : ",(sum_numbers/10))