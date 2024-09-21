from models.task import Task
from models.quote import Quote
from models.employee import Employee
from models.workshop import Workshop

import random
import string
import copy
import uuid
import datetime



def gen_tasks():
    titles = [
        "Fix the Invisible Air Conditioner",
        "Unblock the Cosmic Sink",
        "Tune the Galactic Guitar",
        "Repair the Quantum Microwave",
        "Assemble the Interstellar Coffee Maker",
        "Clean the Space-Time Refrigerator",
        "Upgrade the Time-Traveling Toaster",
        "Refuel the Alien Spaceship",
        "Repaint the Moon’s Crater",
        "Adjust the Interplanetary Antenna",
        "Debug the Extra-Terrestrial Lightbulb",
        "Fix the Asteroid Belt Fountain",
        "Service the Martian Hoverboard",
        "Adjust the Galactic GPS",
        "Tune the UFO Engine",
        "Replace the Nebula Lightbulb",
        "Refurbish the Cosmic Lawn Mower",
        "Rewire the Space Shuttle Console",
        "Install the Alien Home Theater System",
        "Polish the Starship’s Hull",
        "Replace the Rocket’s Turbocharger",
        "Repair the Space Elevator",
        "Tune the Solar-Powered Radio",
        "Clean the Intergalactic Telescope",
        "Unjam the Stellar Printer",
        "Fix the Martian Satellite Dish",
        "Repair the Moon Rover’s Tires",
        "Upgrade the Starship’s Coffee Maker",
        "Tune the Cosmic Drum Kit",
        "Fix the Galaxy’s Wi-Fi Router",
        "Refuel the Galactic Jetpack"
    ]

    tasks = []
    for i in range(30):

        done = random.choice([True, False])
        title = titles[i]
        t = Task(
            title=title,
            vehicle={str(uuid.uuid4()): "future vehicle dictionary"},
            desc="future task description",
            notes="future task note",
            parts=["part1dict", "part2dict", "part3dict"],
            wshop={str(uuid.uuid4()): "future vehicle dictionary"},
            emps=["future", "list", "of", "dicts", "of", "employees"],
            quote=None
        )

        t.done = done
        tasks.append(t)
    
    return tasks


def generate_random_future_date():
        # Define the start date as today
    start_date = datetime.date.today() + datetime.timedelta(days=30)

    # Define the maximum number of days into the future
    max_days = 365 * 4000

    end_date = start_date + datetime.timedelta(days=max_days)
    
    # Calculate the number of days between start_date and end_date
    delta_days = (end_date - start_date).days
    
    # Generate a random number of days within the range
    random_days = random.randint(0, delta_days)
    
    # Calculate the random future date
    random_future_date = start_date + datetime.timedelta(days=random_days)
    
    return random_future_date


list_of_tasks = gen_tasks()
def gen_quotes():
    quotes = []

    for i in range(20):
        price = str(random.randint(100, 100000))
        created_by = {"user": "future user dictionary"}
        payment_method = random.choice(["debit card", "credit card", "cash", "other"])
        warranty = generate_random_future_date()
        instalments = 4530245
        tasks = copy.deepcopy(random.sample(list_of_tasks, random.randint(1, 10)))
        pdue_date = warranty + datetime.timedelta(days=3022)
        sent = random.choice([True, False])
        active = random.choice([True, False])
        confirmed = random.choice([datetime.datetime.now(), None])
        inspect = "DONT HAVE A CLUE WHAT IS THIS"

        q = Quote(
            price,
            created_by,
            tasks,
            payment_method,
            warranty,
            instalments,
            pdue_date,
            sent,
            active,
            confirmed,
            inspect
        )

        for task in q.tasks:
            task.quote = q.oid

        quotes.append(q)

    return quotes

brands = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "BMW", "Mercedes-Benz", "Audi", "Hyundai", "Volkswagen"]
models = [
    ["Camry", "Corolla", "Highlander", "RAV4", "Prius"],  # Toyota models
    ["Civic", "Accord", "CR-V", "Pilot", "Fit"],          # Honda models
    ["F-150", "Mustang", "Explorer", "Fusion", "Escape"], # Ford models
    ["Silverado", "Malibu", "Tahoe", "Impala", "Equinox"],# Chevrolet models
    ["Altima", "Sentra", "Rogue", "Murano", "Maxima"],    # Nissan models
    ["3 Series", "X5", "5 Series", "X3", "7 Series"],     # BMW models
    ["C-Class", "E-Class", "GLC", "GLE", "S-Class"],      # Mercedes-Benz models
    ["A4", "Q5", "A6", "Q7", "A3"],                       # Audi models
    ["Elantra", "Sonata", "Santa Fe", "Tucson", "Kona"],  # Hyundai models
    ["Golf", "Passat", "Tiguan", "Jetta", "Atlas"]        # Volkswagen models
]
generate_fake_plate = lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=8))
get_brand = lambda: random.choice(brands)
get_model = lambda brand: random.choice(models[brands.index(brand)])
