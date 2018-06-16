import os
import csv

# Read csv files
fileA = os.path.join('Resources', 'election_data_1.csv')
fileB = os.path.join('Resources', 'election_data_2.csv')
 
# Open and read CSV
with open(fileA, 'r', newline='') as csvfile:
    csvdoc = csv.reader(csvfile, delimiter=',')
    next(csvdoc)

    # Set Variables
    votestotal = 0
    candidates = []
    votes_count = []
    
    # for loops
    for row in csvdoc:
        votestotal=votestotal + 1
        if row[2] in candidates:
            vote = candidates.index(row[2])
            votes_count[vote]+=1
        else:
            candidates.append(str(row[2]))
            votes_count.append(1)
    
    # Print results
    print("Election Results")
    print("-"*20)
    print("Total Votes: "+str(votestotal))
    print("-"*20)
    for x in range(0, len(candidates)):
        print(candidates[x]+": "+str(round((100*votes_count[x]/votestotal),2))+"% "+str(votes_count[x]))
    print("-"*20)
    winner = votes_count.index(max(votes_count))
    print("The winner is: "+candidates[winner])
    print("-"*20)
    
    # Create new text file
output1 = os.path.join('output', 'results1.txt')
with open(output1, "w") as text_file:
    text_file.writelines('Election Results\n')
    text_file.writelines('-------------------------\n') 
    text_file.writelines('Total Votes ' +  str(votestotal) + '\n')
    text_file.writelines('-------------------------\n') 
    for x in range(0, len(candidates)):
        text_file.writelines([candidates[x] + ': '+ str(round((100*votes_count[x]/votestotal),2)) + '% ' + str(votes_count[x]) + '\n'])
    text_file.writelines('-------------------------\n') 
    text_file.writelines('The winner is: ' + str(candidates[winner]))