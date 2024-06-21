CREATE TABLE sales_orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    shipping_address VARCHAR(255) NOT NULL,
    payment_method VARCHAR(20) NOT NULL,
);

CREATE TABLE sales_order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES sales_orders(order_id),
    item_id INT REFERENCES inventory(item_id),
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
);
    