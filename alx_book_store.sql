CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

-- Table: Books
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT FOREIGN KEY REFERENCES authors(author_id),
    price DOUBLE,
    publication_date DATE
);

-- Table: Authors
CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215)
);

-- Table: Customers

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215) UNIQUE,
    address TEXT
);

-- Table: Orders

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT FOREIGN KEY REFERENCES customers(customer_id),
    order_date DATE
);

-- Table: Order_Details
CREATE TABLE order_details (
    orderdetail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES orders(order_id),
    book_id INT FOREIGN KEY REFERENCES books(book_id)
);