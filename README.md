# Mars Facts Web Application

In this project I used Jupyter Lab to do all the code for web scraping. Then I converted the notebook into a Python script, and added a function that returns one Python dictionary with all the scraping. 
After that, I stored the Python dictionary in MongoDB and created a HTML template to display all the data.
The app.py file is a flask application that is a single page app that allows the user to view all the scraped data. Once the app is opened, the user can click a button and view the current weather in Mars, the latest Mars News from NASA's twitter page, the featured Mars image, a table with Mars facts and images of Mars' Hemispheres.

#### 1 - Scraping various websites:

 * Python:
      * requests.get(), 
      * Beautiful Soup, 
      * Pandas (pd.read_html) 
      
  * Selenium WebDriver 
      * chromedriver,
      * geckodriver
      
 #### 2 - Storing the scraped data: 
 
  * Python:
      * Pymongo
      
  * MongoDB (non-relational database)
  
 #### 3 - App
 
  * Flask Application
  * HTML
  * Bootstrap

![Page](Images/1_web_scrape_mar_02.png)

![Page](Images/2_Web_scrape_mar_02.png)

![Page](Images/3_Web_scrape_mar_02.png)

