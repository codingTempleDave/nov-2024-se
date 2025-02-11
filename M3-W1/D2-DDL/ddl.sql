-- DDL (data definition language)

CREATE DATABASE starwarsdb;
USE starwarsdb;

-- Jedi Table
CREATE TABLE jedi (
	jedi_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    lightsaber_color VARCHAR(20),
    jedi_rank VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Padawans Table (One-to-Many Relationship)
CREATE TABLE padawans (
    padawan_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    training_start_date DATE,
    jedi_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (jedi_id) REFERENCES jedi(jedi_id)
		ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Missions table
CREATE TABLE missions (
    mission_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100) NOT NULL,
    assigned_date DATE,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Jedi_Missions Table (Many to many)
CREATE TABLE jedi_missions (
	jedi_id INT,
    mission_id INT,
    PRIMARY KEY (jedi_id, mission_id),
    FOREIGN KEY (jedi_id) REFERENCES jedi(jedi_id)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	FOREIGN KEY (mission_id) REFERENCES missions(mission_id)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Add a new column to track Jedi's species
ALTER TABLE jedi ADD species VARCHAR(50);

-- Change the data type of lightsaber_color to CHAR(15)
ALTER TABLE jedi MODIFY COLUMN lightsaber_color CHAR(15);

-- Rename the column rank to jedi_force_rank for clarity
ALTER TABLE jedi CHANGE COLUMN jedi_rank jedi_force_rank VARCHAR(50);

-- Rename the missions table to tasks
RENAME TABLE missions TO mission;
RENAME TABLE mission TO missions;

-- Drop the species column from the jedi table
ALTER TABLE jedi DROP COLUMN species;

-- Add a foreign key to link padawans to missions
ALTER TABLE padawans ADD COLUMN mission_id INT,
    ADD CONSTRAINT fk_padawan_mission FOREIGN KEY (mission_id) REFERENCES missions(mission_id)
		ON DELETE SET NULL 
		ON UPDATE CASCADE;


