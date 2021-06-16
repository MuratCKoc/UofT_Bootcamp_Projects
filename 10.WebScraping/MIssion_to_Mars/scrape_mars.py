# Dependencies
from splinter import Browser
from time import sleep
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import pymongo
import pandas as pd
from config import username, password


def scrape_data():

    ###---NASA MARS NEWS---###
    # Setup chromedriver path and driver for splinter
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Nasa Stories URL
    news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(news_url)
    sleep(2)

    # Setup Parser
    html = browser.html
    soup = bs(html, 'lxml')
    pprint(soup.prettify())

    browser.quit()
    # Setup up base url and attributes
    news_base_url = 'https://mars.nasa.gov'
    list_text = soup.find_all('div', class_='list_text')
    news_list = []
    news_dict = {}

    # Go thru latest 40 news about mars
    for i in range(4):
        news_title = list_text[i].a.text
        news_href = news_base_url + list_text[i].a['href']
        news_date = list_text[i].div.text
        news_paragraph = list_text[i].contents[2].text
        news_dict = {'news_date': news_date,
                     'news_title': news_title,
                     'news_href': news_href,
                     'news_paragraph': news_paragraph}
        news_list.append(news_dict)
    pprint(news_list)

    ###---JPL Mars Space Images - Featured Image---###

    # Visit the url for JPL Featured Space Image
    # browser = Browser('chrome', **executable_path, headless=False)
    # murl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # # Use splinter to navigate the site
    # # Visit first link
    # browser.visit(murl)
    # sleep(2)

    # # Click Full Image button
    # browser.click_link_by_id('full_image')
    # sleep(2)

    # # Full Image -> more info
    # browser.click_link_by_partial_text('more info')
    # sleep(2)

    # # Parse html
    # html = browser.html
    # soup = bs(html, 'lxml')
    # browser.quit()

    # # Define base url and dictionary to store featured img
    # fImage_base_url = 'https://www.jpl.nasa.gov/images'
    # featured_img_dict = {}
    # # Find the image url
    # fImage_url = soup.find('figure', class_='lede').a['href']
    # # Append it to the base url
    # featured_image_url = fImage_base_url + fImage_url
    # # Find the image title
    # fImage_title = soup.find('h1', class_='article_title').text.strip()
    # featured_image_dict = {'image_url': featured_image_url,
    #                        'title': fImage_title}
    featured_image_dict=scrape_featured_img()


    ###---Mars Facts---###
    #Visit the Mars Facts webpage here and use
    mars_url = 'https://space-facts.com/mars/'

    #Pandas to scrape the table containing facts about the planet

    # tables = pd.read_html(mars_url)
    # mars_df = tables[0]
    # mars_df.columns = ['Property', 'Value']
    # mars_df.set_index('Property', inplace=True)
    # return mars_df.html()

    #Depricated
    # tables = pd.read_html(mars_url)
    # mars_df = tables[1]
    # mars_df.columns = ['Mars - Earth Comparison', 'Mars', 'Earth']
    # mars_html_table = mars_df.to_html(header=None, index=False)
    # mars_html_table = mars_html_table.replace('\n', '')


    ###---Scrape image sources and titles---###
    # Click on each of the links to get full image url
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(hemispheres_url)
    soup = bs(response.text, 'lxml')

    # Set root url
    root_url = 'https://astrogeology.usgs.gov'

    hemisphere_list = []
    hemisphere_dict = {}

    # Get number of hemisphere links available
    url = soup.find_all('a', class_='itemLink product-item')

    for links in range(len(url)):
    # Go to the next link at the root url
        url_gen = root_url + url[links]['href']

        # Get response
        response = requests.get(url_gen)

        # Parse
        soup = bs(response.text, 'lxml')

        # Get the image source
        img_src = soup.find('img', class_='wide-image')['src']

        # Get image title
        img_title = soup.find_all('h2', class_='title')[0].text.strip()

        # Concat the url and add into dict
        hemisphere_dict = {'img_title': img_title,
                           'img_url': root_url + img_src}

        hemisphere_list.append(hemisphere_dict)

    print(hemisphere_list)

    mars_data = {"news":news_list, 
    "fimage":featured_image_dict,
    "hemisphere":hemisphere_list,
    "facts":scrape_facts()}


    
    # Push to MongoDB
    # Create Connection to MongoDB
    client = pymongo.MongoClient("mongodb+srv://"+username+":"+password +
                        "@cluster0.ow6cz.mongodb.net/mars_db?retryWrites=true&w=majority")

#   # Create database
    mydb = client["mars_db"]

    # Double check if collection exists, drop if so
    try:
        mydb.drop_collection('marsArticles')
        mydb.drop_collection('featuredImage')
        mydb.drop_collection('marsFacts')
        mydb.drop_collection('marsHemispheres')
    except:
        pass

    ## Create Collections
    marsArticles = mydb['marsArticles']
    featuredImg = mydb['featuredImage']
    marsFacts = mydb['marsFacts']
    marsHemi = mydb['marsHemispheres']

    # Insert Dictionaries into corresponding Collections
    marsArticles.insert(news_list)
    featuredImg.insert(featured_image_dict)
    marsFacts.insert(mars_data['facts'])
    marsHemi.insert(hemisphere_dict)

    return mars_data


def scrape_featured_img():
    # Featured image:
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path)
    featured_image_dict = {}

    try:
        #Visit base page
        base_image_url = 'https://www.jpl.nasa.gov/images'
        browser.visit(base_image_url)
        sleep(2)

        # Check Mars from filters
        browser.is_element_present_by_id('filter_Mars')
        browser.find_by_id('filter_Mars').first.click()
        sleep(2)

        # Click the first link
        browser.click_link_by_partial_href('/images')
        sleep(2)

        # Get title
        featured_title = browser.find_by_tag('h1').first.value
        print(featured_title)

        # Get url
        featured_image_url = browser.url
        featured_image_dict = {
            "title": featured_title, "image_url": featured_image_url}
        print(featured_image_dict)
    finally:
        browser.quit()

    # Return the dictionary
    return featured_image_dict


def scrape_facts():

    # Set the exec path and init the chrome browser
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path)
    try:
        #Visit the Nasa mars news site
        mars_url = 'https://space-facts.com/mars/'
        sleep(2)
        mars_df = pd.read_html(mars_url)[1]
        mars_df = mars_df[0]

        mars_df.columns = ['Comparison', 'Mars', 'Earth']
        mars_df.set_index('Comparison', inplace=True)
        mars_html_table = mars_df.to_html(header=None, index=False)
        
    finally:
        browser.quit()
    return mars_df
