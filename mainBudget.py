import os
# Module for reading CSV files
import csv

BudgetData= os.path.join("Resources","budget_data.csv")

total_months = 0
net_list = []
list = []
total_net=0

net_change_list=[]
net_change=0
month_of_change =[]
monthName=[]
month=""
month2=""


with open(BudgetData) as FileHandler:
    variable = csv.reader(FileHandler,delimiter=",")
    
    #csv  header
    csv_header=next(variable)
    FirstRow=next(variable)
    
    print(csv_header)
    print(FirstRow)

    total_months += 1
    total_net += int(FirstRow[1])
    
    prev_net = int(FirstRow[1])
    for row in variable:
        # Track the total
        total_months += 1
        total_net += int(row[1])
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change += [row[0]]
        monthName=month_of_change

   
    #Find maximum value in net_change_list
    GreatestIncrease=max(net_change_list)
    #print(GreatestIncrease)
    # Find minimum value in  net_change_list
    GreatestDecrease=min(net_change_list)
    #print(GreatestDecrease)

    index = net_change_list.index(GreatestIncrease)
    index2 = net_change_list.index(GreatestDecrease)

    #print(index)
    #print(monthName[index])
    month=monthName[index]

    #print(index2)
    #print(monthName[index2])
    month2=monthName[index2]

    net_monthly_avg = round(sum(net_change_list) / len(net_change_list), 2)
    
    print(net_monthly_avg)
    #print(f"Average Change: ${net_monthly_avg:.2f}\n")

       
    print("\n \n")

    print("Financial Analysis\n")
   
    print("---------------------------\n")
    
    print("Total Months:  " + str(total_months), "\n")
    
    print("Total: $" + str(total_net) ,"\n")
   
    print("Average Change:   $" + str(net_monthly_avg)+ "\n")
   
    print("Greatest Increase in Profits:" + month  + "($" + str(GreatestIncrease),")" "\n" )
    print("Greatest Increase in Profits:" + month2 + "($" +  str(GreatestDecrease),")" "\n" )
    print("\n")

    output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {month}  (${GreatestIncrease})\n"
    f"Greatest Decrease in Profits: {month2}  (${GreatestDecrease})\n")

# Print the output (to terminal)
print(output)

file_to_output = os.path.join("budget_analysis.txt")
# Print the output (to terminal)
print(output)
# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    


 




        

 
