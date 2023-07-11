SELECT
    visit_num,
    COUNT(*) AS num_rows
FROM ONS_CIS_New
GROUP BY visit_num
ORDER BY visit_num
