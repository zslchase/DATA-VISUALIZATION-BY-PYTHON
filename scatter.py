import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

input_values=[1,2,3,4,5,6]
squares=[1,4,9,16,25,36]

fig,ax=plt.subplots(1,2)
ax[0].scatter(input_values,squares,c='red',s=20,)#散点颜色，大小
ax[0].set_title('平方数')
ax[0].set_xlabel("值")
ax[0].set_ylabel("值的平方")
ax[0].axis([1,5,1,25]) #设置坐标轴范围

#颜色映射

x_values=range(1,1000)
y_values=[x*x for x in x_values]
ax[1].scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)



plt.show()