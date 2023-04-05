-- The id must be unique

CREATE TABLE IF NOT EXISTS unique_id (
    id int DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);