CREATE TABLE carros(
	id SERIAL primary key,
	marca varchar(100),
	modelo varchar(100),
	ano integer	
);

INSERT INTO carros(marca, modelo, ano) VALUES ('Chevrolet', 'Omega', 1995);
INSERT INTO carros(marca, modelo, ano) VALUES ('Ford', 'Mondeo', 1997);
INSERT INTO carros(marca, modelo, ano) VALUES ('JAC Motors', 'J3', 2009);
INSERT INTO carros(marca, modelo, ano) VALUES ('Hyundai', 'HB20', 2015);
INSERT INTO carros(marca, modelo, ano) VALUES ('Nissan', 'Sentra', 2016);
INSERT INTO carros(marca, modelo, ano) VALUES ('Toyota', 'Corolla', 2009);
INSERT INTO carros(marca, modelo, ano) VALUES ('Fiat', 'Tipo', 1996);
INSERT INTO carros(marca, modelo, ano) VALUES ('VW', 'Jetta Variant', 2012);
INSERT INTO carros(marca, modelo, ano) VALUES ('BMW', '118', 2013);