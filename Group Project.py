import csv
import copy
import pickle


# Defines main function to display output


def main():
    data = fileReader()
    # displays the top profit
    # set a variable to reference findMax function, which return the record containing the max profit
    i_max = findMax(data)
    # set variables to reference the index location of profit, order i.d and index value from record with
    # max profit
    maximum = float(data[i_max][-1])
    indexMax = i_max
    order_idMax = float(data[i_max][6])
    # print order statistics
    print('ORDER STATISTICS')
    print('*********************************************************')
    print('The highest profit is: \t $ ' + '{:,.2f}'.format(maximum))
    print('The order I.D. is:\t\t ' + str(order_idMax))
    print('At index value:\t\t\t ' + str(indexMax))

    # displays the minimum profit
    # set a variable to reference findMin function, which return the record containing the minimum profit
    i_min = findMin(data)
    minimum = float(data[i_min][-1])
    indexMin = i_min
    order_idMin = float(data[i_min][6])

    print('\nThe lowest profit is: \t $ ' + '{:,.2f}'.format(minimum))
    print('The order I.D. is:\t\t ' + str(order_idMin))
    print('At index value:\t\t\t ' + str(indexMin) + '\n')

    # displays top 10 profits
    Top10Profit = find_max10(data)
    print("Top 10 Highest Total Profit Items")
    print('---------------------------------')
    print('Order ID \tDate \t       Profit\n'
          '---------\t---------\t   -------')
    for ind in Top10Profit:
        OrdIDMax = data[ind][6]
        OrdDateMax = data[ind][5]
        TopProf = data[ind][13]
        print(OrdIDMax + '\t' + OrdDateMax + '\t' + '$ ' + '{:,.2f}'.format(float(TopProf)))

    # displays minimum 10 profits
    Bottom10Profit = find_min10(data)
    print("\nTop 10 Lowest Total Profit Items")
    print('--------------------------------')
    print('Order ID \tDate \t     Profit\n'
          '---------\t---------\t-------')
    for ind in Bottom10Profit:
        OrdIDMin = data[ind][6]
        OrdDateMin = data[ind][5]
        MinProf = data[ind][13]
        print(OrdIDMin + '\t' + OrdDateMin + '\t' '$ ' + '{:,.2f}'.format(float(MinProf)))

    reader = csv.reader(open('Records.csv'))
    #  create a collection to allow for fast searching of
    #  the records by Order ID as a key and return the record if found.
    result = {}
    for row in reader:
        key = row[6]
        result[key] = row[0:]
    print("\nOrder Search Function")
    print('*********************************************************')
    # initiate sentinel
    keep_going = 'y'
    # initiate while loop to handle errors
    while keep_going == 'y':
        try:
            # prompt user for order id to locate
            # print info associated with order id
            order = result.get(input('Please input order ID ---> '))
            print("Order ID:        " + order[6])
            print("Ship Date:       " + order[7])
            print("Total Revenue:   " + '$ ' + '{:,.2f}'.format(float(order[11])))
        except:
            print('Order I.D. not found')
        # break out of the matrix
        keep_going = input('Do you have another Order I.D to check? (y/n) --->  ')

    # create a class to hold attributes
    class Record:

        def __init__(self, order_id, ship_date, total_profit):
            self.__order_id = order_id
            self.__ship_date = ship_date
            self.__total_profit = total_profit

        def get_order_id(self):
            return self.__order_id

        def get_ship_date(self):
            return self.__ship_date

        def get_total_profit(self):
            return self.__total_profit

    # create a list to hold first 100 records from the 'data' list
    first_100 = []
    i = 0
    while i < 100:
        for entry in data:
            first_100.append(entry)
            i += 1
    # serialize the first 100 entries into a .dat file
    with open('record_objects.dat', 'wb') as f:
        pickle.dump(first_100, f)
        f.close()

    # declare variables to hold info from the 10th record from first_100 records
    order = first_100[9][6]
    ship_date = first_100[9][7]
    total_profit = first_100[9][13]

    object_10 = Record(order, ship_date, total_profit)
    print("\nDeserialized Objects")
    print('***********************************')
    print('This is record #10 out of 100:')
    print('Order ID:', object_10.get_order_id())
    print('Ship Date:', object_10.get_ship_date())
    print('Total Profit:' + ' $' + '{:,.2f}'.format(float(object_10.get_total_profit())))


# Define a function to open a file and create a list to hold the txt in the file
def fileReader():
    enter_file = 'y'
    while enter_file == 'y':
        try:
            # open the file
            # file_name = input('Please enter the name of the file you wish to analyze ----> ')
            records = open(input('Enter file name: ') + '.csv', 'r')

            # Create an empty list
            data = []

            # Append rows to emtpy list data
            with records as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    data.append(row)
                del data[0]
            records.close()
            return data
        # if file not found, return appropriate errors and allow code to continue to run
        except FileNotFoundError:
            print('File not found. Please enter a valid file name.')
        except:
            print('An error occured.')




# define a function to find max profit
def findMax(data):
    # define variable to hold max value
    max = 0
    index = 0

    # Go through all records in 'data' list and find the max profit
    for i in range(0, len(data) - 1):
        if float(data[i][-1]) > max:
            max = float(data[i][-1])
            index = i
    return index


# define a function to find minimum profit
def findMin(data):
    # define variable to hold min value
    min = float(data[1][-1])
    index = 0

    # Go through all records in 'data' list and find the minimum profit
    for i in range(0, len(data) - 1):
        if float(data[i][-1]) < min:
            min = float(data[i][-1])
            index = i
    return index


# define a function to return top 10 profits to main

def find_max10(data):
    # create an empty list to hold top 10 profits
    max10 = []
    dataCopy1 = copy.deepcopy(data)
    # set an accumulator
    i = 0
    # append top 10 profits to new list
    while i < 10:
        maxIndex = findMax(dataCopy1)
        max10.append(maxIndex)
        dataCopy1[maxIndex][-1] = str(0.0)
        i += 1
    return max10


def find_min10(data):
    # create an empty list to hold bottom 10 profits
    min10 = []
    dataCopy2 = copy.deepcopy(data)
    # set an accumulator
    i = 0
    # append bottom 10 profits to new list
    while i < 10:
        minIndex = findMin(dataCopy2)
        min10.append(minIndex)
        dataCopy2[minIndex][-1] = str(1738704.0)
        i += 1
    return min10


main()


