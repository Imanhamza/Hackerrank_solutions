/*
Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:
FOUNDER -> Lead Manager -> Senior Manager -> Manager -> Employee
Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

Note:
The tables may contain duplicate records.
The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.
Input Format

The following tables contain company data:
Company: The company_code is the code of the company and founder is the founder of the company.
Lead_Manager: The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company.
Senior_Manager: The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.
Senior_Manager: The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.

*/
SELECT
c.company_code ,c.founder, COUNT(DISTINCT lm.lead_manager_code), COUNT(DISTINCT sm.senior_manager_code), COUNT(DISTINCT m.manager_code), COUNT(DISTINCT e.employee_code)
FROM Company c, Lead_Manager lm, Senior_Manager sm, Manager m, Employee e
WHERE
    c.company_code = lm.company_code
    AND 
    lm.lead_manager_code = sm.lead_manager_code
    AND
    sm.senior_manager_code = m.senior_manager_code
    AND 
    m.manager_code = e.manager_code
GROUP BY c.company_code, c.founder