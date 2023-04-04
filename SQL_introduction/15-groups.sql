-- Numbered by score

SELECT score, COUNT(*) 'number' FROM second_table
GROUP BY score
ORDER BY score DESC;