from urllib.request import urlopen
import xml.etree.ElementTree as ET
from helper_functions import remove_html_elements


def return_channel(config):

	site = urlopen(config['url'])
	html = site.read().decode('utf-8')
	root = ET.fromstring(html)
	channel = root[0]

	return channel


def build_data_holder(config):

	data_holder = {}

	for column in config['columns']:
		data_holder[config['columns'][column]] = {
			'output_column_name': column,
			'results_array': []
			}

	return data_holder


def extract_data(data_holder, channel):

	rss_data = data_holder

	for item in channel.iter('item'):
		for entry in item:
			if entry.tag in rss_data:
				rss_data[entry.tag]['results_array'].append(remove_html_elements(entry.text))

	return rss_data


def build_dataframe_arrays(rss_data):

	dataframe_arrays = {}

	for column in rss_data:
		dataframe_arrays[rss_data[column]['output_column_name']] = rss_data[column]['results_array']

	return dataframe_arrays