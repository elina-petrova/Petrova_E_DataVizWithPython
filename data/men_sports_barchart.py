import csv
import matplotlib.pyplot as plt 

sport = ['Ice Hockey', 'Skating', 'Skiing', 'Biathlon', 'Bobsleight', 'Luge']
Skating = []
Skiing = []
Biathlon = []
Bobsleight = []
Luge = []
IceHockey = []

categories = []



with open('data/rusmens - mens.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print("this iis the first. raw in the spreadsheet")
            categories.append(row)
            line_count += 1

        else:
            if row[2] == "Skating":
               
                Skating.append(row[7])
            elif row[2] == "Skiing":
            	
            	Skiing.append(row[7])
            elif row[2] == "Biathlon":
               
                Biathlon.append(row[7])
            elif row[2] == "Bobsleigh":
                
                Bobsleight.append(row[7])
            elif row[2] == "Luge":
                Luge.append(row[7])

            elif row[2] == "Ice Hockey" :
                IceHockey.append(row[7])           


            
            print(line_count)
            line_count += 1


print(len(IceHockey), len(Skating), len(Biathlon), len(Skiing), len(Bobsleight), len(Luge))

quantity = [len(IceHockey), len(Skating), len(Biathlon), len(Skiing), len(Bobsleight), len(Luge)]
plot = plt.bar(sport, quantity)

for value in plot:
    height = value.get_height()
    plt.text(value.get_x() + value.get_width()/2.,
             1.002*height,'%d' % int(height), ha='center', va='bottom')


plt.bar(sport, quantity, color=['lightsteelblue', 'plum', 'orange', 'skyblue', 'crimson'])
plt.title("Russia Men Medals Wins")
plt.xlabel('Sport')
plt.ylabel('Medals')
plt.show()