print("Hello World")

###Data Type###

#INT
type(3)
type (2019)

ballots= 1,341
ballots
type(ballots)
#To type integers greater than 999 we dont use the coma.

#FLOAT
type(73.81)

#STRINGS
type ("Hello World") 
type ("")

#BOOLEAN
type(True)

#VARIABLES

num_candidates = 3
winning_percentage= 73.81
candidate= "Diane"
won_election= True

###Calculations###
(5+2)*3
(8//5)-3
8+(22*(2-4))
16-3/(2+7)-1
3**(3%5)

5+(9*3/2-4)
5+(9*3/(2-4))

###List###
counties=["Arapahoe","Denver","Jefferson"]
counties

#positions
counties[0]
counties[1]
counties[2]
counties[-1]

#length of the list
len(counties)

counties[0:2]
counties[0:1]
counties[1:]

#to add an item to a list 
counties.append("El Paso")
counties

#to add 'El Paso' at index 2
counties.insert(2,"El Paso")
counties

#to remove the extra 'El Paso"
#we can use pop()to eliminate an item, counties.pop(3)
counties.remove("El Paso")
counties

counties.pop(3)

#Change Jefferson for 'El Paso'
counties[2]="El Paso"
counties

counties.insert(2,"El Paso")
counties.remove("El Paso")
counties.remove("Arapahoe")
counties.append("Arapahoe")
counties

###Tuples###
counties_tuple=("Arapahoe","Denver","Jefferson")
len(counties_tuple)

counties_tuple[1]
counties_tuple[0:2]

###Dictionaries###
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict

counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
counties_dict

len(counties_dict)

#return all the values of the dictionary
counties_dict.items()
dict_items([('Arapahoe',422829),('Denver',463353),('Jefferson',432438)])

counties_dict.keys()
dict_keys(['Arapahoe','Denver','Jefferson'])

counties_dict.values()
dict_values([422829,463353,432438])

#to get a specific value
counties_dict.get("Denver")
counties_dict['Arapahoe']

voting_data=[]
voting_data.append({"country":"Arapahoe", "registered_voters":422829})
voting_data.append({"country":"Denver", "registered_voters":463353})
voting_data.append({"country":"Jefferson", "registered_voters":432438})

voting_data

voting_data.append({"country":"El Paso", "registered_voters":471149})
voting_data

voting_data.remove("Arapahoe")

###Decision Statement###

#How many votes did you get?
my_votes=int(input("How many votes did you get in the election?"))
#Total votes in the election
total_votes=int(input("What is the total votes in the election?"))
#Calculate the percentage of votes you received.
percentage_votes=(my_votes/total_votes)*100
print("I recieved" + str(percentage_votes)+" % of total votes.")

########

counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver':
    print(counties[1])
 
#if counties[3] != 'Jefferson':
#    print(counties[2])

#Membership Operators 3.2.9
counties=["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print ("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
    
#Logical Operators
if "Arapahoe" and "Denver" in counties:
    print ("Arapahoe and Denver are in the list of counties.")
else:
    print("Arapahoe or Denver is not in the list of counties.")
    
if "Arapahoe" or "El Paso" in counties:
    print ("Arapahoe or El Paso is in the list of counties.")
else:
    print ("Arapahoe and El Paso are not int he list of counties.")
    
###Repetition Statements###3.2.10
 
#While
count =7
while count <1:
    print("Hello World")
    
#Iterate Through Lists and Tuples
for county in counties:
    print (county)

numbers=[0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print (num)
    
for i in range(len(counties)):
    print(counties[i])

#Tuples
counties_tuple=("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

#Dictionaries
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)
#####
for county in counties_dict.dict():
    print(counties_dict[county])

for county in counties_dict.dict():
    print(counties_dict.get[county])
#####
    
for county, voters in counties_dict.items():
    print(county,voters)

for county_dict in voting_data:
    print(county_dict)

#Retrieve voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])


###Printng Formats###

#Using f

#How many votes did you get?
my_votes=int(input("How many votes did you get in the election?"))
#Total votes in the election
total_votes=int(input("What is the total votes in the election?"))
#Calculate the percentage of votes you received.
percentage_votes=(my_votes/total_votes)*100
print("I recieved" + str(percentage_votes)+" % of total votes.")


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#f style
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multiline F-Strings

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#Format Floating-Point Decimals




