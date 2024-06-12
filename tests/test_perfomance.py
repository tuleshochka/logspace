import pytest
import mysql.connector
from utils import select_like, create_index, drop_index
import time

@pytest.fixture(scope="session")
def db_session():
    con = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              database='logspace')
    yield con
    con.close()
    
def test_perfomance_noindex(db_session, benchmark):
    con = db_session
    pattern = 'Take%'
    benchmark(select_like, con, pattern)
    
def test_perfomance_index(db_session, benchmark):
    con = db_session
    pattern = 'Take%'
    create_index(con)
    benchmark(select_like, con, pattern)
    drop_index(con)
