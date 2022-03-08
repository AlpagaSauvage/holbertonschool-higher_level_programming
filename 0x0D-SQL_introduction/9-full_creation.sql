-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table(id, name, score)
VALUEs ('1', 'John', '10');

INSERT INTO second_table(id, name, score)
VALUEs ('2', 'Alex', '3');

INSERT INTO second_table(id, name, score)
VALUEs ('3', 'Bob', '14');

INSERT INTO second_table(id, name, score)
VALUEs ('4', 'George', '8');
