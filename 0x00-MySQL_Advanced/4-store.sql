-- create a trigger
CREATE TRIGGER my_trigger AFTER
INSERT ON orders FOR EACH ROW
BEGIN
UPDATE items 
SET quantity = quantity - NEW.quantity
WHERE items.number = NEW.number;
END$$
