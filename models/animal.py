class Animal():

    # Class initializer. It has 8 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, status, breed, customer_id, location_id,
                 location, customer):
        self.id = id
        self.name = name
        self.status = status
        self.breed = breed
        self.customerId = customer_id
        self.locationId = location_id
        self.location = None
        self.customer = None
