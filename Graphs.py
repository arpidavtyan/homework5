
# coding: utf-8

# In[53]:


from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
import numpy as np
import quandl
quandl.ApiConfig.api_key = "xhp4sV5t6fVz3gVq8sxH"
mydata = quandl.get("FRED/GDP")
import pandas as pd

mydata.head()
y_value=mydata['Value']
x_value= pd.to_datetime(mydata.index.values)
trace = go.Scatter(x=x_value,y=y_value,mode="lines",fill="tozeroy")

data = [trace]
figure = dict(data=data)
iplot(figure)



# In[92]:




mydata1 = quandl.get("BCHARTS/ABUCOINSUSD",transformation="rdiff")
mydata2 = quandl.get("WIKI/GOOGL",transformation="rdiff")
mydata1.head()
x_values1 = mydata1['Close']
x_values2 = mydata2["Close"]

trace1 = go.Box(x=x_values1,name='Bitcoin')
trace2= go.Box(x=x_values2,name='Google')

data1 = [trace1,trace2]
figure1 = dict(data=data1)
iplot(figure1)



# In[75]:



header = dict(values=['Google', 'Bitcoin'],
             fill=dict(color='dodgerblue')
             )
cells = dict(values=[round(mydata2.Close[1:5,],3),
                    round(mydata1.Close[1:5],3)],
             fill=dict(color=["yellow","white"])
            )
trace3 = go.Table(header=header, cells=cells)

data2 = [trace3]
layout3 = dict(width=400, height=400)
figure2 = dict(data=data2,layout=layout3)
iplot(figure2)




# In[91]:



import plotly.figure_factory as ff
df = [dict(Task="Task 1", Start='2009-01-01', Finish='2009-01-31',Resource='Idea Validation'),
      dict(Task="Task 2", Start='2009-03-01', Finish='2009-04-15',Resource='Prototyping'),
      dict(Task="Task 3", Start='2009-04-17', Finish='2009-09-30',Resource='Team Formation')]

figure3 = ff.create_gantt(df,index_col='Resource', show_colorbar=True,title='Startup Roadmap')
iplot(figure3, filename='gantt-simple-gantt-chart')


# In[98]:


x22 = [20,17,53,18]
x11 = [-38,-7,-53,-18]
y11 = ['x1','x2','x3','x4']
y22 = ['x5','x6','x7','x8']
trace4 = go.Bar(x = x11, y = y11, 
               orientation='h', name = '<b>Negative</b>'
             )
trace5 = go.Bar(x = x22, y = y22, 
               orientation='h', name = 'Positive'
            )


layout8 = go.Layout(
    title = '<b>Correlations with employees probability of churn</b>',
    yaxis = dict(autorange='reversed', title ='Variable' )
)
data6 = [trace4,trace5]
figure4 = dict(data=data6, layout = layout8)
iplot(figure4)

