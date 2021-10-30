#!/usr/bin/env python
# coding: utf-8

# In[116]:


#Import splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[117]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[118]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=5)


# In[119]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[120]:


slide_elem.find('div', class_='content_title')


# In[121]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[122]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# #### Featured Images

# In[123]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[124]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[125]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[126]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[127]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[128]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df.to_html()


# In[151]:


browser.quit()


# In[172]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[173]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[176]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=5)


# In[177]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[178]:


slide_elem.find('div', class_='content_title')


# In[179]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[180]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[181]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[182]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[183]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[184]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[185]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[186]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[187]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[188]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[189]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[190]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for hemis in range(4):
    # Browse through each article
    browser.links.find_by_partial_text('Hemisphere')[hemis].click()
    
    # Parse the HTML
    html = browser.html
    hemi_soup = soup(html,'html.parser')
    
    # Scraping
    title = hemi_soup.find('h2', class_='title').text
    img_url = hemi_soup.find('li').a.get('href')
    
    # Store findings into a dictionary and append to list
    hemispheres = {}
    hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
    hemispheres['title'] = title
    hemisphere_image_urls.append(hemispheres)
    
    # Browse back to repeat
    browser.back()


# In[191]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[192]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




