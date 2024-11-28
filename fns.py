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

def addExpense():
    while True:
        print("Please select an expense category:")
        for (i, item) in enumerate(expenseCats, start=1):
            print(f"{i}. {item}")
        selectedCategory=int(input("\n"))
        # checking if selected category lies between 1 to 8
        # i.e, the number of categories
        if selectedCategory<=i and selectedCategory>0:
            spentAmt=float(input("Enter the amount spent: "))
            # converting all keys from dict `expenseCats` to a list
            # then accessing category via index number
            list(expenseCats.values())[selectedCategory-1].append(spentAmt)
            print(list(expenseCats.values())[selectedCategory-1])
            print(f"{expenseCats}\n")
        else:
            print("Invalid Input. Exiting program")
            break