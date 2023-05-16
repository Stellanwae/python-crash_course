def car_info(model_name, manufacturer, **all_info):
    all_info['Model_name'] = model_name
    all_info['manufacturer'] = manufacturer
    print(all_info)
car_info('Mercedes Benze', 'Mercedes', Country = 'Germany', Class = 3)
