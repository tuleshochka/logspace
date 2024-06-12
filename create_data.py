import time
from faker import Faker
import mysql.connector
from utils import create_index, drop_index, generate_text, select_count, create_table, select_like
from datetime import date

def create_data(con, number):
    rows_number = select_count(con)
    if number > rows_number:
        fake = Faker()
        cursor = con.cursor()
        date_to_insert = date.today().strftime('%Y-%m-%d')
        rows = number-rows_number
        for i in range(rows):
            sentence = fake.text(max_nb_chars=200)
            query = "INSERT INTO ttable (date, str) VALUES (%s, %s)"
            cursor.execute(query, (date_to_insert, sentence))
        con.commit()

if __name__ == "__main__":

    con = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              database='logspace')
    create_table(con)
    create_data(con, 2_000_000)
    con.close()