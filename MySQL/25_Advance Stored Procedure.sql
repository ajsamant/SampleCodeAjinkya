DROP PROCEDURE IF EXISTS spCheckFruitstockLevel;

DELIMITER //

CREATE PROCEDURE spCheckFruitstockLevel(IN pFruit_Id SMALLINT(5), OUT pStockLevel VARCHAR(6))
BEGIN
	DECLARE stockNumber SMALLINT;

	SELECT
		Fruits.Inventory into stockNumber
	FROM
		Fruits INNER JOIN Units ON
		Fruits.Unit_Id = Units.Unit_Id
	WHERE
		Fruits.Fruit_Id = pFruit_Id;
        
	IF stockNumber > 10 THEN
		SET pStockLevel = 'High';
	ELSEIF ( stockNumber <= 10 AND stockNumber >= 5) THEN
		SET pStockLevel = 'Medium';
	ELSEIF ( stockNumber < 5) THEN
		SET pStockLevel = 'Low - Please Replace Now!';
	END IF; 

End //

DELIMITER ;

#TEST STORED PROCEDURE
CALL spCheckFruitstockLevel(1, @stockLevel);
select @stockLevel;

# Drop Procedure
DROP PROCEDURE spCheckFruitstockLevel;