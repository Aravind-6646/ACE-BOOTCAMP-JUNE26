"""
transport_manager.py

Demonstrates:
- Composition
- Polymorphism
"""

from vehicles import Vehicle


class TransportManager:
    """
    Transport Manager.
    """

    def __init__(
        self,
        manager_name="Mr. Ramesh"
    ):
        self.manager_name = manager_name

        # Composition
        self.buses = []
        self.mini_vans = []
        self.drivers = []

    # --------------------------
    # BUS
    # --------------------------

    def add_bus(
        self,
        bus
    ):
        self.buses.append(bus)

    # --------------------------
    # MINIVAN
    # --------------------------

    def add_minivan(
        self,
        minivan
    ):
        self.mini_vans.append(minivan)

    # --------------------------
    # DRIVER
    # --------------------------

    def add_driver(
        self,
        driver
    ):
        self.drivers.append(driver)

    # --------------------------
    # DISPLAY VEHICLES
    # --------------------------

    def display_all_vehicles(self):

        all_vehicles = (
            self.buses +
            self.mini_vans
        )

        print("\n" + "=" * 50)
        print(
            f"ACE College Vehicle Fleet "
            f"- Total: {len(all_vehicles)}"
        )
        print("=" * 50)

        # Polymorphism
        for vehicle in all_vehicles:
            vehicle.display_info()
            print("-" * 50)

    # --------------------------
    # DISPLAY DRIVERS
    # --------------------------

    def display_all_drivers(self):

        print("\n" + "=" * 50)
        print("DRIVER DETAILS")
        print("=" * 50)

        if not self.drivers:
            print("No drivers available.")
            return

        for driver in self.drivers:
            print(driver)

    # --------------------------
    # SEARCH VEHICLE
    # --------------------------

    def search_vehicle(
        self,
        vehicle_id
    ):
        """
        Search by vehicle id.
        """

        all_vehicles = (
            self.buses +
            self.mini_vans
        )

        for vehicle in all_vehicles:

            if vehicle.vehicle_id == vehicle_id:
                return vehicle

        return None

    # --------------------------
    # DASHBOARD
    # --------------------------

    def display_dashboard(self):

        total_buses = len(self.buses)

        total_minivans = len(
            self.mini_vans
        )

        total_drivers = len(
            self.drivers
        )

        print("\n" + "=" * 50)
        print("TRANSPORT DASHBOARD")
        print("=" * 50)
        print()

        print(
            f"Manager Name      : "
            f"{self.manager_name}"
        )

        print(
            f"Total Buses       : "
            f"{total_buses}"
        )

        print(
            f"Total MiniVans    : "
            f"{total_minivans}"
        )

        print(
            f"Total Drivers     : "
            f"{total_drivers}"
        )

        print(
            f"Total Vehicles    : "
            f"{Vehicle.get_total_vehicles()}"
        )

        print("\n" + "=" * 50)