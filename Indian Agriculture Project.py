#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#installing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[ ]:


#load the dataset 
data=pd.read_csv("agroData.csv")
data.head()


# In[ ]:


data.shape


# In[ ]:


#checking data set information
data.info()


# In[ ]:


#Checking the null values
data.isna().sum()/len(data)*100


# # DataPreprocessing Starts

# In[ ]:


#since the grade columns has 100% null values we will drop it
data=data.drop(["Grade"],axis=1)
print("The average values of the Min_x0020_Price is", data["Min_x0020_Price"].mean())
print("The average values of the Max_x0020_Price is", data["Max_x0020_Price"].mean())


# In[ ]:


#checking data after dropping the grade column
print(data.head(3))
print(data.info())


# In[ ]:


#filling the null values in Max and min prices with their respective average prices
data["Max_x0020_Price"].fillna(data["Max_x0020_Price"].mean())
data["Min_x0020_Price"].fillna(data["Min_x0020_Price"].mean())


# In[ ]:


#Now will check the duplicate values
print("The duplicates values in the data is" ,data.duplicated().sum())


# In[ ]:


#checking the statistics in the data
data.describe()


# In[ ]:


#checking the statistics in the data with stylish background
data.describe().style.background_gradient(cmap="gist_yarg_r")


# In[ ]:


#cheking the correlation map using the heatmap
sns.heatmap(data.corr(),annot=True,cmap="gnuplot2_r" , fmt=".2f",linewidths=1)
plt.title("The correlation Map")
plt.show()


# # Explore Data analysis

# ## Questions Asked from the Data

# In[ ]:


#Ques1,2: Some Unique states in the data

states_in_data=data["State"].unique()
print("\nThe Unique states in the Data are: ", states_in_data)


# In[ ]:


data["State"].nunique()


# In[ ]:


print("The most dominated state is ", data["State"].value_counts().idxmax())
print("The least dominate state is ", data["State"].value_counts().idxmin())


# In[ ]:


print("The most demanding commodity in the data is", data["Commodity"].value_counts().idxmax())
print("The less demanding commodity in the data is", data["Commodity"].value_counts().idxmin())


# In[ ]:


#Ques2: Creating Bar charts for states

data["State"].value_counts().sort_values(ascending=False)\
.plot(kind="bar", title="Visualize the States in the Data", figsize=(8,6),color="#bcbd22")
plt.xlabel("States")
plt.ylabel("Count of Values")
plt.show()
                                                                 


# In[ ]:


#creating bar chart to find the top 10 district in the data

data["State"].value_counts().nlargest(10).sort_values(ascending=False)\
.plot(kind="bar", title="Top 10 Districts in the Data", figsize=(8,6),color=["Green"])
plt.xlabel("District")
plt.ylabel("Count of Values")
plt.show()


# In[ ]:


#Calculate the most revenue generate in the market

data["Market_revenue"]=data["Min_x0020_Price"]+data["Max_x0020_Price"]+data["Modal_x0020_Price"]
label=["Nahan","Kollengode","Mumbai","Thodupuzha","Fish, Polutry & Egg Market, Gazipur","Pothencode","Shimoga","Yellapur","Siddapur","Palakkad"]
data.groupby("Market")["Market_revenue"].sum().sort_values(ascending=False).head(10)\
.plot(kind="pie", labels=label, colors=["red","blue","green","orange","yellow"],autopct='%1.2f%%',shadow=True)
plt.title("Most Revenued to Market in the data")
plt.show()


# In[ ]:


#creating the histogram with minimum price, maximum price and Modal Price


# In[ ]:


#creating the histogram with minimum price, maximum price and Modal Price
data[["Min_x0020_Price","Max_x0020_Price","Modal_x0020_Price"]].plot(kind="hist")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Distribution of the prices")
plt.show()


# In[ ]:


#creating the Scatter plot for minimum price and Modal Price
data.plot.scatter(x="Min_x0020_Price", y="Modal_x0020_Price",color="blue")
plt.xlabel("Min Price")
plt.ylabel("Modal Price")
plt.title("Relationship between Minimum and Modal Price")
plt.show()


# In[ ]:


#Finding the Average Price of the top 10 commodity in the data
avg_prices=data.groupby("Commodity")["Min_x0020_Price","Max_x0020_Price","Modal_x0020_Price"]
avg_prices.head(5).style.background_gradient(cmap="tab20b")


