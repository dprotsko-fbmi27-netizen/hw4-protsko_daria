CREATE DATABASE IF NOT EXISTS my_database
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE my_database;

DROP TABLE IF EXISTS titanic;

CREATE TABLE titanic (
    PassengerId INT PRIMARY KEY,
    Survived TINYINT NOT NULL,
    Pclass TINYINT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Sex VARCHAR(20) NOT NULL,
    Age DECIMAL(5,2) NULL,
    SibSp INT NOT NULL,
    Parch INT NOT NULL,
    Ticket VARCHAR(100) NOT NULL,
    Fare DECIMAL(10,4) NOT NULL,
    Cabin VARCHAR(100) NULL,
    Embarked CHAR(1) NULL
);

LOAD DATA INFILE '/var/lib/mysql-files/titanic.csv'
INTO TABLE titanic
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    PassengerId,
    Survived,
    Pclass,
    Name,
    Sex,
    @Age,
    SibSp,
    Parch,
    Ticket,
    Fare,
    @Cabin,
    @Embarked
)
SET
    Age = NULLIF(@Age, ''),
    Cabin = NULLIF(@Cabin, ''),
    Embarked = NULLIF(TRIM(TRAILING '\r' FROM @Embarked), '');
    