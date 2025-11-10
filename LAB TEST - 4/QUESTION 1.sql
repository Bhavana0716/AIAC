-- Drop existing tables to avoid conflicts
DROP TABLE IF EXISTS Order_Items;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Menu_Items;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Restaurants;

-- Create Restaurants table
CREATE TABLE Restaurants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(20)
);

-- Create Customers table
CREATE TABLE Customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address VARCHAR(255)
);

-- Create Menu_Items table
CREATE TABLE Menu_Items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    is_vegetarian BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(id) ON DELETE CASCADE
);

-- Create Orders table
CREATE TABLE Orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    restaurant_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(20) DEFAULT 'PLACED',
    FOREIGN KEY (customer_id) REFERENCES Customers(id) ON DELETE CASCADE,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(id) ON DELETE CASCADE
);

-- Create Order_Items table
CREATE TABLE Order_Items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    menu_item_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    item_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(id) ON DELETE CASCADE,
    FOREIGN KEY (menu_item_id) REFERENCES Menu_Items(id) ON DELETE CASCADE
);

-- Insert sample Restaurants
INSERT INTO Restaurants (name, address, phone) VALUES
('Spice Villa', '1 MG Road, Bangalore', '080-1111111'),
('Royal Bites', 'Brigade Road, Bangalore', '080-2222222'),
('Cozy Cafe', 'Koramangala, Bangalore', '080-3333333');

-- Insert sample Customers
INSERT INTO Customers (name, email, phone, address) VALUES
('Asha Sharma', 'asha.sharma@example.com', '9876543210', 'Indiranagar'),
('Rahul Verma', 'rahul.verma@example.com', '9123456780', 'Jayanagar'),
('Priya Singh', 'priya.singh@example.com', '9988776655', 'Whitefield');

-- Insert sample Menu Items
INSERT INTO Menu_Items (restaurant_id, name, description, price, is_vegetarian) VALUES
(1, 'Butter Chicken Thali', 'Rich butter chicken with sides', 450.00, FALSE),
(1, 'Lamb Rogan Josh (Family Platter)', 'Serves 3-4, premium lamb', 1200.00, FALSE),
(2, 'Royal Paneer Platter', 'Paneer cooked in royal spices', 550.00, TRUE),
(2, 'Gourmet Prawns', 'Tiger prawns in garlic butter', 799.00, FALSE),
(3, 'Veg Salad', 'Fresh organic salad', 250.00, TRUE),
(3, 'Signature Steak', '250g premium steak', 999.00, FALSE);

-- Insert sample Orders
INSERT INTO Orders (customer_id, restaurant_id, order_date, total_amount, status) VALUES
(1, 1, '2025-11-01 12:30:00', 1650.00, 'DELIVERED'),
(2, 2, '2025-11-02 19:15:00', 1349.00, 'DELIVERED'),
(3, 3, '2025-11-03 13:00:00', 1249.00, 'PLACED');

-- Insert sample Order Items
INSERT INTO Order_Items (order_id, menu_item_id, quantity, item_price) VALUES
(1, 2, 1, 1200.00),
(1, 1, 1, 450.00),
(2, 3, 1, 550.00),
(2, 4, 1, 799.00),
(3, 5, 1, 250.00),
(3, 6, 1, 999.00);

SELECT DISTINCT c.id, c.name, c.email, c.phone
FROM Customers c
JOIN Orders o ON o.customer_id = c.id
JOIN Order_Items oi ON oi.order_id = o.id
WHERE oi.item_price > 500
ORDER BY c.id;

SELECT
  c.name AS customer_name,
  c.email,
  r.name AS restaurant_name,
  mi.name AS menu_item,
  oi.item_price,
  oi.quantity,
  (oi.item_price * oi.quantity) AS total_item_cost
FROM Customers c
JOIN Orders o ON o.customer_id = c.id
JOIN Order_Items oi ON oi.order_id = o.id
JOIN Menu_Items mi ON mi.id = oi.menu_item_id
JOIN Restaurants r ON r.id = o.restaurant_id
WHERE oi.item_price > 500
ORDER BY c.name;

