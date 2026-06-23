"""
utils.py

Utility functions for validation and input handling.
"""

import re


def validate_vehicle_id(vehicle_id):
    """
    Validate vehicle number format.

    Examples:
    AP28Z1234
    TN05AB789
    """
    pattern = r"^[A-Z]{2}\d{2}[A-Z]{1,2}\d{3,4}$"

    if not re.match(pattern, vehicle_id):
        raise ValueError(
            "Invalid Vehicle ID. Example: AP28Z1234 or TN05AB789"
        )

    return True


def validate_capacity(capacity):
    """
    Validate vehicle capacity.
    """
    if capacity <= 0:
        raise ValueError("Capacity must be greater than zero.")

    return True


def validate_route_number(route_number):
    """
    Validate route number.
    """
    if route_number <= 0:
        raise ValueError("Route number must be positive.")

    return True


def validate_distance(distance):
    """
    Validate distance.
    """
    if distance <= 0:
        raise ValueError("Distance must be greater than zero.")

    return True


def validate_contact(contact):
    """
    Validate 10-digit mobile number.
    """
    if not re.match(r"^\d{10}$", contact):
        raise ValueError(
            "Contact number must contain exactly 10 digits."
        )

    return True


def validate_license(license_number):
    """
    Validate license number length.
    """
    if len(license_number) != 16:
        raise ValueError(
            "License number must contain exactly 16 characters."
        )

    return True


def get_positive_integer(message):
    """
    Safe integer input.
    """
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                raise ValueError

            return value

        except ValueError:
            print("Enter a valid positive integer.")


def get_positive_float(message):
    """
    Safe float input.
    """
    while True:
        try:
            value = float(input(message))

            if value <= 0:
                raise ValueError

            return value

        except ValueError:
            print("Enter a valid positive number.")