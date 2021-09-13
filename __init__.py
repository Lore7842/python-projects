from Hotel_Search_Bot.booking import Booking

with Booking() as app:
    app.visitWebsite()
    app.change_currency(currency='EUR')
    app.select_place_to_go('Venezia')
    app.select_dates('2021-10-05', '2021-10-10')
    app.select_adults(2)
    app.click_search()
    app.close_Message()