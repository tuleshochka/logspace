import pytest
import mysql.connector
from utils import select_like, create_index, drop_index

@pytest.fixture(scope="session")
def db_session():
    con = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              database='logspace')
    yield con
    con.close()

def test_func_noindex(db_session):
    con = db_session
    pattern = 'Take%'
    rows = select_like(con, pattern)
    assert len(rows) == 2065
    
def test_func_index(db_session):
    con = db_session
    pattern = 'Take%'
    create_index(con)
    rows = select_like(con, pattern)
    assert len(rows) == 2065
    drop_index(con)

def test_functional_compare(db_session):
    con = db_session
    pattern = 'Take%'
    no_index_rows = select_like(con, pattern)
    create_index(con)
    index_rows = select_like(con, pattern)
    assert len(no_index_rows) == len(index_rows)
    drop_index(con)