"""
routes.py

Demonstrates:
- Lists
- Tuples
- Sets
- Dictionaries
- Functions
"""

# ----------------------------
# LIST
# ----------------------------

route_1_stops = [
    "College Gate",
    "RTC Cross",
    "Miyapur"
]

# ----------------------------
# TUPLE
# GPS Coordinates
# ----------------------------

route_coordinates = (
    17.4946,
    78.3918
)

# ----------------------------
# SET
# Unique Student Pass IDs
# ----------------------------

student_pass_ids = set()

# ----------------------------
# DICTIONARY
# Bus Fleet Details
# ----------------------------

bus_fleet = {
    "AP28Z1234": {
        "driver": "Ramesh",
        "route": 3
    }
}


def display_route_stops():
    """
    Display route stops.
    """
    print("\nROUTE STOPS")
    print("-" * 30)

    for stop in route_1_stops:
        print(stop)


def add_stop(stop_name):
    """
    Add stop to route.
    """
    route_1_stops.append(stop_name)

    print(f"{stop_name} added successfully.")


def register_student_pass(pass_id):
    """
    Register student pass.
    """
    student_pass_ids.add(pass_id)

    print("Student pass registered successfully.")


def display_bus_details():
    """
    Display bus fleet information.
    """
    print("\nBUS FLEET DETAILS")
    print("-" * 40)

    for vehicle_id, details in bus_fleet.items():
        print(
            f"Vehicle: {vehicle_id} | "
            f"Driver: {details['driver']} | "
            f"Route: {details['route']}"
        )