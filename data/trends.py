import matplotlib.pyplot as plt
import csv
import numpy as np 

years = [1994,1998,2002,2006,2010,2014]
medals_one = []
medals_two = []
medals_three = []
medals_four = []
medals_five = []
medals_six = []
i = 0



categories = [] # first row -> nt data

with open('data/Russia - Sheet1.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print("this iis the first. raw in the spreadsheet")
            categories.append(row)
            line_count += 1

        else:
            if row[0] == "1994":
                medals_one.append(row[0])
            elif row[0] == "1998":
                
                medals_two.append(row[0])
            elif row[0] == "2002":
                
                medals_three.append(row[0])
            elif row[0] == "2006":
                
                medals_four.append(row[0])
            elif row[0] == "2010":

                medals_five.append(row[0])
                
            elif row[0] == "2014":
                
                medals_six.append(row[0])
            
    
            
            print(line_count)
            line_count += 1

medals = [len(medals_one),len(medals_two),len(medals_three),len(medals_four),len(medals_five),len(medals_six)]


plt.plot(years, medals, color='blue', linewidth=6.0)

plt.xticks(np.arange(1990, 2018, 4)) 

plt.ylabel("Medal Quantity")
plt.xlabel("Olimpic Years")
plt.title("Russia Medal Wins 1994 - 2014", pad=20)
plt.xlim(1990, 2018)
plt.ylim(0, 100)

#show the chart
plt.show()