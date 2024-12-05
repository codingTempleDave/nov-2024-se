-- DML (Data Manipulation Language)
-- CRUD (Create, Read, Update, Delete)

INSERT INTO jedi (name, lightsaber_color, jedi_rank) VALUES
	('Yoda', 'Green', 'Grand Master'),
    ('Obi-Wan Kenobi', 'Blue', 'Master'),
	('Mace Windu', 'Purple', 'High Council Member'),
	('Qui-Gon Jinn', 'Green', 'Master'),
	('Luke Skywalker', 'Green', 'Knight');

-- Insert Padawans
INSERT INTO padawans (name, training_start_date, jedi_id) VALUES
	('Anakin Skywalker', '2022-01-01', 2),
	('Ahsoka Tano', '2022-02-01', 2),
	('Obi-Wan Kenobi (Padawan)', '2020-05-01', 4),
	('Baby Yoda', '2023-01-10', 1),
	('Leia Organa', '2023-04-01', 5);
    
-- Insert Missions
INSERT INTO missions (location, assigned_date, completed) VALUES
	('Tatooine', '2023-05-01', FALSE),
	('Coruscant', '2023-06-10', TRUE),
	('Dagobah', '2023-07-15', FALSE),
	('Hoth', '2023-08-20', TRUE),
	('Endor', '2023-09-25', FALSE);
    
INSERT INTO jedi_missions (jedi_id, mission_id) VALUES
	(1, 1), (1, 3),
	(2, 2), (2, 4),
	(3, 3), (3, 5),
	(4, 1), (5, 5);
    
UPDATE jedi 
SET lightsaber_color = "Blue"
WHERE jedi_id = 5; -- LUKE

-- Mark a mission as completed
UPDATE missions 
SET completed = TRUE 
WHERE mission_id = 1;

-- Delete a specific Jedi **make sure to always have a WHERE condition **
DELETE FROM padawans
WHERE padawan_id = 3; -- Obi-Wan Padawan

-- DQL (Data Query Language)
SELECT * FROM jedi;

SELECT * FROM jedi
WHERE jedi_id = 2;

-- BONUS yay!
SELECT * FROM missions 
WHERE mission_id IN (
    SELECT mission_id FROM jedi_missions WHERE jedi_id = 1
);

-- List Jedi ordered by name alphabetically
SELECT * FROM jedi 
ORDER BY name;

-- List Padawans ordered by training start date
SELECT * FROM padawans 
ORDER BY training_start_date DESC;


-- Find Jedi with a name containing 'Ken'
SELECT * FROM jedi 
WHERE name LIKE '%Ken%';

-- Find missions at locations starting with 'T'
SELECT * FROM missions 
WHERE location LIKE 'T%';

-- Find padawans that start with anything followed by 'aby' and followed by anything
SELECT * FROM padawans 
WHERE name LIKE '_aby%';

-- List all Jedi with their Padawans
SELECT j.name AS Jedi, p.name AS Padawan
FROM jedi j -- jedi is the left table
LEFT JOIN padawans p ON j.jedi_id = p.jedi_id; -- padawans is right table

-- List all Jedi and their assigned missions
SELECT j.name AS Jedi, m.location AS Mission
FROM jedi j
JOIN jedi_missions jm ON j.jedi_id = jm.jedi_id
JOIN missions m ON jm.mission_id = m.mission_id;


-- Count the number of Padawans per Jedi BONUS
SELECT j.name AS Jedi, COUNT(p.padawan_id) AS PadawanCount
FROM jedi j
LEFT JOIN padawans p ON j.jedi_id = p.jedi_id
GROUP BY j.name;


