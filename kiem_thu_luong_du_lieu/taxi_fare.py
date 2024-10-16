class TaxiFareCalculator:
    def __init__(self):
        self.opening_fare = 30000  
        self.fare_up_to_20km = 20000  
        self.fare_above_21km = 10000  

    def calculate_fare(self, distance: float, num_people: int) -> float:
        if distance < 0 or distance > 200:
            raise ValueError("Khoảng cách phải từ 0 đến 200 km")

        if num_people < 1 or num_people >= 6:
            raise ValueError("Số lượng người phải lớn hơn 1 và dưới 6 người")
        
        fare_for_one = self.opening_fare

        if distance > 1:
            if distance <= 20:
                fare_for_one += (distance - 1) * self.fare_up_to_20km
            else:
                fare_for_one += 19 * self.fare_up_to_20km  
                fare_for_one += (distance - 20) * self.fare_above_21km  

        fare_taxi = 0

        if num_people > 1:
            fare_taxi = fare_for_one + fare_for_one * 0.2 * (num_people - 1)
        else:
            fare_taxi = fare_for_one
        return fare_taxi
    

if __name__ == "__main__":
    calculator = TaxiFareCalculator()
    fare = calculator.calculate_fare(10, 1)
    print(fare)