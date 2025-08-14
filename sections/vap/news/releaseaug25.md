---
author: Veracity
description: This is the changelog for the release 4.25 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.25 release
Read this page to learn what has changed in the Veracity Adapter for Power BI. 

## New Features

This section covers new features.

### Color-coded Refresh Time Chart  
We've introduced a **color-coded chart** to help you plan report refreshes during optimal times.  
- **Green** = Non-peak hours (best choice)  
- **Red** = Peak hours (avoid to reduce delays)  

This chart helps you schedule refreshes during non-peak hours (such as nighttime) to reduce delays and improve performance.

#### Where to find it  
On the **Resources** page, open **Refresh Schedule Plans** and either add or edit a plan.  

You can now:
- **Preview refresh times** while setting a schedule.
- Click **Check Refresh Time Chart** to visualize peak vs. non-peak hours.  

<figure>
	<img src="../admin-tab/assets/refresh-time-chart.png"/>
</figure>

### Optimize performance with refresh scheduling  
The color-coded chart helps you avoid delays caused by peak usage times:  
- **Green hours**: Schedule refreshes here whenever possible for smoother performance.  
- **Red hours**: These are peak times. Avoid scheduling refreshes during these periods to prevent delays.  

By scheduling refreshes during off-peak (green) times, you reduce the risk of delays and help maintain performance for everyone using the service.

### Daylight Saving Time reminder  
Refresh schedules **do not adjust automatically for daylight saving time changes**.  
Please review and update your schedules manually when DST starts or ends.

## Learn more  
See the updated [Resources documentation](../admin-tab/resource.md) to learn more about scheduling report refreshes.