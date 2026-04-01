from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars from Japan"},
        {"name": "Mercedes", "description": "Luxury cars from Germany"},
        {"name": "Audi", "description": "Premium German automobiles"},
        {"name": "Kia", "description": "Reliable Korean cars"},
        {"name": "Toyota", "description": "Dependable Japanese vehicles"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make, created = CarMake.objects.get_or_create(
            name=data['name'], defaults={'description': data['description']}
        )
        car_make_instances.append(car_make)

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV",   "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Qashqai",    "type": "SUV",   "year": 2023, "car_make": car_make_instances[0]},
        {"name": "XTRAIL",     "type": "SUV",   "year": 2023, "car_make": car_make_instances[0]},
        {"name": "A Class",    "type": "SUV",   "year": 2023, "car_make": car_make_instances[1]},
        {"name": "C Class",    "type": "SUV",   "year": 2023, "car_make": car_make_instances[1]},
        {"name": "E Class",    "type": "SUV",   "year": 2023, "car_make": car_make_instances[1]},
        {"name": "A4",         "type": "SUV",   "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A5",         "type": "SUV",   "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A6",         "type": "SEDAN", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Sorento",    "type": "SUV",   "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Carnival",   "type": "SUV",   "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Kona",       "type": "SUV",   "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Corolla",    "type": "SEDAN", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Camry",      "type": "SEDAN", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "RAV4",       "type": "SUV",   "year": 2023, "car_make": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.get_or_create(
            name=data['name'],
            car_make=data['car_make'],
            defaults={'type': data['type'], 'year': data['year']}
        )