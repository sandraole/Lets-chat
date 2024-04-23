from db import db
from sqlalchemy import text

def add_visit():
    sql = text('INSERT INTO visitors (time) VALUES (NOW())')
    db.session.execute(sql)
    db.session.commit()

def get_counter():
    sql = text('SELECT COUNT(*) FROM visitors')
    result = db.session.execute(sql)
    counter = result.fetchone()[0]
    return counter
