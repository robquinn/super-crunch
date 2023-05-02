SELECT
DISTINCT
outside_brokerage_agent
FROM `super-crunch-384118.transactions.closed`
WHERE
outside_brokerage_agent LIKE "%NA"
OR
outside_brokerage_agent LIKE "%None%"
OR
outside_brokerage_agent LIKE "-"
OR
outside_brokerage_agent IS NULL
