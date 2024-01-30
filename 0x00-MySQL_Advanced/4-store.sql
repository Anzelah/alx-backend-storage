-- create a trigger
DELIMITER $$

CREATE TRIGGER my_trigger AFTER
INSERT ON orders FOR EACH ROW
BEGIN
UPDATE items 
SET quantity = quantity - 1
WHERE name = NEW.item_name;
END$$

DELIMITER ;
