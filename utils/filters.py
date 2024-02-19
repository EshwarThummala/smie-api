import json

def filter_based_on_followers_count(json_data, given_followers_count):
  minimum_followers, maximum_followers = given_followers_count
  filter = 'tiktok_followers'
  filtered_data = []
  for json_object in json_data:
    follower_count = json_object['user_profile'].get(filter)
    if (follower_count != None and minimum_followers <= follower_count <= maximum_followers):
      filtered_data.append(json_object)
  return filtered_data

def filter_based_on_keyword(json_data, keyword):
  keyword = keyword.lower()
  filter='tiktok_bio'
  filtered_data = []
  for json_object in json_data:
    bio = (json_object['user_profile'].get(filter)).lower()
    if (bio != None and keyword in bio):
      filtered_data.append(json_object)
  return filtered_data

def filter_based_on_avg_views(json_data, given_avg_views):
  filtered_data = []
  for json_obj in json_data:
    avg_views = 0
    number_of_posts = 0
    for post in json_obj['posts_info']:
      if(post.get('views')):
        avg_views += post['views']
        number_of_posts += 1
    if(number_of_posts != 0):
      avg_views /= number_of_posts
    if(avg_views >= given_avg_views):
      filtered_data.append(json_obj)
  return filtered_data