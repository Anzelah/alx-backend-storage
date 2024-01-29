-- Write a SQL script that lists all bands with Glam rock
-- as their main style, ranked by their longevity
SELECT band_name, DATEDIFF(split, formed) AS lifespan
WHERE style = "Glam rock"
ORDER BY lifespan DESC;
