# db_init.sql
# Keril Ivanchuk
# 02/23/2023
# whatabook database initialization script


# drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

# create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

# grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

# drop tables if they exist, mainly for anyone from class/teacher testing code
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS whatabook;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

# Creating all the tables

CREATE TABLE whatabook (
    store_id    INT             NOT NULL,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE books (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    author      VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    FOREIGN KEY (book_id)
        REFERENCES books(book_id),
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


# insert whatabook location record 

INSERT INTO whatabook(store_id, locale)
    VALUES('1','1234 Plain Street Lincoln, Nebraska 68501');

# insert book records 

INSERT INTO books(book_name, details, author)
    VALUES('From the Ground UP', 'Hard Cover, New', 'Keril Ivanchuk');

INSERT INTO books(book_name, details, author)
    VALUES('Into the Bold Sky', 'Soft Cover, New', 'Keril Ivanchuk');

INSERT INTO books(book_name, details, author)
    VALUES('The Flight', 'Hard Cover, Used', 'Keril Ivanchuk');

INSERT INTO books(book_name, details, author)
    VALUES('Keril Ivanchuk - Reliving a life worth living', 'Hard Cover, New', 'Sammy Ivanchuk');

INSERT INTO books(book_name, details, author)
    VALUES('Descending to Land Untouched', 'Soft Cover, Used', 'Sammy Ivanchuk');

INSERT INTO books(book_name, details, author)
    VALUES('On our feet, the road to Safety', 'Hard Cover, Used', 'Sammy Ivanchuk');

INSERT INTO books(book_name, details, author)
    VALUES('From those who care, the path back home', 'Hard Cover, New', 'Sammy Ivanchuk');

INSERT INTO books(book_name, details, author)
    VALUES('Home, at last', 'Hard Cover, Used', 'Sammy Ivanchuk');

INSERT INTO books(book_name, details, author)
    VALUES('The Epic of Gryph - FLIGHT', 'Soft Cover, Used', 'Sammy Ivanchuk');

# insert user

INSERT INTO user(first_name, last_name) 
    VALUES('Keril', 'Ivanchuk');

INSERT INTO user(first_name, last_name)
    VALUES('Sammy', 'Ivanchuk');

INSERT INTO user(first_name, last_name)
    VALUES('Kyle', 'Budner');

# insert wishlist records 

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Keril'), 
        (SELECT book_id FROM books WHERE book_name = 'Home, at last')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Sammy'),
        (SELECT book_id FROM books WHERE book_name = 'From the Ground UP')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Kyle'),
        (SELECT book_id FROM books WHERE book_name = 'Keril Ivanchuk - Reliving a life worth living')
    );