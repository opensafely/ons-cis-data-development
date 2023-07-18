SELECT
    visit_status,
    COUNT(*) AS num_rows
FROM ONS_CIS_New
GROUP BY visit_status
ORDER BY visit_status
