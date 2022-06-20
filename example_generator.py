import random
import json
import datetime


def generate_random_product_recommendations(
  product_count: int,
  start_id: int,
  max_id: int
):
  product_list = []
  
  for r in range(product_count):
    product_list.append(random.randint(101, 1000000))
  
  product_recommendations = {}
  
  for i in product_list:
    i_list = []
    for ri in range(random.randrange(2, 30)):
      ab = product_list[random.randint(0,(product_count-1))]
  
      if ab == i:
        continue
      
      i_list.append(f'AB{ab}')
    product_recommendations[f'AB{i}'] = i_list
  
  
  with open('example_data.json', 'w') as file:
    now = datetime.datetime.now()
    now = now.isoformat()
    
    product_data = {
      'generated': now,
      'productRecommendations': product_recommendations
    }
    json.dump(product_data, file, indent=2)
