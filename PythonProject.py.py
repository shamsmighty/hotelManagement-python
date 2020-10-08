import csv
import sys
filename = "hotels.csv"


def hotelsearchWithCost(state, operation):
    answer = [[0]]
    cost = 0
    maxCost = sys.maxsize
    #reading the csv file
    with open(filename, 'r') as csvfile:

        datalength = 0
        costly = 0
        x = 0
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            #logic to ignor 1st row in csv file
            if (x == 0):
                x += 1
                continue

            if (row[2] == state):
                #Calculating the total sum of cost in csv file of given state
                cost += int(row[3])
                #total length of rows in the state as per user input
                datalength = datalength + 1
                if (operation == "Highest" and int(row[3]) >= costly):
                    #calculating the row with highest cost
                    costly = int(row[3])
                    #accessing the particular row with highest cost
                    answer[0] = row

                if (operation == "Cheapest" and int(row[3]) < maxCost):
                    #calculating the row with lowest cost
                    maxCost = int(row[3])
                    #accessing the particular row with cheapest cost
                    answer[0] = row
            if (state == "India"):
                #Calculating the total sum of cost in csv file based on state
                cost += int(row[3])
                #total length of rows in the state as per user input
                datalength = datalength + 1
                if (operation == "Highest" and int(row[3]) >= costly):
                    #calculating the row with highest cost
                    costly = int(row[3])
                    #accessing the particular row with highest cost
                    answer[0] = row

                if (operation == "Cheapest" and int(row[3]) < maxCost):
                    #calculating the row with lowest cost
                    maxCost = int(row[3])
                    #accessing the particular row with cheapest cost
                    answer[0] = row

        if (operation == "Average"):
            #calculating the average of the particular state(As per user input)
            answer[0] = [float(cost) / float(datalength)]

        return answer


def hotelsearchWithRatings(state, operation):

    answer = [[0]]
    cost = 0
    maxRating = sys.maxsize

    with open(filename, 'r') as csvfile:
        datalength = 0
        costly = 0
        x = 0
        #reading the csv file
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            #logic to ignor 1st row in csv file
            if (x == 0):
                x += 1
                continue

            if (row[2] == state):
                #Calculating the total sum of ratings in csv file of given state
                cost += float(row[4])
                #total length row
                datalength = datalength + 1
                if (operation == "Highest" and float(row[4]) >= costly):
                    #calculating the row with highest rating and storing in costly
                    costly = float(row[4])
                    #accessing the row particular with highest rating
                    answer[0] = row

                if (operation == "Cheapest" and float(row[4]) < maxRating):
                    #calculating the row with cheapest rating and storing in maxRating
                    maxRating = float(row[4])
                    #accessing the particular row with cheapest rating
                    answer[0] = row

            if (state == "India"):
                #Calculating the total sum of ratings in csv file of given state
                cost += float(row[4])
                #total length row
                datalength = datalength + 1
                if (operation == "Highest" and float(row[4]) >= costly):
                    #calculating the row with highest rating and storing in costly
                    costly = float(row[4])
                    #accessing the particular row with highest rating
                    answer[0] = row

                if (operation == "Cheapest" and float(row[4]) < maxRating):
                    #calculating the row with cheapest rating and storing in maxRating
                    maxRating = float(row[4])
                    #accessing the particular row with cheapest rating
                    answer[0] = row

        if (operation == "Average"):
            #calculating the average of the particular state(As per user input) 
            answer[0] = [float(cost) / float(datalength)]

        return answer
print("Please go through readme file for detailes.");
print("Please Choose anyone among 'Karnataka, Maharashtra, TamilNadu or even India' ");
state = input("What is the state: ").capitalize()
print("Please select anyone among 'Cost or Ratings'  ");
criteria = input("Choose Cost or Ratings: ").capitalize()
print("Choose anyone operation among '(Highest/Cheapest/Average)' ");
operation = input("Type of Operation(Highest/Cheapest/Average): ").capitalize()

if (criteria == "Cost"):
    output = hotelsearchWithCost(state, operation)
    #print(output)
    if (output[0][0] == 0 or len(output[0]) == 0):
        print("No data found for given inputs")
    elif (operation == "Average"):
        print(" Average cost of hotel in " + state + " is " +
              str(round(output[0][0], 2)))
    else:
        if (state == 'India'):
            print("Hotel with " + operation + " price in " + output[0][2] +
                  " is " + output[0][1] + " with price " + output[0][3])
        else:
            print("Hotel with " + operation + " price in " + state + " is " +
                  output[0][1] + " with price " + output[0][3])

elif (criteria == "Ratings"):

    output = hotelsearchWithRatings(state, operation)
    #print(output)
    if (output[0][0] == 0 or len(output[0]) == 0):
        print("No data found for given inputs")
    elif (operation == "Average"):
        print("Average Rating of hotel in " + state + " is " +
              str(round(output[0][0], 2)))
    else:
        if (state == 'India'):
            print("Hotel with " + operation + " rating in " + output[0][2] +
                  " is " + output[0][1] + " with rating is " + output[0][4])
        else:
            print("Hotel with " + operation + " rating in " + state + " is " +
                  output[0][1] + " with rating is " + output[0][4])

else:
    print("Invalid inputs please try again with valid inputs!!")
