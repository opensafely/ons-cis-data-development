SELECT
    visit_type,
    COUNT(*) AS num_rows
FROM ONS_CIS_New
GROUP BY visit_type
ORDER BY visit_type
