
def process_data(car_data):
  years = {}
  most_sales = {'car': {}, 'sales': 0}
  
  for item in car_data:
    car = item['car']
    if item['total_sales'] > most_sales['sales']:
      most_sales['car'] = car
      most_sales['sales'] = item['total_sales']

    if car['car_year'] not in years:
      years[car['car_year']] = 0
    years[car['car_year']] += 1

    popular_year = max(years, key=years.get)

  summary = [""]
  summary.append("The {car_model} had the most sales: {total_sales}"
                 .format(car_model=format_car(most_sales['car']),
                         total_sales=most_sales['sales']))
  summary.append("The most popular year was {year} with {total_sales} sales."
                 .format(year=popular_year, total_sales=years[popular_year]))

    
msg = process_data()
paragraph = "<br/>".join(msg)
report.generate('/tmp/cars.pdf', 'Sales summary for last month', process_data(), cars_dict_to_table())
emails.generate("automation@example.com", "student@example.com", "Sales summary for last month", "\n".join(msg), "/tmp/cars.pdf")

