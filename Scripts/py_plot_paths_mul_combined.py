import matplotlib.pyplot as plt
import csv

x1 = []
x2 = []
y1 = []
y2 = []


with open('avg.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(int(row[0]))
        y1.append(float(row[1]))
plt.plot(x1,y1,color='blue',label="AFL")


with open('avg.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x2.append(int(row[0]))
        y2.append(float(row[2]))
plt.plot(x2,y2,color='red',label="AFLSmart")


plt.legend(loc="lower right")
plt.xlim=(0,24)
plt.ylim=(0,100)
plt.ylabel('Total branches covered (%)', fontsize=12)
plt.xlabel('Time (hours)', fontsize=12)
plt.suptitle('State 8 (Encrypted Handshake Message(Server)) total paths discovered', fontsize=12)
plt.savefig('coverage.png')
plt.show()
