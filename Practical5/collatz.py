# Fibonacci:
#       Repeat:
#           Cn = C(n-1) + C（n-2)
a = 0
b = 0    # Set "b" as C(n-1)
c = 1    # Set "c" as Cn

for i in range(1,13):
    print(c)  # Print Cn
    a = c     # use "a" as a "reservoir" to transfer the number from "c" to "b"
    c = c + b # Generate C(n+1) for the next print
    b = a
    i = i + 1
