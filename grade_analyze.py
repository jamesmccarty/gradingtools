#!/usr/bin/env python

import xlrd
import matplotlib.pyplot as plt
import numpy as np

print "Grade Analyzer\n"
print "Written by J. McCarty\n"

loc = ("/Users/jmccarty/Downloads/Fall_2020_Midterm1grades.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

scores = []
#print(sheet.cell_value(0,0))
print "number of entries in column: ", sheet.nrows

for i in range(sheet.nrows):
    scores.append(sheet.cell_value(i,1))

scores.pop(0)
scores = np.array(scores)

print "Class average: ", np.mean(scores)
print "Standard Deviation: ", np.std(scores)


# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(scores, bins=30, color='#0504aa',
                            alpha=0.5, rwidth=0.85)
plt.grid(axis='y', alpha=0.5)
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Grade Distribution')
#plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
#plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()
