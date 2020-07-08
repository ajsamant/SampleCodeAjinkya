DELIMITER //

CREATE PROCEDURE spCheckFruitstock(thisFruit SMALLINT)
BEGIN
SELECT
Fruits.Fruit_Name,
Fruits.inventory,
Units.Unit_Name
FROM
Fruits INNER JOIN Units ON
Fruits.Unit_Id  = Units.Unit_Id
WHERE
Fruits.Fruit_Id = thisFruit;
End //

DELIMITER ;

#RUNNING STORED PROCEDURE
CALL spCheckFruitstock(1);
CALL spCheckFruitstock(2);
