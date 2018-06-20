class Purchase:
    def __init__(self, street, city, zipcode, state, beds, baths, sq__ft,
                 home_type, sale_date, price, latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.sale_date = sale_date
        self.home_type = home_type
        self.sq__ft = sq__ft
        self.baths = baths
        self.beds = beds
        self.state = state
        self.zipcode = zipcode
        self.city = city
        self.street = street

    @staticmethod
    def create_from_dict(dictionary):
        return Purchase(
            dictionary['street'],
            dictionary['city'],
            dictionary['zip'],
            dictionary['state'],
            int(dictionary['beds']),
            int(dictionary['baths']),
            int(dictionary['sq__ft']),
            dictionary['type'],
            dictionary['sale_date'],
            float(dictionary['price']),
            float(dictionary['latitude']),
            float(dictionary['longitude']),
        )
