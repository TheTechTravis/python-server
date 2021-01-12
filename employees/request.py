EMPLOYEES = [
    {
        "id": 1,
        "name": "Scott Silver",
        "locationId": 1,
        "animalId": 5
    },
    {
        "name": "Jisie Davis",
        "locationId": 1,
        "animalId": 5,
        "id": 2
    }
]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    # Variable to hold the found location, if it exists
    requested_employee = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
