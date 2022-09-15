from booking.booking import Booking


# inst=Booking()
# inst.land_first_page()
try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go("New York")
        bot.select_dates(check_in='2022-09-15', check_out='2022-09-22')
        bot.select_adults(10)
        bot.click_searh()
        bot.apply_filter()
        bot.refresh()
        bot.report()

        print("Exiting ... ")
except Exception as  e:
    if 'in PATH' in str(e):
        print("There is a problem running from cmd")
    else:
        raise