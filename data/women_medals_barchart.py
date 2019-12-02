import csv
import matplotlib.pyplot as plt 
import numpy as np


women = []
sport = ['Skating', 'Skiing', 'Biathlon', 'Bobsleight', 'Luge']
Skating = []
Skiing = []
Biathlon = []
Bobsleight = []
Luge = []

categories = []



with open('data/Women - Sheet2.csv') as csvfile:
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

            
            print(line_count)
            line_count += 1


print(len(Skating), len(Skiing), len(Biathlon), len(Bobsleight), len(Luge))


quantity = [len(Skating), len(Skiing), len(Biathlon), len(Bobsleight), len(Luge)]
plot = plt.bar(sport, quantity)



for value in plot:
    height = value.get_height()
    plt.text(value.get_x() + value.get_width()/2.,
             1.002*height,'%d' % int(height), ha='center', va='bottom')

plt.bar(sport, quantity, color=['lightsalmon', 'lightseagreen', 'hotpink', 'royalblue', 'rosybrown'])








# now we are 
plt.title("Russia Woman Medal Wins")
plt.xlabel("Sport")
plt.ylabel("Medals")

plt.show()
