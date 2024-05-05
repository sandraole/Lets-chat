from db import db
from sqlalchemy import text

def add_like(user_id, message_id):
    sql = text('INSERT INTO likes (user_id, message_id) VALUES (:user_id, :message_id)')
    db.session.execute(sql, {'user_id': user_id, 'message_id': message_id})
    db.session.commit()
    return True

def remove_like(user_id, message_id):
    sql = text('DELETE FROM likes WHERE user_id = :user_id AND message_id = :message_id')
    db.session.execute(sql, {'user_id': user_id, 'message_id': message_id})
    db.session.commit()
    return True

def get_list():
    sql = text('''
        SELECT M.id, M.content, U.username, M.created_at, M.topic, COUNT(L.id) AS likes
        FROM messages M
        LEFT JOIN likes L ON M.id = L.message_id
        JOIN users U ON M.user_id = U.id
        GROUP BY M.id, U.username, M.content, M.created_at, M.topic
        ORDER BY M.created_at DESC
    ''')
    result = db.session.execute(sql)
    return result.fetchall()
# "Likes" on määritelty väärin profile.html:ssä ja sen vuoksi tykkäysten määrä ei näy, kun antaa tykkäyksen

