CREATE DATABASE user_auth;
SET GLOBAL event_scheduler = ON;


CREATE TABLE users (,
    username VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL, 
    courses TEXT NOT NULL,
    points INT NOT NULL,
    major TEXT NOT NULL
);

ON SCHEDULE EVERY 1 WEEK STARTS '2025-02-16 00:00:00'
DO
UPDATE users SET points = 0;
USE user_auth;