-- create users for our table
ALTER TABLE users ADD (
	country ENUM('US', 'CO', 'TN') NOT NULL
);
