-- Numbered by score

SELECT score, COUNT(*) 'number' from second_table
GROUP BY score
ORDER BY score DESC;