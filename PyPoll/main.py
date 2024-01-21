#Pull in data from election_data.csv
import os
import csv

#Importing .csv file from local repo and outline of file path
script_dir = os.path.dirname(os.path.abspath('election_data.csv'))

data_folder = os.path.join(script_dir, 'PyPoll', 'Resources')

file_path = os.path.join(data_folder, 'election_data.csv')

#Initialize variables & create the lists to store the data
count = 0
candidate_list = []
vote_count = {}
vote_percent = []

#Open the CSV file using the set path PyPollcsv
with open (file_path, newline="") as csvfile:
    #Create a CSV reader with dictionaries
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row first
    csv_header = next(csvreader)

    #Iterate through the rows in the CSV files
    for row in csvreader:
        #Count total number of votes
        count = count + 1 
        #Set candidate names to candidate_list 
        candidate_list.append(row[2])
        #Create a set from candidate_list to get candidate_unique names
    candidate_unique = set(candidate_list)

    #calculate volte count and percentage for each candidate
    for candidate in candidate_unique:   
        # y is the total votes number per candidate
        y = candidate_list.count(candidate)
        vote_count[candidate] = y
        # z is the total votes percent per candidate
        z = (y/count)*100
        vote_percent.append(z)
    
    winning_vote_count = max(vote_count.values())
    winner = [candidate for candidate, votes in vote_count.items() if votes == winning_vote_count][0]

    print("----------------------------------------------------------")
    print("Election Results")
    print("----------------------------------------------------------")
    print("Total Votes: " + str(count))
    print("----------------------------------------------------------")
    for candidate in candidate_unique:
        index = list(candidate_unique).index(candidate)
        print(f"{candidate}: {vote_percent[index]}% ({vote_count[candidate]})")
    print("----------------------------------------------------------")
    print(f"Winner: {winner}")
    print("----------------------------------------------------------")

with open('election_results.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("Election Results"+ "\n")
    text.write("----------------------------------------------------------\n")
    text.write("Total Votes: " + str(count) + "\n")
    text.write("----------------------------------------------------------\n")
    for candidate in candidate_unique:
        index = list(candidate_unique).index(candidate)
        text.write(f"{candidate}: {vote_percent[index]}% ({vote_count[candidate]})\n")
    text.write("----------------------------------------------------------\n")
    text.write("Winner: " + winner + "\n")
    text.write("----------------------------------------------------------\n")