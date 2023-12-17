import matplotlib.pyplot as plt

# Pie chart
labels = ['Wins', 'Losses', 'Draws']
sizes = [30, 3, 5]
# only "explode" the 1st slice (i.e. 'Wins')
explode = (0.1, 0, 0)  
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.show()