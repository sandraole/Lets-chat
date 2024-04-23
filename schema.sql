DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS visitors CASCADE;
DROP TABLE IF EXISTS messages CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

CREATE TABLE visitors (
    id SERIAL PRIMARY KEY, 
    time TIMESTAMP
    );

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);

-- CREATE TABLE topics (
--     id SERIAL PRIMARY KEY,
--     name TEXT,
--     description TEXT
-- );

-- CREATE TABLE threads (
--     id SERIAL PRIMARY KEY,
--     topic_id INTEGER REFERENCES topics,
--     title TEXT,
--     created_at TIMESTAMP
-- );

-- CREATE TABLE replies (
--     id SERIAL PRIMARY KEY,
--     thread_id INTEGER REFERENCES threads,
--     user_id INTEGER REFERENCES users,
--     content TEXT,
--     sent_at TIMESTAMP
-- );