def day_of_year(date_string):
    import datetime
    fmt = '%Y-%m-%d %H:%M:%S'
    date = datetime.datetime.strptime(date_string, fmt)
    return date.strftime('%j')