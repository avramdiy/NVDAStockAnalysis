# TRG Week 21 Project

## Nvidia Stock Analysis

- Link To Master Dataset : https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

- Root File : nvda.us.txt

### 1st Commit

- Initiated proper code to convert .txt into .csv, then loaded to HTML for cleaning.

### 2nd Commit

- Filter data to show all information for the year of 2000 and for the year of 2010.

- Remove the "OpenInt" column

### 3rd Commit

- Rename Dataset Table to "2010", not "2020"

- Create a separate route and plot that shows the aggregate monthly open price for the year of 2000. We will use the months as the X axis, and the prices as the Y axis.

- Add another line plotting the aggregate monthly close price for the year of 2000.

### 4th Commit

- Create two line plots on the same route, showing the color-coded lines for the aggregate monthly open and closing prices of 2010.

- I can see there is a common historical support or resistance level around the ten dollar amount.

### 5th Commit

- I want to add color-coded lines showing the aggregate monthly High and Low prices for 2000 and 2010 on the same plot.

- By adding the aggregate monthly High and Low prices for both years, we can see a range in which the price moved monthly. However, the color-coding is messy.

- Let's make the 2000 Open & Close lines solid blue. Make 2000 High and Low lines dashed blue of the same shade.

- Make the 2010 Open & Close lines solid green. Make the 2010 High and Low lines dashed green of the same shade.

- Now the range of price movement is visible to those who have not worked with the data in depth.