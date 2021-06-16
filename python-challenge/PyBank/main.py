import csv
import os

write_txt = os.path.join("analysis","results.txt")
read_csv = os.path.join("Resources","budget_data.csv")

lineCounter = 0
totalAmount = 0
oldAmount = 0
newAmount = 0
monthlyChange = 0
averageChange = 0

# Dictionaries to keep records of max and min
greatestIncrease = {
    "date": "",
    "amount": 0
}
greatestDecrease = {
    "date": "",
    "amount": 0
}
# List to keep monthly changes
aChange = []

def findAverage(l):
    return (sum(l)/len(l))

# Displat results to console
def printResults():
    print(f'Financial Analysis')
    print(f'------------------')
    print(f'Total Months: {lineCounter}')
    print(f'Total:\t ${totalAmount}')
    print(f'Average Change: ${round(findAverage(aChange),2)}')
    print(
        f'Greatest Increase in Profits: ${greatestIncrease["date"]} (${greatestIncrease["amount"]})')
    print(
        f'Greatest Decrease in Profits: ${greatestDecrease["date"]} (${greatestDecrease["amount"]})')
    print(f'Processed {lineCounter} rows.')

# Export to txt file
def exportReport():
    with open(write_txt,"w") as fileX:
        fileX.write(f'Financial Analysis\n')
        fileX.write(f'------------------\n')
        fileX.write(f'Total Months: {lineCounter}\n')
        fileX.write(f'Total:\t ${totalAmount}\n')
        fileX.write(f'Average Change: ${round(findAverage(aChange),2)}\n')
        fileX.write(
        f'Greatest Increase in Profits: ${greatestIncrease["date"]} (${greatestIncrease["amount"]})\n')
        fileX.write(
        f'Greatest Decrease in Profits: ${greatestDecrease["date"]} (${greatestDecrease["amount"]})\n')
        
# def main():
with open(read_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Skip the first row
    header = next(csv_reader)

    # Process the first record to assign relevant variables for Change calculation
    remover = next(csv_reader)
    oldAmount=int(remover[1])
    totalAmount = int(remover[1])
    lineCounter = 1

    for row in csv_reader:

        # Month (Record) Counter
        lineCounter += 1

        # TotalAmount
        totalAmount += int(row[1])
        
        # Calculate Average change
        newAmount = int(row[1])
        monthlyChange = newAmount-oldAmount
        oldAmount = int(row[1])
        # Add new value to the list
        aChange.append(monthlyChange)
        
        # Find Greatest Increase
        if monthlyChange > greatestIncrease.get("amount"):
            greatestIncrease["date"] = row[0]
            greatestIncrease["amount"] = monthlyChange

        # Find Greatest Decrease
        if monthlyChange < greatestDecrease.get("amount"):
            greatestDecrease["date"] = row[0]
            greatestDecrease["amount"] = monthlyChange

    #Print and Export the results       
    printResults()
    exportReport()