import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([3,9,2,5,7])

# plt.plot(y, marker='X')
#shor notation for marker line color
# plt.title('Line Plot',c='blue',loc='center',fontdict={'fontname':'Comic Sans MS','fontsize':20,'fontweight':'bold'})
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.plot(x,y,'X-r') #X is marker,- is line type and r is line color
# # plt.grid()
# plt.grid(axis='y',color='green', linestyle='--', linewidth=0.5) #customize grid
# plt.show()

x1=np.array([1,2,3,4,5])
y1=np.array([3,9,2,5,7])
x2=np.array([1,2,3,4,5])
y2=np.array([5,7,8,9,10])

# plt.plot(x1,y1,x2,y2)
# plt.show()


#subplots, with subplots we can create multiple plots in a single figure

# plt.subplot(1,2,1) #1 row, 2 columns, 1st plot
# plt.subplot(2,1,1) #2 rows, 1 column, 1st plot
# plt.plot(x1,y1,'X-r')
# plt.title('Line Plot 1',c='blue',loc='center',fontdict={'fontname':'Comic Sans MS','fontsize':20,'fontweight':'bold'})
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# # plt.subplot(1,2,2) #1 row, 2 columns, 2nd plot
# plt.subplot(2,1,2) #2 rows, 1 column, 2nd plot
# plt.plot(x2,y2,'X-g')
# plt.title('Line Plot 2',c='green',loc='center',fontdict={'fontname':'Comic Sans MS','fontsize':20,'fontweight':'bold'})
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# plt.tight_layout() #tight_layout is used to adjust the spacing between the subplots, it automatically adjusts the spacing to prevent overlap between the subplots
# plt.suptitle("subplots example") #suptitle is used to give a title to the entire figure, it is placed at the top of the figure and it is not affected by the individual plot titles
# plt.show()


#scatter plot

# plt.scatter(x1,y1,cmap='viridis',c=y1) #cmap is used to specify the color map, c is used to specify the color of the points based on the values of y1
# plt.colorbar() #colorbar is used to show the color scale for the points
# plt.show()


# #bar plot
# fruits=['apple','banana','orange','grape','mango']
# quantities=[10,20,15,5,25]
# plt.bar(fruits,quantities)
# # plt.barh(x2,y2) #horizontal bar plot
# plt.show()

#pie chart
labels=['apple','banana','orange','grape','mango']
sizes=[10,20,15,5,25]
gap=[0,0,0,0,0.2] #gap between slices, it is used to explode the slices
plt.pie(sizes,labels=labels,autopct='%1.1f%%',explode=gap) #autopct is used to show the percentage of each slice
plt.legend(title='Fruits')
plt.show()
