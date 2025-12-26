class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
        self.clean_mark_before_washing = self.clean_mark


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]):
        income = 0
        for car in cars:
            if self.wash_single_car(car):
                income += self.calculate_washing_price(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        costs = round(
            car.comfort_class
            * (self.clean_power - car.clean_mark_before_washing)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )
        return costs

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark_before_washing = car.clean_mark
            car.clean_mark = self.clean_power
            return True
        return False

    def rate_service(self, rate: int) -> None:
        rating = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(rating / self.count_of_ratings, 1)
