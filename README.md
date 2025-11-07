# ShopEasy Marketing Insights -- Project overview 
---
#### ShopEasy is an online retail company that offers a wide range of consumer products through its digital platform. The company is facing **reduced customer engagement and conversion rates** despite launching several new online marketing campaigns. This project aims to analyze the business data via various KPIs and provide actionable insights and recommendations to different stakeholders. 

---
## KPIs
- **Conversion Rate**: Percentage of website visitors who make a purchase.
- **Customer Engagement Rate**: Level of interaction with marketing content (clicks, likes, comments).
- **Customer Feedback Score**: Average rating from customer reviews.
--- 
## Goals for this project
- **Increase Conversion Rates**:
   - **Goal**: Identify factors impacting the conversion rate and provide recommendations to improve it.
   - **Insight**: Highlight key stages where visitors drop off and suggest improvements to optimize the conversion funnel.
- **Enhance Customer Engagement**:
   - **Goal**: Determine which types of content drive the highest engagement. 
   - **Insight**: Analyze interaction levels with different types of marketing content to inform better content strategies.
- **Improve Customer Feedback Scores**:
   - **Goal**: Understand common themes in customer reviews and provide actionable insights.
   - **Insight**: Identify recurring positive and negative feedback to guide product and service improvements.
---
## Data structure 
- The dataset contains _**100 customers, 1,363 customer reviews, 4,623 customer engagement and 4,011 customer journeys over 2023 to 2025**_. 
- The dataset consists of 6 tables: customers, products, customer journey, customer reviews, customer engagement, and customer reviews with sentiment. 
- Calendar and calculations were calculated tables added for the purpose of creating the dashboard.
  