# In[ ]:


#creating the pie chart to visualize the top 10 commoditys in the data
color=["#0080FF","#F79F81","#00BFFF","#3ADF00","#7401DF","#FF0040"]
label=["Onion","Potato","Tomato","Brinjal","Green Chilli","Cauliflower","Cabbage","Wheat","Banana","Carrot"]
data["Commodity"].value_counts().sort_values(ascending =False).head(10)\
.plot(kind="pie",labels=label,colors=color,autopct="%1.2f%%",shadow=True)
plt.title("Top 10 Commodity in the data")
plt.show()


# In[ ]:


#to calculated the Most Revenue generated States
data["Revenue"]=data["Min_x0020_Price"]*data["Modal_x0020_Price"]
data.groupby("State")["Revenue"].sum().sort_values(ascending=False).head(10)\
.plot(kind="bar",title="Top 10 Most Revenue generated states",color=["#0080FF","#F79F81","#00BFFF","#3ADF00","#7401DF","#FF0040"])
plt.xlabel("State")
plt.ylabel("Sum of the Revenue")
plt.show()
      


# In[ ]:


#create a  pie chart to visualize Green chilli produced states
chilli=data[data["Commodity"]=="Green Chilli"]
label=["UP","Kerala","WB","Maharashtra","Haryana","Telangana","HP","Karnataka","MP","Gujrat"]
chilli["State"].value_counts().head(10).sort_values(ascending=False)\
.plot(kind="pie",labels=label,colors=["#F79F81","#00BFFF","#3ADF00","#7401DF","#FF0040"],autopct="%1.2f%%",shadow=True)
plt.title("Top 10 Green Chilli produced States")
plt.show()


# In[ ]:


#find the profit and loss states for the onion prices

current_maximum_price=2000
colors=["#82FA58","#F79F81","#00BFFF","#3ADF00","#7401DF","#FF0040"]
onion=data[data["Commodity"]=="Onion"]
onion["onion_profit"]=onion["Max_x0020_Price"]-current_maximum_price
onion.groupby("State")["onion_profit"].sum()\
.plot(kind="bar",figsize=(8,6),title="Most Profit and loss gained states in onions",color=colors)
plt.xlabel("Price")
plt.ylabel("States")
plt.show()


# In[ ]:


#find the profit and loss states for the onion prices

current_maximum_price=2000
colors=["#82FA58","#F79F81","#00BFFF","#3ADF00","#7401DF","#FF0040"]
onion=data[data["Commodity"]=="Onion"]
onion["onion_profit"]=onion["Max_x0020_Price"]-current_maximum_price
onion.groupby("State")["onion_profit"].sum()\
.plot(kind="barh",title="Most Profit and loss gained states in onions",color=colors)
plt.xlabel("Price")
plt.ylabel("States")
plt.show()


# In[ ]:


#To calculate the most profitable states in Apple sales with cuurent_apple_price

current_apple_price=8225
colors=["red","blue","green","purple","yellow","#FF0040"]
apple =data[data["Commodity"]=="Apple"]
apple["Profit"]=data["Min_x0020_Price"]-current_apple_price
apple.groupby("State")["Profit"].sum().sort_values(ascending=False)\
.plot(kind="barh",title="Most Profitable State in Apple Fruits",color=colors)
plt.xlabel("Price")
plt.ylabel("State")
plt.show()


# In[ ]:


#maximum price to produced rice in state wise

rice=data[data["Commodity"]=="Rice"]
colors=["red","blue","green","purple","orange"]
rice.groupby("State")["Max_x0020_Price"].mean().sort_values(ascending=False).plot(kind="bar",color=colors,figsize=(8,6),title="Most Profitable States in Apple Fruits")
plt.xlabel("States")
plt.ylabel("Average Maximum Price")
plt.show()


# In[ ]:


#create a  pie chart to visualize top 10 most rice states
rice=data[data["Commodity"]=="Rice"]
colors=["#F79F81","#00BFFF","#3ADF00","#7401DF","#FF0040"]
label=["Burdwan","Birbhum","Darjeeling","Bankura","Shimoga","howrah","Gulbarga","Gautam Budh Nagar","Mallapuram","Thane"]
rice.groupby("District")["Max_x0020_Price"].sum().sort_values(ascending=False).head(10)\
.plot(kind="pie",labels=label,colors=colors,autopct="%1.2f%%",shadow=True)
plt.title("Top 10 Rice produced Price District")
plt.show()


