GET_LIST_PRODUCT = """
  SELECT 
    id,
    price,
    product_name AS name,
    img_path AS path
    FROM
      project_app_product
      ORDER BY id DESC
      LIMIT {0}, {1}
"""