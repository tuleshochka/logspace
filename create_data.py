import mysql.connector
from mimesis import Text
from utils import drop_index, generate_text, select_count, create_table
from datetime import date

def create_data(con, number):
    rows_number = select_count(con)
    if number > rows_number:
        cursor = con.cursor()
        text = Text('ru')
        date_to_insert = date.today().strftime('%Y-%m-%d')
        rows = number-rows_number
        for i in range(rows):
            sentence = generate_text(text, 200)
            query = "INSERT INTO ttable (date, str) VALUES (%s, %s)"
            cursor.execute(query, (date_to_insert, sentence))
        con.commit()

if __name__ == "__main__":
    con = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              database='logspace')
    create_table(con)
    create_data(con, 10_000_000)
    con.close()