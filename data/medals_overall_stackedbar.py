import numpy as np 
import csv
import matplotlib.pyplot as plt 
from matplotlib import rc
import pandas as pd

rc('font', weight='bold')


golds_one = []
silver_one = []
bronzes_one = []

golds_two = []
silver_two = []
bronzes_two = [] 

golds_three = []
silver_three = []
bronzes_three = []

golds_four = []
silver_four = []
bronzes_four = []

golds_five = []
silver_five = []
bronzes_five = []

golds_six = []
silver_six = []
bronzes_six = []

categories =[]

with open ('data/Russia - Sheet1.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this iis the first. raw in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[0] == "1994":
				if row[7] == "Gold":
					golds_one.append(row[7])
				elif row[7] == "Silver":
					silver_one.append(row[7])
				elif row[7] == "Bronze":
					bronzes_one.append(row[7])

			elif row[0] == "1998" :
				if row[7] == "Gold":
					golds_two.append(row[7])
				elif row[7] == "Silver":
					silver_two.append(row[7])
				elif row[7] == "Bronze":
					bronzes_two.append(row[7])

			elif row[0] == "2002" :
				if row[7] == "Gold":
					golds_three.append(row[7])
				elif row[7] == "Silver":
					silver_three.append(row[7])
				elif row[7] == "Bronze":
					bronzes_three.append(row[7])

			elif row[0] == "2006" :
				if row[7] == "Gold":
					golds_four.append(row[7])
				elif row[7] == "Silver":
					silver_four.append(row[7])
				elif row[7] == "Bronze":
					bronzes_four.append(row[7])

			elif row[0] == "2010":
				if row[7] == "Gold":
					golds_five.append(row[7])
				elif row[7] == "Silver":
					silver_five.append(row[7])
				elif row[7] == "Bronze":
					bronzes_five.append(row[7])

			elif row[0] == "2014":
				if row[7] == "Gold":
					golds_six.append(row[7])
				elif row[7] == "Silver":
					silver_six.append(row[7])
				elif row[7] == "Bronze":
					bronzes_six.append(row[7])



			print(line_count)
			line_count += 1

bar1 = [len(bronzes_one), len(bronzes_two), len(bronzes_three), len(bronzes_four), len(bronzes_five), len(bronzes_six)]
bar2 = [len(silver_one), len(silver_two), len(silver_three), len(silver_four), len(silver_five), len(silver_six)]
bar3 = [len(golds_one), len(golds_two), len(golds_three), len(golds_four), len(golds_five), len(golds_six)]

bars = np.add(bar1, bar2).tolist()
r = [1,2,3,4,5,6]

names = ['1994','1998','2002','2006','2010', '2014']
barWidth = 1

# Create brown bars
plt.bar(r, bar1, color='peru', edgecolor='white', width=barWidth)
# Create green bars (middle), on top of the firs ones
plt.bar(r, bar2, bottom=bar1, color='silver', edgecolor='white', width=barWidth)
# Create green bars (top)
plt.bar(r, bar3, bottom=bars, color='gold', edgecolor='white', width=barWidth)
 
# Custom X axis
plt.xticks(r, names, fontweight='bold')
plt.title("Russia Medal Statistic 1994 - 2014")
 
# Show graphic
plt.show()



