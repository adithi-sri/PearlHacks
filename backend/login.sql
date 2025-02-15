CREATE DATABASE user_auth;

USE user_auth;

CREATE TABLE users (,
    username VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL, 
    courses TEXT NOT NULL,
    points INT NOT NULL,
    major TEXT NOT NULL
);