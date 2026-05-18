import mysql.connector
import pandas as pd


db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="vaishumanu",
    database="healthcaredb"
)

query="select*from sales_data"
df=pd.read_sql(query,db)

df['total_revenue']=df['price_per_unit']* df['quantity_sold']

print("---retail sales report---")
print(df)

top_category = df.groupby('category')['total_revenue'].sum()
print("\n---revenue by category---")
print(top_category)

df.to_excel("retail_sales_final_report.xlsx",index=False)
print("\n--- done your excel report is ready---")

import matplotlib.pyplot as pit
category_data = df.groupby('category')['total_revenue'].sum()

category_data.plot(kind='bar',color='orange')

pit.title('revenue by category')
pit.xlabel('product category')
pit.ylabel('total revenue')
pit.savefig('category_revenue_chart.png')
pit.show()
db.close()