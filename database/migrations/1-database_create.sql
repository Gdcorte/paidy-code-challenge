CREATE TABLE restaurant.orders (
	id VARCHAR(50),
    item_name TEXT NOT NULL,
    table_number INT NOT NULL,
    time_to_cook INT NOT NULL,
    
    PRIMARY KEY (id)
);