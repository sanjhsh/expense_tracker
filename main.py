from fns import *

print("Press Ctrl+c to exit program. No other way to exit :)\n")

availableFns=["Add an Expense", "Sum of all Expenses", "Average of Expenses", "Display all Expenses"]
while True:
    print("\nSelect an option: \n")
    for (i, item) in enumerate(availableFns, start=1):
            print(f"{i}. {item}")
    try:
        selectedFn=int(input("\n"))
        if selectedFn<=i and selectedFn>0:
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
        if selectedFn==1:
            addExpense()
        elif selectedFn==2:
            finalSum_countElements=totalExpense()
            print("\nTotal expense across categories is: %.2f\n" %finalSum_countElements[0])
        elif selectedFn==3:
            finalAvg=avgExpense()
            print("\nAverage expense across categories is: %.2f\n" %finalAvg)
        elif selectedFn==4:
            displayExpense()
        else:
            print("Something went wrong. Exiting program")
            break
