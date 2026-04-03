CREATE DATABASE RetailDB;
USE RetailDB;

CREATE TABLE Sales (
    TransactionID VARCHAR(20),
    TransactionTime DATETIME,
    ItemCode VARCHAR(20),
    ItemDescription VARCHAR(255),
    Quantity INT,
    CostPerItem FLOAT,
    Country VARCHAR(50)
);
