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
