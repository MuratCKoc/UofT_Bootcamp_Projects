/*Combining all uploaded tables into a single table called combined_table*/

CREATE TABLE combined_table AS (
SELECT * FROM aircanada
UNION
SELECT * FROM bell
UNION
SELECT * FROM bombardier
UNION
SELECT * FROM cineplex
UNION
SELECT * FROM great_canadian_gaming
UNION
SELECT * FROM nuvei_corp
UNION
SELECT * FROM recipe_ultd
UNION
SELECT * FROM rogers_canada
UNION
SELECT * FROM shopify)
