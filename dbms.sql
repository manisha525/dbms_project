CREATE TABLE Product(prod_id CHAR(10), pname VARCHAR(30), price DECIMAL);

ALTER TABLE Product ADD CONSTRAINT pk_product PRIMARY KEY (prod_id);
ALTER TABLE Product ADD CONSTRAINT ck_product_price CHECK (price > 0);

CREATE TABLE Depot(dep_id CHAR(10), addr VARCHAR(30), volume INTEGER);

ALTER TABLE Depot ADD CONSTRAINT pk_depot PRIMARY KEY (dep_id);
ALTER TABLE Depot ADD CONSTRAINT ck_depot_volume CHECK (volume >= 0);

CREATE TABLE Stock (prod_id CHAR(10), dep_id CHAR(10), quantity INTEGER, PRIMARY KEY (prod_id, dep_id), FOREIGN KEY (prod_id) REFERENCES Product (prod_id) , FOREIGN KEY (dep_id) REFERENCES Depot (dep_id) ON UPDATE CASCADE);

INSERT INTO Product (prod_id, pname, price) VALUES ('p1', 'Tape', 2.5), ('p2', 'TV', 250), ('p3', 'VCR', 80);

INSERT INTO Depot (dep_id, addr, volume) VALUES ('d1', 'New York', 9000), ('d2', 'Syracuse', 6000), ('d4', 'New York', 2000);

INSERT INTO Stock (prod_id, dep_id, quantity) VALUES ('p1', 'd1', 1000), ('p1', 'd2', -100), ('p1', 'd4', 1200), ('p3', 'd1', 3000), ('p3', 'd4', 2000), ('p2', 'd4', 1500), ('p2', 'd1', -400), ('p2', 'd2', 2000);
