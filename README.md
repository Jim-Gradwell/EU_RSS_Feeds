# EU_RSS_Feeds README
 
Introduction
==============
This repository contains a small python module designed to extract data from an RSS Feed and export it to CSV.

There are four python files in the module:
- rss_config.py

This file contains config information about the EU RSS Feeds to be called

- rss_feed_functions.py

Contains functions specific to working with the RSS Feeds

- helper_functions.py

Contains functions not specific to working with the RSS Feeds 

- main.py

Imports config & functions from the other files and runs


rss_config.py
--------------
rss_config.py contains an array of python dictionaries in the format below:

     {
     'url': 'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml',
     'output_file_name': 'eu_top_stories',
     'columns' : {
      'article_title': 'title',
      'article_link': 'link',
      'article_content': 'description',
      'article_published': 'pubDate'
      }
     }
     
- The 'url' key from each dictionary should contain the weburl of the rss feed
- 'output_file_name' should be the desired file name prefix of the .csv file to be output
- The 'columns' key of the dictionary contains another dictionary of column name key values. Each key corresponds to the column header in the csv to be output, and each value corresponds to the XML elemement within the <item> element to be output into the csv file.
 
 The example config above will extract the data from the \<title\> \<link\> \<description\> and \<pubDate\> elements and output them into columns 'article_title', 'article_link', 'article_content' and 'article_published' and output to a csv file called 'eu_top_stories' (from the RSS Feed at url 'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml') from this example XML below.

    <item>
      <title>Top story - Transparent taxation - The fight for a fair and transparent tax system</title>
      <link>https://www.europarl.europa.eu/news/en/headlines/priorities/taxation</link>
      <description>&lt;img src="https://www.europarl.europa.eu/...</description>
      <source url="https://www.europarl.europa.eu/rss/doc/top-stories/en.xml">Top stories - European Parliament</source>
      <category domain="type">Top story</category>
      <pubDate>Tue, 16 Nov 2021 08:43:57 GMT</pubDate>
      <guid isPermaLink="false">TST_TST-2021-11-15-17321_EN</guid>
    </item>
 
 The benefit of using this style of configuation file is that it allows additional RSS Feed config to be supplied and use the same functionality to produce CSV files. For example you could also add this dictionary to the list and it would use the same process to create a "justice_and_citizenship" csv from this Justice & Citizenship RSS Feed.
 
     {
     'url': 'https://www.europarl.europa.eu/rss/topic/902/en.xml',
     'output_file_name': 'justice_and_citizenship',
     'columns' : {
      'article_title': 'title',
      'article_link': 'link',
      'article_content': 'description',
      'article_published': 'pubDate'
      }
     }
 
 
rss_feed_functions.py
--------------
rss_feed_functions.py contains functions specific to working with the https://www.europarl.europa.eu/rss/ rss feeds. There are four:
 
- return_channel | uses default python libraries urllib.request.urlopen & xml.etree.ElementTree to open the URL provided in rss_config.py and navigate to the \<channel\> element of the XML
- build_data_holder | Creates a python dictionary for each column / XML element to be retrieved along with an empty array to hold the data
- extract_data | loops over the columns from rss_config and elements in each \<item\> element and appends data to appropriate element in the data_holder
- build_dataframe_arrays | loops over the data now in data_holder and converts to a dictionary of arrays, suitable for constructing a pandas dataframe from.
 
 
helper_functions.py
--------------
helper_functions.py is designed to hold functions potentially re-usable accross other tasks, and no neccessarily limited to the RSS Feeds from https://www.europarl.europa.eu/rss/. There are two functions here:
 
- remove_html_elements | takes a string input and removes any HTML elements then returns the adjusted string
- generate_timestamp | generates a string timestamp in the format YYYYMMDDHHMMSS, to be used in adding suffixs to file names for example
 
main.py
-------------- 
main.py imports the data from rss_config.py; and the functionality from rss_feed_functions.py and helper_functions.py and for each config dictionary in the rss_config array creates a .csv file in the output_files/ directory; using the pandas library to convert the build_dataframe_arrays response from rss_feed_functions to a dataframe.
 
 
running the module locally
--------------
To run this module locally; first clone the repository on a machine with python version 3.7 or higher installed. and then open a command line window in EU_RSS_Feeds folder and run the command `py -m pip install -r requirements.txt` to install the required libraries.
 
To run the rss feeds you can then run the command `python main.py` from the same directory or double click the `run_rss_feeds.bat` file.
 

Next development steps
--------------
- Implement testing
- Adapt script to handle "duplicate" XML elements within an \<item\> element
 
 
