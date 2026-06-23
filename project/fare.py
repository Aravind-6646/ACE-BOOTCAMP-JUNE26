"""
fare.py

Demonstrates:
- ABC
- Abstract Methods
- Inheritance
- Polymorphism
"""

from abc import ABC, abstractmethod


class FareCalculator(ABC):
    """
    Abstract Fare Calculator.
    """

    @abstractmethod
    def calculate_fare(self):
        pass

    @abstractmethod
    def display_fare_summary(self):
        pass

    def apply_discount(
        self,
        amount,
        discount_percent=10
    ):
        """
        Shared method.
        """
        discount_amount = (
            amount * discount_percent / 100
        )

        return amount - discount_amount


class RouteFare(FareCalculator):
    """
    Route Fare Calculator.
    """

    def __init__(
        self,
        student_id,
        distance,
        pass_type
    ):
        self.student_id = student_id
        self.distance = distance
        self.pass_type = pass_type

    def calculate_fare(self):
        """
        Monthly Fare = distance * 2.5
        Semester Fare = distance * 12
        """

        if self.pass_type.lower() == "monthly":
            fare = self.distance * 2.5
        else:
            fare = self.distance * 12

        return fare

    def display_fare_summary(self):
        """
        Display receipt.
        """

        fare = self.calculate_fare()
        final_amount = self.apply_discount(fare)

        print("\n[ROUTE FARE CALCULATOR]")
        print()

        print(
            f"Student ID      : {self.student_id}"
        )

        print(
            f"Distance (km)   : {self.distance}"
        )

        print(
            f"Pass Type       : "
            f"{self.pass_type.title()}"
        )

        print("-" * 28)

        print(
            f"Fare Calculated : "
            f"Rs. {fare:.2f}"
        )

        print(
            "Discount Applied: 10%"
        )

        print(
            f"Final Amount    : "
            f"Rs. {final_amount:.2f}"
        )


class SpecialTripFare(FareCalculator):
    """
    Special Trip Fare Calculator.
    """

    def __init__(
        self,
        distance,
        num_students
    ):
        self.distance = distance
        self.num_students = num_students

    def calculate_fare(self):
        """
        Total Fare
        """
        return (
            self.distance
            * 5
            * self.num_students
        )

    def display_fare_summary(self):
        """
        Display detailed fare.
        """

        total_fare = self.calculate_fare()

        per_student = (
            total_fare /
            self.num_students
        )

        print("\n[SPECIAL TRIP FARE]")
        print()

        print(
            f"Distance (km)      : "
            f"{self.distance}"
        )

        print(
            f"Students Count     : "
            f"{self.num_students}"
        )

        print("-" * 35)

        print(
            f"Total Fare         : "
            f"Rs. {total_fare:.2f}"
        )

        print(
            f"Per Student Fare   : "
            f"Rs. {per_student:.2f}"
        )