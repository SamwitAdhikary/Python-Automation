from booking.makemytrip import MakeMyTrip

if __name__ == "__main__":
    bot = MakeMyTrip()

    bot.land_page()
    # bot.close_popup()
    bot.search_from_city()
    bot.search_to_city()
    bot.departure_date()
    bot.travellers()
    bot.submit_btn()
    bot.press_okay_btn()
    bot.filter_minimum()