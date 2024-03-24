import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
x = pd.read_csv('./diwali_sales_data.csv')
print(x.head())
print(x.shape)

# data_cleaning

y= x.drop(['Status','unnamed1'] , axis = 1 , inplace = True)
print(x)
print(x.isnull().sum())
y = x.dropna(inplace = True) #deleted all the null values
print(x.isnull().sum())
print(x.info())
x['Amount'] = x['Amount'].astype(int)
print(x.info())
print(x[['Age', 'Amount', 'Orders']].describe())

# data_analysis

print(x.columns)
# ax = sns.countplot(x = 'Gender', data = x )
# plt.show()

# from the plot, it is clearly evident that females bought more diwali items than males (more than twice)

# t = x.groupby(['Gender'] , as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending= False)
# print(t)
# s = sns.barplot(x = 'Gender' , y = 'Amount', data = t)
# plt.show()

n = x.groupby(['Gender','Age Group'])['Age Group'].count()
print(n)    # females of age 26-35 bought diwali gifts more than any other group ages/ same for males

# m = sns.countplot(x = 'Age Group', hue = 'Gender', data = x)
# plt.show()

m = x.groupby(['Marital_Status', 'Gender'], as_index = True)['Marital_Status'].count()
print(m)

# z = sns.countplot(x = 'Gender', hue = 'Marital_Status', data = x)
# plt.show()  # females who are non married bought gifts more

z = x.groupby(['Zone', 'Occupation', 'Gender'], as_index= True)['Occupation'].count()
print(z)

# t = sns.countplot( x = 'Zone' , hue = 'Gender' , data = x)
# plt.show()  #most of the people are from central zone which are females

t = x.groupby(['State'], as_index= False )['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)
print(t)

# c = sns.set(rc = {'figure.figsize':(15,5)})
# b = sns.barplot(x = 'State' , y = 'Orders', data = t)
# plt.show()
#uttar pradesh has many customers who bought diwali items followed by maharashtra, and karnataka

# c = x.groupby(['Occupation','Gender'], as_index= False)['Orders'].sum().sort_values(by = 'Orders', ascending= False).head(10)
# b = sns.set({'figure.figsize':[15,5]})
# d = sns.barplot(x = 'Occupation', y = 'Orders' ,hue = 'Gender', data = c)
# plt.show()   # most of the people are from IT sector which are again females(majority) followed by healthcare and aviation sector

print(x.columns)

# c = x.groupby(['State'],as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
# e = sns.set({'figure.figsize':[30,7]})
# d = sns.barplot(x = 'State', y = 'Amount', data = c)
# plt.show()

c = x.groupby(['Product_Category'])['Product_Category'].count().sort_values(ascending = False).head(10)
print(c)   #most bought product category is clothing and apparel, food, electronics and gadegts

# target_type = 'IT Sector'
# e = sns.set({'figure.figsize':[20,5]})
# d = sns.countplot(x = 'Product_Category', data = x[x['Occupation']== target_type])
# plt.show()
#people of IT sector bought clothes in high quantity

j = x.groupby(['Age Group','Product_Category'])['Product_Category'].count()
print(j)

# k = sns.set({'figure.figsize':[15,5]})
# l = sns.countplot(x= 'Product_Category', data = x[x['Age Group']== '0-17'])
# plt.show()
#the age group 0-17 product category = food

# k = sns.set({'figure.figsize':[15,5]})
# l = sns.countplot(x= 'Product_Category', data = x[x['Age Group']== '18-25'])
# plt.show()
#the age group 18-25 product category = food

# k = sns.set({'figure.figsize':[15,5]})
# l = sns.countplot(x= 'Product_Category', data = x[x['Age Group']== '26-35'])
# plt.show()
#the age group 26-35 product category = clothing and apparel

# k = sns.set({'figure.figsize':[15,5]})
# l = sns.countplot(x= 'Product_Category', data = x[x['Age Group']== '36-45'])
# plt.show()
#the age group 36-45 product category = clothing and apparel

# k = sns.set({'figure.figsize':[15,5]})
# l = sns.countplot(x= 'Product_Category', data = x[x['Age Group']== '46-50'])
# plt.show()
#the age group 46-50 product category = clothing and apparel
# k = sns.set({'figure.figsize':[15,5]})
# l = sns.countplot(x= 'Product_Category', data = x[x['Age Group']== '51-55'])
# plt.show()
#the age group 51-55 product category = clothing and apparel and increase in electronic devices also
# k = sns.set({'figure.figsize':[15,5]})
# l = sns.countplot(x= 'Product_Category', data = x[x['Age Group']== '55+'])
# plt.show()
#the age group 55+ product category = clothing and food both


o = x.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by ='Amount', ascending=False)
u = sns.set(rc ={'figure.figsize':[20,5]})
p = sns.barplot(x = 'Product_Category', y ='Amount', data = o)
plt.show()
#food category has total highest amount, clothing and then electronics and gadgets




#CONCLUSION
#females(especially who are non married) bought more diwali items than males
#age group 26-35 bought more gifts than any other age group
#people from the central zone bought more gifts
#highest number of sales are from uttar Pradesh followed by Maharashtra and karnataka
#people from IT sector bought more gifts followed by healthcare, and aviation sectors (signifies high purchasing power)
#people had a great interest in buying clothing folowed by food, and electronic gadgets
#age group 0-25 invested more on food whereas age group above 26 invested more on clothing
