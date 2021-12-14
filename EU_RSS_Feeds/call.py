import pandas as pd
from rss_config import rss_config
from helper_functions import generate_timestamp
import rss_feed_functions as rss


for config in rss_config:

	rss_data_holder = rss.build_data_holder(config)
	channel = rss.return_channel(config)
	rss_data = rss.extract_data(rss_data_holder, channel)
	dataframe_arrays = rss.build_dataframe_arrays(rss_data)

	filename = f"output_files/{config['output_file_name']}_{generate_timestamp()}.csv"

	df = pd.DataFrame(dataframe_arrays)
	df.to_csv(filename, encoding='utf-8', index=False)
