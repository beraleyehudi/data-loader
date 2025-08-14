CREATE TABLE students(
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(20) NOT NULL,
    age INT CHECK (age > 0),
);