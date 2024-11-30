from fns import *

print("Press Ctrl+c to exit program. No other way to exit :)\n")

## Add expense to dict
# addExpense()

## Sum of all expenses
finalSum_countElements=totalExpense()
print("\nTotal expense across categories is: %.2f\n" %finalSum_countElements[0])


## Average
finalAvg=avgExpense()
print("\nAverage expense across categories is: %.2f\n" %finalAvg)

## Display expense
displayExpense()