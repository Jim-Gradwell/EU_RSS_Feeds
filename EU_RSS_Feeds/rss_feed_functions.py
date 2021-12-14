from urllib.request import urlopen
import xml.etree.ElementTree as ET
from helper_functions import cleanhtml


def build_data_holder(config):

	data_holder = {}

	for column in config['columns']:
		data_holder[config['columns'][column]] = {
			'output_column_name': column,
			'results_array': []
			}

	return data_holder


def return_channel(config):

	site = urlopen(config['url'])
	html = site.read().decode('utf-8')
	root = ET.fromstring(html)
	channel = root[0]

	return channel


def extract_data(data_holder, channel):
	for item in channel.iter('item'):
		for entry in item:
			if entry.tag in data_holder:
				data_holder[entry.tag]['results_array'].append(cleanhtml(entry.text))

	return data_holder


def build_dataframe_arrays(rss_data):

	dataframe_arrays = {}

	for c in rss_data:
		dataframe_arrays[rss_data[c]['output_column_name']] = rss_data[c]['results_array']

	return dataframe_arrays