"""
main.py

ACE Engineering College Transportation Portal

Main application file.
"""

from vehicles import Bus, MiniVan
from drivers import Driver
from fare import RouteFare, SpecialTripFare
from transport_manager import TransportManager

from utils import (
    validate_vehicle_id,
    validate_capacity,
    validate_route_number,
    validate_distance,
)

# --------------------------------------
# MANAGER OBJECT
# --------------------------------------

manager = TransportManager()


def add_new_bus():
    """
    Add bus.
    """

    try:
        print("\nADD NEW BUS")

        vehicle_id = input(
            "Enter Vehicle ID: "
        ).upper()

        validate_vehicle_id(vehicle_id)

        capacity = int(
            input("Enter Capacity: ")
        )

        validate_capacity(capacity)

        route_number = int(
            input("Enter Route Number: ")
        )

        validate_route_number(
            route_number
        )

        ac_choice = input(
            "AC Bus (Y/N): "
        ).upper()

        has_ac = ac_choice == "Y"

        bus = Bus(
            vehicle_id,
            capacity,
            route_number,
            has_ac
        )

        manager.add_bus(bus)

        print(
            "\nBus added successfully."
        )

    except Exception as error:
        print(
            f"Error: {error}"
        )


def add_new_minivan():
    """
    Add minivan.
    """

    try:
        print("\nADD NEW MINIVAN")

        vehicle_id = input(
            "Enter Vehicle ID: "
        ).upper()

        validate_vehicle_id(vehicle_id)

        capacity = int(
            input("Enter Capacity: ")
        )

        validate_capacity(capacity)

        purpose = input(
            "Trip Purpose: "
        )

        minivan = MiniVan(
            vehicle_id,
            capacity,
            purpose
        )

        manager.add_minivan(
            minivan
        )

        print(
            "\nMiniVan added successfully."
        )

    except Exception as error:
        print(
            f"Error: {error}"
        )


def add_new_driver():
    """
    Add driver.
    """

    try:
        print("\nADD NEW DRIVER")

        name = input(
            "Driver Name: "
        )

        license_number = input(
            "License Number (16 chars): "
        )

        contact = input(
            "Contact Number: "
        )

        driver = Driver(
            name,
            license_number,
            contact
        )

        manager.add_driver(
            driver
        )

        print(
            "\nDriver added successfully."
        )

    except Exception as error:
        print(
            f"Error: {error}"
        )


def calculate_route_fare():
    """
    Route fare.
    """

    try:
        print(
            "\nROUTE FARE CALCULATOR"
        )

        student_id = input(
            "Student ID: "
        )

        distance = float(
            input(
                "Distance (km): "
            )
        )

        validate_distance(
            distance
        )

        pass_type = input(
            "Pass Type "
            "(Monthly/Semester): "
        )

        fare = RouteFare(
            student_id,
            distance,
            pass_type
        )

        fare.display_fare_summary()

    except Exception as error:
        print(
            f"Error: {error}"
        )


def calculate_special_trip_fare():
    """
    Special trip fare.
    """

    try:
        print(
            "\nSPECIAL TRIP FARE"
        )

        distance = float(
            input(
                "Distance (km): "
            )
        )

        validate_distance(
            distance
        )

        num_students = int(
            input(
                "Number of Students: "
            )
        )

        fare = SpecialTripFare(
            distance,
            num_students
        )

        fare.display_fare_summary()

    except Exception as error:
        print(
            f"Error: {error}"
        )


def search_vehicle():
    """
    Search vehicle.
    """

    vehicle_id = input(
        "Enter Vehicle ID: "
    ).upper()

    vehicle = (
        manager.search_vehicle(
            vehicle_id
        )
    )

    if vehicle:
        print("\nVehicle Found")
        print("-" * 40)
        vehicle.display_info()

    else:
        print(
            "Vehicle not found."
        )


def display_menu():
    """
    Display menu.
    """

    print("\n")
    print("=" * 55)
    print(
        "ACE Engineering College Transportation Portal"
    )
    print("=" * 55)

    print("\n1. Add New Bus")
    print("2. Add New MiniVan")
    print("3. Add New Driver")
    print("4. Display All Vehicles")
    print("5. Display All Drivers")
    print("6. Calculate Route Fare")
    print("7. Calculate Special Trip Fare")
    print("8. Search Vehicle by ID")
    print("9. Display Dashboard Summary")
    print("0. Exit Portal")

    print("\n" + "=" * 55)


def main():
    """
    Main function.
    """

    while True:

        display_menu()

        choice = input(
            "Enter Choice: "
        )

        if choice == "1":
            add_new_bus()

        elif choice == "2":
            add_new_minivan()

        elif choice == "3":
            add_new_driver()

        elif choice == "4":
            manager.display_all_vehicles()

        elif choice == "5":
            manager.display_all_drivers()

        elif choice == "6":
            calculate_route_fare()

        elif choice == "7":
            calculate_special_trip_fare()

        elif choice == "8":
            search_vehicle()

        elif choice == "9":
            manager.display_dashboard()

        elif choice == "0":

            print(
                "\nThank you for using "
                "ACE Transportation Portal."
            )

            break

        else:
            print(
                "Invalid choice."
            )


if __name__ == "__main__":
    main()