"""
vehicles.py

Demonstrates:
- Classes & Objects
- Class Variables
- Instance Variables
- Class Methods
- Static Methods
- Inheritance
- Method Overriding
- Polymorphism
- __str__
- __repr__
"""

import re


class Vehicle:
    """
    Base Vehicle Class.
    """

    college_name = "ACE Engineering College"
    total_vehicles = 0

    def __init__(
        self,
        vehicle_id,
        vehicle_type,
        capacity
    ):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity = capacity

        Vehicle.total_vehicles += 1

    @classmethod
    def get_total_vehicles(cls):
        """
        Return total vehicles count.
        """
        return cls.total_vehicles

    @staticmethod
    def validate_vehicle_number(vehicle_number):
        """
        Validate vehicle number.

        Examples:
        AP28Z1234
        TN05AB789
        """
        pattern = r"^[A-Z]{2}\d{2}[A-Z]{1,2}\d{3,4}$"

        return bool(
            re.match(pattern, vehicle_number)
        )

    def display_info(self):
        """
        Method overridden by subclasses.
        """
        print("Vehicle Information")


class Bus(Vehicle):
    """
    Bus Class.
    """

    def __init__(
        self,
        vehicle_id,
        capacity,
        route_number,
        has_ac
    ):
        super().__init__(
            vehicle_id,
            "Bus",
            capacity
        )

        self.route_number = route_number
        self.has_ac = has_ac

    def __str__(self):
        return (
            f"Bus [{self.vehicle_id}] | "
            f"Route: {self.route_number} | "
            f"Capacity: {self.capacity} | "
            f"AC: {'Yes' if self.has_ac else 'No'}"
        )

    def __repr__(self):
        return (
            f"Bus("
            f"vehicle_id='{self.vehicle_id}', "
            f"route_number={self.route_number})"
        )

    def display_info(self):
        """
        Polymorphic implementation.
        """
        print(self)


class MiniVan(Vehicle):
    """
    MiniVan Class.
    """

    def __init__(
        self,
        vehicle_id,
        capacity,
        trip_purpose
    ):
        super().__init__(
            vehicle_id,
            "MiniVan",
            capacity
        )

        self.trip_purpose = trip_purpose

    def __str__(self):
        return (
            f"MiniVan [{self.vehicle_id}] | "
            f"Purpose: {self.trip_purpose}"
        )

    def __repr__(self):
        return (
            f"MiniVan("
            f"vehicle_id='{self.vehicle_id}', "
            f"trip_purpose='{self.trip_purpose}')"
        )

    def display_info(self):
        """
        Polymorphic implementation.
        """
        print(self)