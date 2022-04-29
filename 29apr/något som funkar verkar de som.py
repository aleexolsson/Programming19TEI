import random


# Input values to list
temps = []
for i in range(20):
    temps.append(random.randint(-50, 50))


# Calculate max, min and average temps
maxTemp = max(temps)
minTemp = min(temps)
averageTemp = sum(temps)/len(temps)


# Create dictionary
dictionary = {
    "Max Temp": maxTemp,
    "Max": maxTemp,
    "max": maxTemp,
    "Min Temp": minTemp,
    "Min": minTemp,
    "min": minTemp,
    "AvgTemp": averageTemp,
    "Average": averageTemp,
    "Avg": averageTemp,
    "avg": averageTemp,
    "average": averageTemp,
    "all values": temps,
    "all": temps
}

# Create tuple
mytuple = (dictionary, )
dictionary = mytuple[0]


# Main
while True:
    answer = (input("Write the element you with to see or exit to exit: ")).lower()

    if answer == "exit" or answer == "Exit" or answer == "EXIT":
        break

    elif answer in dictionary.keys():
        print(dictionary[answer])

    else:
        print(answer, "was not found", end="\n\n")
        print("You have to choose one of the following:")
        for key in dictionary.keys():
            print(key)
