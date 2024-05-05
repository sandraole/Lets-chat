--DROP TABLE IF EXISTS threads CASCADE;
--DROP TABLE IF EXISTS messages CASCADE;
DROP TABLE IF EXISTS messages CASCADE;
DROP TABLE IF EXISTS visitors CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Käyttäjät
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

-- Vierailijat
CREATE TABLE IF NOT EXISTS visitors (
    id SERIAL PRIMARY KEY, 
    time TIMESTAMP
);

-- Viestit
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    topic TEXT,
    content TEXT,
    created_at TIMESTAMP
);

-- Langat
--CREATE TABLE IF NOT EXISTS threads (
--    id SERIAL PRIMARY KEY,
--    topic_id INTEGER REFERENCES topics(id) ON DELETE CASCADE,
--    messages_id INTEGER REFERENCES messages(id) ON DELETE CASCADE,
--    title TEXT,
--    content TEXT
--);