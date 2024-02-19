from utils.filters import filter_based_on_avg_views
from utils.filters import filter_based_on_followers_count
from utils.filters import filter_based_on_keyword
from utils.data_import import load_json_data
from multiprocessing import Pool
import os

def get_filtered_data(filters, app):
   filter_function_mapper = {
      'follower_filter':filter_based_on_followers_count,
      'keyword_filter': filter_based_on_keyword,
      'avgview_filter': filter_based_on_avg_views
      }
   filtered_data = load_json_data(os.path.join(app.root_path,'static','user-info.json'))
   for filter_key, filter_criteria in filters.items():
      if(len(filtered_data) != 0):
         filtered_data = parallel_filter(filtered_data, filter_criteria, filter_function_mapper[filter_key])
   return filtered_data


def parallel_filter(data, filter_criteria, filter_function):
  if(len(data) <= 100):
     return filter_function(data, filter_criteria)
  number_of_process = 3
  chunk_size = len(data)//number_of_process
  data_chunks = [data[i:None if i==(3*chunk_size) else i+chunk_size] for i in range(0,len(data),chunk_size)]
  with Pool(processes=number_of_process) as pool:
    results = pool.starmap(filter_function, [(chunk, filter_criteria) for chunk in data_chunks])
  return [json_obj for json_list in results for json_obj in json_list]