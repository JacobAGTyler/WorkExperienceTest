import os

from example_generator import generate_random_product_recommendations


product_count: int = int(os.environ['ProductCount'])
start_id: int = int(os.environ['StartID'])
max_id: int = int(os.environ['MaxID'])

generate_random_product_recommendations(
  product_count=product_count,
  start_id=start_id,
  max_id=max_id
)