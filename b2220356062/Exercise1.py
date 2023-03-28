n = int(input("Please enter number N:"))

odd = sum(i for i in range(n+1) if (i % 2 != 0))
even = (sum(i for i in range(n+1) if (i % 2 == 0))) / (n/2)
print("Sum of odds:", odd)
print("Average of evens:", even)
