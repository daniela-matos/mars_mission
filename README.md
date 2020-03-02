# Mars Facts Web Scraping

In this project I used Jupyter Lab to do web scraping 

Using a jupyter notebook, initial web scraping is performed using the Python library Beautiful Soup. All the code for web scraping is copied into a python file to create a function to perform all the scraping at once. Using Pymongo in the function, the data is stored in a MongoDB database. This function is called into the app.py file. The app.py file is a flask app that is a single page app that allows the user to view all the scraped data. Once the app is opened, the user can view a Mars fact from NASA's twitter page, the weather on Mars, the featured Mars image on NASA's website, and images of every one of Mars' Hemispheres.

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




