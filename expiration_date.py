import datetime

def expiration_date(number_of_hours):
    now = datetime.datetime.now()
    #print(now.strftime("%d.%m.%Y %H:%M:%S"))

    date_today = now.strftime("%a %b %d 8:00:00 %Y")
    now_datetime = now.strftime("%d.%m.%Y %H:%M:%S") # текущее время в системе
    date_today = datetime.datetime.strptime(date_today, "%a %b %d %H:%M:%S %Y")
    date_today_f = date_today.strftime("%d.%m.%Y %H:%M:%S")


    def expiration_date(number_of_hours):
        try:
            date_plus_hours = date_today + datetime.timedelta(hours=number_of_hours)
            return date_today_f, number_of_hours, date_plus_hours.strftime("%d.%m.%Y %H:%M:%S")
        except OverflowError:
            return "Сэр, вы ввели избыточное значение! Попробуйте ещё раз :)"


    return f"текущее время в системе: {now_datetime}\n{(expiration_date(number_of_hours))}"

#print(expiration_date(36))

#print(expiration_date(72))
#print(expiration_date(140))
#print(expiration_date(120))