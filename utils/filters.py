import re

def filter_based_on_followers_count(json_object, given_followers_count):
  minimum_followers, maximum_followers = given_followers_count
  follower_count = json_object['user_profile'].get('tiktok_followers')
  if (follower_count != None and int(minimum_followers) <= follower_count <= int(maximum_followers)):
      return True
  return False

def filter_based_on_keyword(json_object, keyword):
  keyword = keyword.lower()
  bio = (json_object['user_profile'].get('tiktok_bio')).lower()
  if (bio != None and keyword in bio):
    return True
  return False

def filter_based_on_avg_views(json_object, given_avg_views):
  avg_views = 0
  number_of_posts = 0
  for post in json_object.get('posts_info',[]):
    if(post.get('views')):
      avg_views += post['views']
      number_of_posts += 1
  if(number_of_posts != 0):
    avg_views /= number_of_posts
  if(avg_views >= int(given_avg_views)):
    return True
  return False

def filter_based_on_id_available(json_object, given_social_ids):
  social_media_ids = json_object.get('social_media')
  if(social_media_ids):
    for given_social_id in given_social_ids:
      if(not social_media_ids.get(given_social_id)):
        return False
      elif(social_media_ids.get(given_social_id) == ''):
        return False
  else:
    return False
  return True

def filter_based_on_username(json_object, given_approximate_username):
  user_profile = json_object.get('user_profile')
  pattern = re.compile('.*('+given_approximate_username+').*', re.IGNORECASE)
  if(user_profile and user_profile['username']):
    search_result = pattern.search(user_profile['username'])
    if(search_result):
      return True
  return False

def filter_based_on_country(json_object, given_country):
  user_profile = json_object.get('user_profile')
  if(user_profile and user_profile.get('country', None) == given_country):
    return True
  return False