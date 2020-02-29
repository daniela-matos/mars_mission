# get_ipython().run_line_magic('load_ext', 'lab_black')
import os
from bs4 import BeautifulSoup as bs
import requests
import time

from splinter import browser
from selenium import webdriver
from selenium.webdriver.common.by import By

import urllib.parse
import pandas as pd
import pprint


def scrape():
    # Since requests.get wasn't bringing the latest news, I used selenium.
    url = "https://mars.nasa.gov/news/"
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source

    # The driver opened the page and the soup brought the latest news title
    soup = bs(html, "html.parser")
    news_title = (soup.find("div", class_="list_text")).find("a").text
    # print(f"News Title: {news_title}")

    # Close the driver
    driver.close()

    # Find the news url
    teaser_url = (
        "https://mars.nasa.gov/news/" + soup.find("div", class_="list_text").a["href"]
    )

    # Soup brought the teaser
    r = requests.get(teaser_url)
    html = r.text
    soup = bs(html, "html.parser")
    teaser = (soup.find("div", class_="wysiwyg_content")).find("p").text

    # print(f"Teaser: {teaser}")

    # Connect to a url to grab NASA's featured Mars image

    # Use selenium to navegate to the page with the image
    driver = webdriver.Firefox()
    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    driver.get(url_image)
    time.sleep(1)

    elem = driver.find_element_by_id("full_image")
    elem.click()
    time.sleep(1)

    # Navigate to "more info" web site, where the full image URL is
    elem = driver.find_element_by_link_text("more info")
    elem.click()
    time.sleep(1)

    # Get the "more info" page URL to parse and find the image in full resolution
    url_more_info = driver.current_url

    # Use requests and soup to return the image url
    r = requests.get(url_more_info)
    html = r.text
    soup = bs(html, "html.parser")
    featured_image_url = (
        "https://www.jpl.nasa.gov" + soup.find("figure", class_="lede").a["href"]
    )
    # print(featured_image_url)

    # Close the driver
    driver.close()

    # Scrape the latest Mars weather tweet from the page.
    # Save the tweet text for the weather report as a variable called `mars_weather`.

    url_twitter = "https://twitter.com/marswxreport?lang=en"

    # Create a Beautiful Soup object
    r = requests.get(url_twitter)
    html = r.text
    soup = bs(html, "html.parser")
    mars_weather = soup.find_all("div", class_="js-tweet-text-container")

    # find the first actual weather tweet
    mars_weather = mars_weather[0].text

    # print(f"The weather today in Mars is: {mars_weather}")

    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Use Pandas to convert the data to a HTML table string.

    url_facts = "http://space-facts.com/mars/"
    mars_facts = pd.read_html(url_facts)

    # Turn the table into a Dataframe
    mars_facts_df = mars_facts[0]
    mars_facts_df.columns = ["Description", "Value"]
    mars_facts_df.set_index("Description", inplace=True)

    # Store the table as html
    mars_facts_html = mars_facts_df.to_html(justify="left")

    # print(mars_facts_df)
    # print(mars_facts_html)

    # ### Mars Hemispheres

    # Obtain high resolution images for each of Mar's hemispheres.
    # Save both the image url string for the full resolution hemisphere image.
    # and the Hemisphere title containing the hemisphere name.
    # Use a Python dictionary to store the data using the keys `img_url` and `title`.
    # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    # set url and the driver

    driver = webdriver.Chrome()
    url_hem = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    driver.get(url_hem)
    html = driver.page_source

    time.sleep(5)

    # scrape page into Soup to get the hemispheres names

    soup = bs(html, "html.parser")
    hemisphere_dict = []

    hemispheres = [name.text[:-19] for name in soup.find_all("h3")]

    # Loop through the click to get each image in high resolution
    for hemisphere in hemispheres:
        driver.find_element_by_partial_link_text(hemisphere).click()
        html = driver.page_source
        soup = bs(html, "html.parser")
        name = (soup.find("h2", class_="title")).text
        img_url = soup.find("div", class_="content").a["href"]
        hemisphere_dict.append({"Title": name, "Img_url": img_url})
        time.sleep(2)
        driver.back()

    #pprint.pprint(hemisphere_dict)

    # Close the browser
    driver.close()

    # create dict of all mars info

    # Store all the scrapped data in a dictionary
    mars_data = {
        "news": news_title,
        "teaser": teaser,
        "image_url": featured_image_url,
        "weather": mars_weather,
        "facts": mars_facts_html,
        "hemispheres": hemisphere_dict,
    }

    # Return the scrapped data dictionary
    return mars_data

