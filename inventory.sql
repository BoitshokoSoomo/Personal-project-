CREATE TABLE inventory (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);