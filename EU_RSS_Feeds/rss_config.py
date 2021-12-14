rss_config = [
	{
	'url': 'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml',
	'output_file_name': 'eu_top_stories',
	'columns' : {
		'article_title': 'title',
		'article_link': 'link',
		'article_content': 'description',
		'article_published': 'pubDate'
		}
	},
	{
	'url': 'https://www.europarl.europa.eu/rss/topic/902/en.xml',
	'output_file_name': 'justice_and_citizenship',
	'columns' : {
		'article_title': 'title',
		'article_link': 'link',
		'article_content': 'description',
		'article_published': 'pubDate'
		}
	},
]