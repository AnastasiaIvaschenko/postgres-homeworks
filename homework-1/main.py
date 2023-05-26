"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

conn = psycopg2.connect(dbname='north', user='postgres', password='pastasea84', host='localhost')

file_path_customers = os.path.join("north_data/customers_data.csv")
file_path_employees = os.path.join("north_data/employees_data.csv")
file_path_orders = os.path.join("north_data/orders_data.csv")

cur = conn.cursor()

# with open('north_data/customers_data.csv', 'r', encoding='utf-8') as file:
#     data_customers = csv.reader(file, delimiter=',')
#
#     for row in data_customers:
#         customers = cur.execute(f"INSERT INTO customers VALUES ({row[0]}, {row[1]}, {row[2]})")

with open(file_path_customers, 'r') as file:
    data_customers = file.readlines()

for row in data_customers:
    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", tuple(row.strip().split(",")))

with open(file_path_employees, 'r') as file:
    data_employees = file.readlines()

for row in data_employees:
    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", tuple(row.strip().split(",")))

with open(file_path_orders, 'r') as file:
    data_orders = file.readlines()

for row in data_orders:
    orders = cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", tuple(row.strip().split(",")))

conn.commit()
cur.close()
conn.close()

