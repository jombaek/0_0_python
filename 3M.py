name = input()
k = float(input())

print("""SELECT
  id,
  SUM(product_price) AS revenue_by_user
FROM
  dataset.data_table
WHERE
  ab_test = '""" + name + "'" + """
GROUP BY
  id
HAVING
  revenue_by_user < """ + str(f'{k:.2f}'))