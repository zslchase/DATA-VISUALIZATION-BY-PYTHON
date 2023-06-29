import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

input_values=[1,2,3,4,5,6]
squares=[1,4,9,16,25,36]

fig,ax=plt.subplots()
ax.plot(input_values,squares,linewidth=3)
ax.set_title('平方数')
ax.set_xlabel("值")
ax.set_ylabel("值的平方")
ax.tick_params(axis='both',labelsize=14)#设置刻度线格式

plt.show()