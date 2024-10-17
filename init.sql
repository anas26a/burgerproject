CREATE TABLE menu_items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    description TEXT,
    price NUMERIC(10, 2)
);

INSERT INTO menu_items (name, description, price) VALUES
('Classic Burger', 'A delicious beef burger with lettuce, tomato, and cheese.', 8.99),
('Chicken Burger', 'Grilled chicken with mayo and lettuce.', 7.99),
('Veggie Burger', 'A hearty veggie patty with fresh veggies.', 6.99);
