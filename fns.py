# dict containing category names as keys and a list of expenses as values
expenseCats = {
    "Apparel" : [],
    "Entertainment" : [],
    "Food" : [],
    "Medical" : [],
    "Rent" : [],
    "Travel" : [],
    "Utilities" : [],
    "Misc" : []
}

# demoDict = {
#     "One" : [99,23],
#     "Two" : [],
#     "Three" : [123.456],
#     "Four" : [500,420,88.96],
#     "Five" : [778]
# }

def addExpense():
    while True:
        print("\nPlease select an expense category:")
        for (i, item) in enumerate(expenseCats, start=1):
            print(f"{i}. {item}")
        # if try block doesn't have any errors, it will proceed to else block
        # checking if selected category lies between 1 to 8
        # i.e, the number of categories
        try:
            selectedCategory=int(input("\n"))
            if selectedCategory<=i and selectedCategory>0:
                pass
            else:
                raise Exception()
        # if keyboard interruption is detected, exit program
        except KeyboardInterrupt:
            break
        # on any error except keyboard interruption, this except block will run
        # in practice this will just warn the user for valid input and continue program
        except:
            print(f"\nWARNING: Expense category needs to be within 1 and {i}")
        else:
            # Taking spent amount input as float
            # if spent amount is -ve, raise an exception
            # else continue to the else block since try has no errors
            # i.e, add expense to the respective category
            try:
                spentAmt=float(input("Enter the amount spent: "))
                if spentAmt>0:
                    pass
                else:
                    raise Exception()
            except:
                print(f"\nWARNING: Expense needs to be a positive float value")
            else:
                # converting all keys from dict `expenseCats` to a list
                # then accessing category via index number
                list(expenseCats.values())[selectedCategory-1].append(spentAmt)

def avgExpense():
    finalSum_countElements=totalExpense()
    avgAll=finalSum_countElements[0]/finalSum_countElements[1]
    return avgAll

def totalExpense():
    allExpenses=list(expenseCats.values())[:]
    sumAll=0
    totalElements=0
    for i in range(len(allExpenses)):
        for j in range(len(allExpenses[i])):
            totalElements+=1
            sumAll=sumAll+allExpenses[i][j]
    return [sumAll, totalElements]

def displayExpense():
    print("\nExpenses per category are:")
    for key, value in expenseCats.items():
        print("{}: {}".format(key, value))
