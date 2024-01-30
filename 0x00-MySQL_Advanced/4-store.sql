-- create a trigger
CREATE TRIGGER my_trigger AFTER
INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - ?
WHERE ? = orders.number;