![ERD](https://github.com/eggchoo/ShopEasy-marketing-analysis/blob/main/ERD.png?raw=true)
---
## Executive Overview
This analysis evaluates ShopEasy’s conversion performance, customer engagement, and feedback trends to identify areas for improvement. Findings show strong seasonal conversions but declining engagement and slightly below-target customer ratings. Targeted marketing, refreshed content strategies, and service enhancements are recommended to boost overall performance and customer satisfaction.

**[View the Power BI Interactive Dashboard here](https://app.powerbi.com/links/ZRnbstLhCp?ctid=6f0bb72f-5377-4ddf-936a-b6c72bf21ae2&pbi_source=linkShare&bookmarkGuid=519eae8b-b62d-47ab-b44d-3dfc1c9fd223)**
![Power BI Dashboard](https://github.com/eggchoo/ShopEasy-marketing-analysis/blob/main/bi_overview.png?raw=true)

### Overview
- **Conversion Rates**
  - The conversion rate showed a strong recovery in December, rising to 10.2% after a significant decline to 5.0% in October.
  - This upward trend indicates an effective rebound in customer purchasing behavior toward the end of the year, suggesting that recent marketing or promotional efforts may have contributed to renewed consumer interest and improved conversion performance.
- **Customer Engagement**
  - Overall social media engagement has **declined**, with total views decreasing steadily over the year.
  - Although clicks and likes remain relatively low compared to views, the click-through rate (15.37%) suggests that users who do engage are doing so meaningfully. This suggests that while audience reach has declined, engagement quality among active users remains strong.
- **Customer Reviews**
  - Average customer ratings have **remained relatively stable** at around 3.7 throughout the year.
  - While this consistency is positive, the score remains below the target of 4.0, highlighting the need for targeted actions to **boost satisfaction—particularly for products rated below 3.5**.

## Business insights for each KPI 
### Conversion Rates
![Power BI Dashboard](https://github.com/eggchoo/ShopEasy-marketing-analysis/blob/main/bi_conversion.png?raw=true)
**General Conversion Trends**
- Conversion rates fluctuated throughout the year, with notable peaks observed in **February** and **July**. These trends suggest that certain products experience **strong seasonal demand**, highlighting opportunities to leverage these patterns while **implementing targeted strategies** to improve performance during lower-converting months.

**Lowest Conversion Month**
- The month of **May** and **October** recorded the lowest overall conversion rate at 7.61% and 6.15%, with no specific products demonstrating strong performance. This pattern indicates a potential gap in marketing effectiveness or promotional activity during this period, warranting a review of campaign timing and customer targeting strategies to enhance conversions.

**Highest Conversion Rates**
- In contrast, **January** achieved the highest overall conversion rate of 18.5%, largely driven by the exceptional performance of Ski Boots, which reached a 150% conversion rate. This strong start to the year likely reflects **effective seasonal marketing** and **heightened consumer interest**, providing a valuable benchmark for future campaign planning.

---
### Customer Engagement
![Power BI Dashboard](https://github.com/eggchoo/ShopEasy-marketing-analysis/blob/main/bi_engagement.png?raw=true)
**Declining Views**
- Audience views reached their highest levels in February and July, followed by a noticeable decline from August onward. This downward trend suggests a **reduction in audience engagement during the latter half of the year**, potentially due to decreased campaign activity or content fatigue.
  
**Low Interaction Rates**
- Despite steady visibility, clicks and likes remained consistently low relative to total views. This indicates **a need to enhance content appeal through more engaging formats, clearer messaging, or stronger calls** to action to better **convert passive viewers into active participants**.

**Content Type Performance**
- Among all content types, **blog posts generated the highest viewership**, particularly in April and July, demonstrating their effectiveness in attracting audience interest. Meanwhile, social media and video content maintained moderate but stable engagement levels, suggesting consistent performance with room for optimization in reach and interaction.
--- 

### Customer Reviews 
![Power BI Dashboard](https://github.com/eggchoo/ShopEasy-marketing-analysis/blob/main/bi_customer%20review.png?raw=true)
**Customer Ratings Distribution**  
- The majority of customer feedback is positive, with **140 reviews rated 4 stars** and **135 reviews rated 5 stars**, reflecting a generally favorable perception of ShopEasy’s products and services. In contrast, lower ratings—**26 reviews at 1 star** and **57 reviews at 2 stars**—represent a smaller portion of the overall review distribution, indicating that negative experiences are relatively limited.  

**Sentiment Analysis**  
- Overall customer sentiment is predominantly positive, with **275 reviews** expressing satisfaction. **Negative sentiment**, recorded in **82 reviews**, remains modest, while a smaller proportion of **mixed or neutral sentiments** suggests some areas that could benefit from targeted improvement. These results indicate that the majority of customers hold a favorable view of their shopping experience.  

**Opportunities for Improvement**  
- The presence of **mixed positive and mixed negative sentiments** highlights opportunities to strengthen customer satisfaction further. By addressing the specific issues mentioned in these reviews—such as product quality, delivery experience, or customer support; ShopEasy can potentially transform moderately satisfied customers into highly satisfied ones, thereby improving overall ratings and customer loyalty.  
--- 
## **Stakeholder Breakdown of Recommended Actions**

#### **1. Increase Conversion Rates** 
- **Marketing Team** – Lead targeted campaigns for high-performing product categories (e.g., **Kayaks**, **Ski Boots**, **Baseball Gloves**). Plan and execute **seasonal promotions** and personalized advertisements during peak months such as **January** and **September**.  
- **Product Management Team** – Coordinate with marketing to ensure **inventory alignment** and adequate stock levels for high-demand products during promotional periods.  
- **Data Analytics / Business Intelligence Team** – Monitor conversion metrics and evaluate the **effectiveness of targeted campaigns**, providing ongoing data insights to guide adjustments.  

---

#### **2. Enhance Customer Engagement** 
- **Content & Social Media Team** – Revise and diversify the **content strategy** by incorporating **interactive videos**, **user-generated content**, and improved **call-to-action (CTA)** placements in social media and blog posts.  
- **UX / Web Design Team** – Optimize **content layout and CTA visibility** across digital platforms to encourage deeper engagement. Ensure consistent design and accessibility during low-engagement months (**September–December**).  
- **Marketing Team** – Support content initiatives through **paid promotions** and **A/B testing** to determine which formats and CTAs drive the highest engagement.  

---

#### **3. Improve Customer Feedback Scores**
- **Customer Service / Support Team** – Establish a **feedback loop** to actively address issues raised in mixed or negative reviews. Follow up with dissatisfied customers to resolve concerns and potentially encourage re-ratings.  
- **Product Management Team** – Use insights from review analysis to **prioritize product improvements**, focusing on recurring issues affecting quality or performance.  
- **Data Analytics Team** – Conduct **sentiment analysis** to identify common themes in feedback and measure progress toward the **4.0 rating target** over time.  
- **Senior Management** – Oversee and support **cross-department collaboration** to ensure that customer satisfaction initiatives are adequately resourced and strategically aligned.  

