from faker import Faker

fake = Faker()

def create_table(con):
  cursor = con.cursor()
  query = """CREATE TABLE IF NOT EXISTS ttable (
  id int NOT NULL AUTO_INCREMENT,
  date date NOT NULL,
  str varchar(255) NOT NULL,
  PRIMARY KEY (id)
  )"""
  cursor.execute(query)

def generate_text(text_generator, max_length):
  sentence = text_generator.sentence()
  if len(sentence) > max_length:
      return sentence[:max_length] + '...'
  else:
      return sentence

def select_count(con):
  cursor = con.cursor()
  query = "SELECT COUNT(*) FROM ttable"
  cursor.execute(query)
  result = cursor.fetchone()[0]
  return int(result)
  
def create_index(con):
  cursor = con.cursor()
  query = "CREATE INDEX str_idx ON ttable(str)"
  cursor.execute(query)
  con.commit()
    
def drop_index(con):
  cursor = con.cursor()
  query = "DROP INDEX str_idx ON ttable"
  cursor.execute(query)
  con.commit()
    
def select_like(con, pattern):
  cursor = con.cursor()
  query = "SELECT * FROM ttable WHERE str LIKE %s"
  cursor.execute(query, (pattern,))
  rows = cursor.fetchall()
  return rows