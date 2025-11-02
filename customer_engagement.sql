SELECT*
FROM engagement_data

-- clean and normalize engagement data table 
SELECT 
EngagementID,
ContentID,
UPPER(REPLACE(ContentType,'Socialmedia','Social media')) AS ContentType,
Likes,
FORMAT(CONVERT(Date,EngagementDate),'dd.MM.yyyy')AS EngagementDate,
CampaignID,
ProductID,
LEFT(ViewsClicksCombined, CHARINDEX('-', ViewsClicksCombined) -1) AS Views,
RIGHT(ViewsClicksCombined, LEN(ViewsClicksCombined) - CHARINDEX('-', ViewsClicksCombined) )AS Clicks
FROM engagement_data
