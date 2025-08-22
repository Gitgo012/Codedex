# Write code below 💖

#reading data from csv using csv module
# import csv

# # Open the CSV file in 'read' mode with UTF-8 encoding
# with open('example.csv', 'r', encoding='utf8') as file:
#   # Create a CSV reader object
#   csv_reader = csv.reader(file)

#   for row in csv_reader:
#     print(row)

import pandas as pd

df=pd.read_csv("D:\\Downloads\\Bestseller - Sheet1.csv")
#print the data in the csv file
print("columns in csv file are \n",df.columns.to_list())
print("data in csv is\n", df)
bestseller_info=df.loc[df['sales in millions'].idxmax()]
print("Book with highest sales: \n", bestseller_info)




df=pd.DataFrame([bestseller_info])
df.to_csv("bestseller_info.csv", index=False, header=True)
#verify the saved data
data=pd.read_csv("bestseller_info.csv")
print("data in new csv is\n",data)

#write to csv file
# data_to_write = [
#   ['Name', 'Age', 'Grade'],
#   ['Alice', 25, 'A'],
#   ['Bob', 22, 'B'],
#   ['Charlie', 28, 'A+']
# ]

# #open the csv file in write mode
# with open('output.csv','w', newline='') as file:
#   #create a new csv writer object
#   csv_writer=csv.writer(file)
#   #write the data to csv file
#   csv_writer.writerows(data_to_write)