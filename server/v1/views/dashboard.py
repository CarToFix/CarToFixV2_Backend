from fastapi import APIRouter, Query, HTTPException

#from models.task import Task


router = APIRouter()


set_versions = {
    "get_workshop_active_tasks" = ""
}


# Harcoded examples -----------------------------------------
class Task:
    def __init__(self, done, title):
        import uuid
        self.public_oid = uuid.uuid4()
        self.done = done
        self.vehicle = {str(uuid.uuid4()): "future vehicle dictionary"}
        self.title = title
        self.description = "future task description"
        self.note = "future task note"
        self.parts = ["part1", "part2", "part3"]
        self.workshop = {str(uuid.uuid4()): "future vehicle dictionary"}
        self.employees = ["future", "list", "of", "employees"]
        self.created_by = {str(uuid.uuid4()): "future employee dictionary"}
        self.quote = {str(uuid.uuid4()): "future quote dictionary"}

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

# Generate 30 tasks
import random
tasks = []
for i in range(30):
    done = random.choice([True, False])
    title = titles[i]
    tasks.append(Task(done=done, title=title))

# ------------------------------------------------------------------------------------------------------------

@router.get("/dashboard/active_workshop_tasks")
async def get_workshop_active_tasks(workshop_name: str = Query(..., description="The workshop's name")):
    return [{t.title: t.__dict__} for t in tasks if t.done == True]
