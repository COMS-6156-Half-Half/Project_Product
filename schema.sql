CREATE DATABASE IF NOT EXISTS product;
USE product;
DROP TABLE IF EXISTS products CASCADE;

CREATE TABLE products(
	pid INTEGER AUTO_INCREMENT,
    pname VARCHAR(100),
    description VARCHAR(255),
    location VARCHAR(100),
    price INTEGER,
    ptype VARCHAR(100),
    retailer_link VARCHAR(500),
    CHECK (price > 0),
    PRIMARY KEY(pid));

INSERT INTO products(pname,description, price, ptype, location) VALUES ('Bed frame', 'White, easy to unfold', 30, 'bed','245 W 109th St');
INSERT INTO products(pname,description, price) VALUES ('Mattress', "Zinus 12-inch memory foam", 85);
INSERT INTO products(pname,description, price) VALUES ('Floor lamp', "Bought from Amazon. 5 different lightness and color", 25);


