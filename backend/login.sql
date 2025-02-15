CREATE DATABASE user_auth;

USE user_auth;

CREATE TABLE users (,
    username VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(18) UNIQUE NOT NULL, 
);