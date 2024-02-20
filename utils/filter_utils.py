from utils.filters import filter_based_on_avg_views
from utils.filters import filter_based_on_followers_count
from utils.filters import filter_based_on_keyword
from utils.filters import filter_based_on_id_available
from utils.filters import filter_based_on_username
from utils.data_import import load_json_data
from multiprocessing import Pool
import os

def get_filtered_data(filters, app):
   filter_function_mapper = {
      'follower_filter':filter_based_on_followers_count,
      'keyword_filter': filter_based_on_keyword,
      'avgview_filter': filter_based_on_avg_views,
      'socialid_filter': filter_based_on_id_available,
      'username_filter' : filter_based_on_username

      }
   user_data = load_json_data(os.path.join(app.root_path,'static','user-info.json'))
   return parallel_filter(user_data, filters, filter_function_mapper)


def parallel_filter(data, filters, filter_function_mapper):
  if(len(data) <= 100):
     return apply_filters(data, filters, filter_function_mapper)
  number_of_process = 3
  chunk_size = len(data)//number_of_process
  data_chunks = [data[i:None if i==(3*chunk_size) else i+chunk_size] for i in range(0,len(data),chunk_size)]
  with Pool(processes=number_of_process) as pool:
    results = pool.starmap(apply_filters, [(chunk, filters, filter_function_mapper) for chunk in data_chunks])
  return [json_obj for json_list in results for json_obj in json_list]

def apply_filters(json_data, filters, filter_function_mapper):
   current_filters = filters.keys()
   filtered_data = []
   for json_object in json_data:
      passed_filter = True
      for filter in current_filters:
         if(not filter_function_mapper[filter](json_object, filters[filter])):
            passed_filter = False
      if(passed_filter):
         filtered_data.append(json_object)
   return filtered_data


