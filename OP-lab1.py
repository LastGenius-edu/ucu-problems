# the ugliest one of them all
import random

def main():
    # nmber of situations with a shared birthday
    shared = 0

    #acquiring input from user to determine how many people are in a group
    x = int(input("Type in the number of people to check: "))

    times = 10000

    # repeat the whole process of randomizing and checking 10000 times to minimize odd situations
    for i in range (times):
        # declaring the list with all the birthdays of a group
        bd = []

        # boolean expression which shows if there has been at least one shared birthday
        same = False

        for i in range (x):
            # randomly generate a birthday, append it to the list
            bd.append(random.randint(1, 365))
            for j in range (0, i):
                if (bd[i] == bd[j]):
                    # we've found a shared birthday, so let's remember it and stop looking for shared ones 
                    same = True
                    break
            if same:
                # if we have found a shared birthday, add 1 to a number of "shared birthday" situations
                # and start generating birthdays all over again
                shared += 1
                break

    # figure out the overall probability of shared birthdays by seeing what share of total situations they have accounted for
    prob = (shared / times) * 100

    print(prob, "%")


main()
