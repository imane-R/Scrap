class Book:
    def __init__(self, title, price, availability, rating):
        self.title = title
        self.price = price
        self.availability = availability
        self.rating = rating

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "availability": self.availability,
            "rating": self.rating
        }
