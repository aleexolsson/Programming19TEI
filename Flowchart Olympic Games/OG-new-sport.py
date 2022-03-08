import nola

sports = ["Soccer", "Handball", "Skiing", "Swimming", "Pole Vault", "Biathlon"]


basic_questions = ["Do the Olympic Games need more sports?", "Is it a sport?", "Is the sport legal?", "Is the sport doable?", "Is there a big fan base around the sport?", "Is there enough people that do this sport?", "Does the Olympic Games have to many sports now?" ]
questioning = True
i = 0

new_sport = input("Which sport do you think should be added to the Olympic Games?")


while questioning and i != 6:
    answer = nola.s(input(basic_questions[i]))

    if answer == "yes":
        i += 1

    elif answer == "no":
        print("Alright let's not add a now sport now.")
        questioning = False


while questioning:
    sports.append(new_sport)

    print("\nSports in the Olympic Games now are:")
    for i in range(len(sports)):
        print(sports[i])

    answer = nola.s(input("Does the Olympic Games have to many sports now?"))
    if answer == "yes":
        break
    elif answer == "no":
        questioning = False
        break


while questioning:
    remove = input("Which sport should be removed?")
    if remove in sports:
        sports.remove(remove)
        break



print("\nSports in the Olympic Games now are:")
for i in range(len(sports)):
    print(sports[i])