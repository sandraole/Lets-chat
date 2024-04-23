DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS visitors CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    role INTEGER
);

CREATE TABLE visitors (
    id SERIAL PRIMARY KEY, 
    time TIMESTAMP
    );

