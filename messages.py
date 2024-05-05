from db import db
from sqlalchemy import text
import users

def get_list():
    sql = text('SELECT M.content, U.username, M.created_at, M.topic FROM messages M JOIN users U ON M.user_id = U.id ORDER BY M.id')
    result = db.session.execute(sql)
    return result.fetchall()

def send(content, topic):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text('INSERT INTO messages (content, user_id, topic, created_at) VALUES (:content, :user_id, :topic, NOW())')
    db.session.execute(sql, {'content': content, 'user_id': user_id, 'topic': topic})
    db.session.commit()
    return True

def search_messages(query):
    sql = text("SELECT M.content, U.username, M.created_at, M.topic FROM messages M JOIN users U ON M.user_id = U.id WHERE M.content ILIKE :query OR M.topic ILIKE :query ORDER BY M.created_at DESC")
    result = db.session.execute(sql, {'query': f'%{query}%'})
    return result.fetchall()

