#FranklinP2
#Programmer: Anthony Franklin
#Email: afranklin18@cnm.edu
#Purpose: Provides user capability to view contact info

state =[
'Alabama',
'Alaska',
'Arizona',
'Arkansas',
'California',
'Colorado',
'Connecticut',
'Delaware',
'Florida',
'Georgia',
'Hawaii',
'Idaho',
'Illinois',
'Indiana',
'Iowa',
'Kansas',
'Kentucky',
'Louisiana',
'Maine',
'Maryland',
'Massachusetts',
'Michigan',
'Minnesota',
'Mississippi',
'Missouri',
'Montana',
'Nebraska',
'Nevada',
'New Hampshire',
'New Jersey',
'New Mexico',
'New York',
'North Carolina',
'North Dakota',
'Ohio',
'Oklahoma',
'Oregon',
'Pennsylvania',
'Rhode Island',
'South Carolina',
'South Dakota',
'Tennessee',
'Texas',
'Utah',
'Vermont',
'Virginia',
'Washington',
'West Virginia',
'Wisconsin',
'Wyoming'
]

capital =[
'Montgomery',
'Juneau',
'Phoenix',
'Little Rock',
'Sacramento',
'Denver',
'Hartford',
'Dover',
'Tallahassee',
'Atlanta',
'Honolulu',
'Boise',
'Springfield',
'Indianapolis',
'Des Moines',
'Topeka',
'Frankfort',
'Baton Rouge',
'Augusta',
'Annapolis',
'Boston',
'Lansing',
'St. Paul',
'Jackson',
'Jefferson City',
'Helena',
'Lincoln',
'Carson City',
'Concord',
'Trenton',
'Santa Fe',
'Albany',
'Raleigh',
'Bismarck',
'Columbus',
'Oklahoma City',
'Salem',
'Harrisburg',
'Providence',
'Columbia',
'Pierre',
'Nashville',
'Austin',
'Salt Lake City',
'Montpelier',
'Richmond',
'Olympia',
'Charleston',
'Madison',
'Cheyenne'
]

districts =[
'7',
'1',
'8',
'4',
'53',
'7',
'5',
'1',
'25',
'13',
'2',
'2',
'19',
'9',
'5',
'4',
'6',
'7',
'2',
'8',
'10',
'15',
'8',
'4',
'9',
'1',
'3',
'3',
'2',
'13',
'3',
'29',
'13',
'1',
'18',
'5',
'5',
'19',
'2',
'6',
'1',
'9',
'32',
'3',
'1',
'11',
'9',
'3',
'8',
'1',
]

joined =[
'22',
'49',
'48',
'25',
'31',
'38',
'5',
'1',
'27',
'4',
'50',
'43',
'21',
'19',
'29',
'34',
'15',
'18',
'23',
'7',
'6',
'26',
'32',
'20',
'24',
'41',
'37',
'36',
'9',
'3',
'47',
'11',
'12',
'39',
'17',
'46',
'33',
'2',
'13',
'8',
'40',
'16',
'28',
'45',
'14',
'10',
'42',
'35',
'30',
'44'
]

    

requested_state = input("\nPlease enter the name of any state. Please be sure to capitalize the state name! ")
index=state.index(requested_state)


print("\n\nThe capital of", requested_state,"is",capital[index])
print(requested_state,"is State #",joined[index],"to join the Union")
print(requested_state,"has",districts[index],"districts.")
print("****Thank you for allowing me to help you learn about",requested_state,"today!****")
input()