# In[ ]:


#Find the Variety of the sold for the minimum prices
# variety_min_price_sum=rice.groupby(["State","Variety"])["Min_x0020_Price"].sum().sort_values(ascending = False).head(10)
# sns.barplot(x=variety_min_price_sum["Variety"],y=variety_min_price_sum["Min_x0020_Price"],figsize=(8,6))
# plt.xlabel("Variety")
# plt.ylabel("Sum of Minimum Price")
# plt.title("Sum of Minimum Price by Variety and State")
# plt.xticks(rotation=90)
# plt.show()


# In[ ]:


##creating the Bar chart to visualize the top 10 commodity minimum price in the  Himachal Pradesh
color=["#0080FF","#F79F81","#00BFFF","#3ADF00","#7401DF"]
Himachal=data[data["State"]=="Himachal Pradesh"]
Himachal.groupby("Commodity")["Max_x0020_Price"].mean().head(10).sort_values(ascending=False)\
.plot(kind="bar",title="Top 10 Commodity in HP",color=color)
plt.xlabel("Commodity")
plt.ylabel("Average Minimum Price of the Commodity")
plt.show()


# In[ ]:


#Top 10 Demanding commodity in the Telangana
telangana=data[data["State"]=="Telangana"]
telangana.groupby("Commodity")["Max_x0020_Price"].sum().head(10).sort_values(ascending=False)\
.plot(kind="bar",title="Top 10 Demanding commodity in the Telangana ",color=["green","orange","red","purple","yellow"])
plt.xlabel("Commodity")
plt.ylabel("Sum of the Maximum Price")
plt.show()


# In[ ]:


#Finding the top 10 minimum and maximumvalues of the commodity with minimum prices
commodity_stats=data.groupby("Commodity")["Min_x0020_Price"].agg(["min","max"])
commodity_stats.head(10).style.background_gradient(cmap="nipy_spectral_r")


# In[ ]:


#create pie chart to understand the commodity in Andhra Pradesh
andhra_pradesh=data[data["State"]=="Andhra Pradesh"]
andhra_pradesh["Commodity"].value_counts().sort_values(ascending =False)\
.plot(kind="pie",labels=["Tomato","Gur","Dry chillies","paddy","Trumeric","Lemon","black gram","jowar"],colors=["green","orange","red","purple","blue","pink","yellow","brown"],autopct="%1.2f%%", shadow=True)
plt.title("Andhra Pradesh Commodity in the Data")
plt.show()


# In[ ]:


Market_price_range=data.groupby("Market")["Min_x0020_Price","Max_x0020_Price"].agg(["min","max"])
Market_price_range.head(10).style.background_gradient(cmap="twilight_shifted")


# In[ ]:


Market_price_range=data.groupby("Market")["Min_x0020_Price","Max_x0020_Price"]
Market_price_range.head(10).style.background_gradient(cmap="twilight_shifted")


# In[ ]:


state_stats=data.groupby("State").agg({"Min_x0020_Price":["mean","median","max","min"]})
state_stats.style.background_gradient(cmap="inferno")


# In[ ]:


#create a bar chart to find the top 10 market with minumum price
colors=["#82FA58","#F79F81","#00BFFF","#3ADF00","#7401DF"]
data.groupby("Market")["Min_x0020_Price"].mean().nlargest(10).sort_values(ascending=False)\
.plot(kind="bar",title="Top 10 Markets with Average Minimum Price",figsize=(8,6),color=colors)
plt.xlabel("Market")
plt.ylabel("Average Minimum Price")
plt.show()


# In[ ]:


#Top 10 District with average_min_price

colors=["#82FA58","#F79F81","#00BFFF","#3ADF00","#7401DF"]
data.groupby("District")["Min_x0020_Price"].mean().nlargest(10).sort_values(ascending=False)\
.plot(kind="bar",title="Top 10 Districts with Average Minimum Price",figsize=(8,6),color=colors)
plt.xlabel("District")
plt.ylabel("Average Minimum Price")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




