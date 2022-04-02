SELECT CONCAT(name,'(',SUBSTR(occupation,1,1),')') AS NAME
FROM OCCUPATIONS
ORDER BY NAME;

SELECT CONCAT('There are a total of',' ',COUNT(occupation),' ',lower(occupation),'s.')
FROM OCCUPATIONS
GROUP BY occupation
ORDER BY COUNT(occupation), occupation;
