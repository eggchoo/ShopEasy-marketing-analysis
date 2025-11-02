SELECT*
FROM customer_journey;

-- identify duplicate combinations 
WITH DuplicateRecords AS (
   SELECT
       JourneyID,
       CustomerID,
       ProductID,
       VisitDate,
       Stage,
       Action,
       Duration,
       ROW_NUMBER()OVER(
          PARTITION BY CustomerID,ProductID,VisitDate,Stage,Action
          ORDER BY JourneyID) 
          AS row_num
     FROM dbo.customer_journey
     )
SELECT * 
FROM DuplicateRecords 
WHERE row_num >1 --filter out the first appearance of unique combinations and only keep the duplicates here 
ORDER BY JourneyID; 

SELECT 
       JourneyID,
       CustomerID,
       ProductID,
       VisitDate,
       Stage, 
       Action,
       COALESCE(Duration, avg_duration) AS Duration -- fill missing values in duration with avg_duration for that visitdate 
FROM 
    (SELECT 
       JourneyID,
       CustomerID,
       ProductID,
       VisitDate,
       UPPER(Stage)AS Stage,
       Action,
       Duration,
       AVG(Duration) OVER(PARTITION BY VisitDate) AS avg_duration,
       ROW_NUMBER()OVER(
          PARTITION BY CustomerID,ProductID,VisitDate, UPPER(Stage),Action
          ORDER BY VisitDate) 
          AS row_num
     FROM dbo.customer_journey) AS sub
 WHERE row_num =1;  --dropping duplicates by only keeping the first occurance of the combination 

