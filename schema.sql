CREATE DATABASE IF NOT EXISTS Product;
USE Product;
DROP TABLE IF EXISTS Product CASCADE;

CREATE TABLE Product(
	pid INTEGER AUTO_INCREMENT,
    pname VARCHAR(100),
    description VARCHAR(255),
    price REAL,
    CHECK (price > 0),
    PRIMARY KEY(pid));

INSERT INTO Product(pname,description, price) VALUES ('Bed frame', "White, easy to unfold", 30);
INSERT INTO Product(pname,description, price) VALUES ('Mattress', "Zinus 12-inch memory foam", 85);
INSERT INTO Product(pname,description, price) VALUES ('Floor lamp', "Bought from Amazon. 5 different lightness and color", 25);

SELECT * FROM Product;

