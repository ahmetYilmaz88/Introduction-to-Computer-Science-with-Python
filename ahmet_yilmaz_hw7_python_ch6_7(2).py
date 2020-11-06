## My name: Ahmet Yilmaz
##Course number and course section: IS 115 - 1001 - 1003
##Time of completion: 2 hours
##The coding is about processing data for a voting agency  

### Define election 
def election():
##    how many candidates will participate
    number_of_candidate = int(input("Enter the number of candidates: "))
    names = []
    votes = []
##    what is the last name of the candidates
    print("Enter the last name and votes for each candidate: ")
##    create a for loop to enter last names and number of votes 
    for i in range(number_of_candidate):
        print("Enter the last name of candidate ",i+1,":")
        name = input()
        vote = int(input("Enter the number of vote received: "))
        names.append(name)
        votes.append(vote)
    
    total_votes = sum(votes)
    average_votes = total_votes / len(votes)
##    output the total votes and average votes
    print("Total number of votes casted: ",total_votes)
    print("Average number of votes casted: ",average_votes)
    percentage_of_votes = []
##create another for loop to find percentage of each votes
    for i in range(len(votes)):
        temp = (votes[i]/total_votes)*100
        percentage_of_votes.append(temp)
##    create for loop and use arrays to output each name, votes and percentage    
    for i in range(len(votes)):
        print("###############################")
        print("Candidate Name: ",names[i])
        print("Number of votes received: ",votes[i])
        print("Percentage of votes received: ",percentage_of_votes[i],"%")
        print("###############################")
 
    min_vote = votes[0]
    max_vote = votes[0]
    min_vote_candidate = 0
    max_vote_candidate = 0
##    use 2 for loops and arrays to calculate the lowest and highest votes
    for i in range(len(votes)):
        if votes[i] < min_vote:
            min_vote = votes[i]
            min_vote_candidate = i
    for i in range(len(votes)):
        if votes[i] > max_vote:
            max_vote = votes[i]
            max_vote_candidate = i;
##            display the lowest and highest votes
    print("Candidate with maximum votes is: ",names[max_vote_candidate], "with",max_vote,"votes")
    print("Candidate with minimum votes is: ",names[min_vote_candidate], "with",min_vote,"votes")

    x=0
##    ask the user for a candidate name
    can_name = input("Enter any candidate's name: ")
##    display the number of candidates
    for i in range(number_of_candidate):
        if names[i]==can_name:
            print("Candidate got ",votes[i], "votes !")
            x=1
            break
##        if not in list, give an error message
    if x==0:
        print("Name of candidate is not present in voter list !")
        
election()
