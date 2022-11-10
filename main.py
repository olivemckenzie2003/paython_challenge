import os
# Module for reading CSV files
import csv

ElectionData = os.path.join("Resources", "election_data.csv")

totalNumberVotesCast = 0
listCandidateReceivedVotes = []
#Declare dictionary
md={}

percentVotesWinner = 0
winerOfElection = ""
winnerVotes=0

with open(ElectionData) as FileHandler:
    variable = csv.reader(FileHandler)

    # csv  header
    csv_header = next(variable)
   
    #loop through file "election_data.csv"
    for row in variable:

        #add up total number of votes
        totalNumberVotesCast += 1

        #Collect candidate names
        CanditNames=row[2]

        #Collecting Candidate name once and associated info
        
        if CanditNames not in listCandidateReceivedVotes:

            #Add candidate with votes name to list
            listCandidateReceivedVotes.append(CanditNames)

        #Populate Dictionary with candidate details    
            #Position in dictionary
            md[CanditNames]=0
        
        md[CanditNames]+=1      
            
    
 
# Pointer to where will create a ffile call "election_date.txt" to write to
file_to_output = os.path.join("election_data.txt")

#write to text file
with open(file_to_output, "w") as writefile:
    
    header = ( f"Election Results\n"
    f"------------------------------------\n"
    f"Total Votes: {totalNumberVotesCast}\n"
    f"------------------------------------\n")
    writefile.write(header)

    # Print the output (to terminal)

    print("\n")
    print("Election Results\n")
    print("------------------------------------\n")
    print("Total Votes:" + str(totalNumberVotesCast),"\n")
    print("------------------------------------\n")

      
    #Using candidate name as key look in dictionary for candiadte with most votes
    for x in listCandidateReceivedVotes:

        if md[x]>winnerVotes:
            winnerVotes=md[x]
            winerOfElection=x

        # Print the output (to terminal)
        print(f"{x}: Percent Votes = {round(md[x]/totalNumberVotesCast*100,3)}% ({md[x]})")
       
        #write information to file
        writefile.write(f"{x}: Percent Votes = {round(md[x]/totalNumberVotesCast*100,3)}% ({md[x]}) \n")

    footer = (    f"------------------------------------\n"
    f"Winner: {winerOfElection}\n"
    f"------------------------------------\n")
    writefile.write(footer)

    #Output to Screen
    print("------------------------------------\n")
    print("Winner:" + winerOfElection, "\n")
print("------------------------------------\n")
    
   
    
  
#file_to_output = os.path.join("budget_analysis.txt")

   

