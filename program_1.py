#programmer = Caiden
#date = 10.18.24

# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, # and the months with the highest and lowest amounts.
list = []
month = 0
totalRain =0
for x in range(12):
    month += 1
    rain = int(input('How much rain during month? '))
    list.append(rain)
    totalRain += rain
averageRain = totalRain/12
print(list)
print('there was a total of',totalRain,'inches of rain during the year')
print('There was an average rainfall of',averageRain,'inches per month')
print(max(list))
print(min(list))
