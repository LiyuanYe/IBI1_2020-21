#R rate
#    Repeat:
#    newly infected people = R rate * already infected people
#    infected people in total = newly infected people + already infected people
n = 84  # originally infected people
r = 1.2
m = 0
for i in range (1,5):
    m = r*n # Newly infected people in this round
    n = m + n # Infected people in total after this round
print("R rate is "+ str(r) + " and the total number of individuals infected after 5 generations is " + str(n))
