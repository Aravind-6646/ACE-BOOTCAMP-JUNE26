"""
drivers.py

Demonstrates:
- Encapsulation
- Property Decorators
- Getter
- Setter
- Deleter
"""

import re


class Driver:
    """
    Driver Class.
    """

    def __init__(
        self,
        name,
        license_number,
        contact
    ):
        self.name = name
        self.license_number = license_number
        self.contact = contact

    # -------------------------
    # LICENSE PROPERTY
    # -------------------------

    @property
    def license_number(self):
        """
        Getter
        """
        return self._license_number

    @license_number.setter
    def license_number(self, value):
        """
        Setter
        """
        if len(value) != 16:
            raise ValueError(
                "License number must contain exactly 16 characters."
            )

        self._license_number = value

    # -------------------------
    # CONTACT PROPERTY
    # -------------------------

    @property
    def contact(self):
        """
        Getter
        """
        return self._contact

    @contact.setter
    def contact(self, value):
        """
        Setter
        """
        if not re.match(r"^\d{10}$", value):
            raise ValueError(
                "Contact must contain exactly 10 digits."
            )

        self._contact = value

    @contact.deleter
    def contact(self):
        """
        Deleter
        """
        print("Contact information deleted.")
        del self._contact

    def __str__(self):
        return (
            f"Driver: {self.name} | "
            f"License: {self.license_number} | "
            f"Contact: {self.contact}"
        )

    def __repr__(self):
        return (
            f"Driver("
            f"name='{self.name}', "
            f"license='{self.license_number}')"
        )