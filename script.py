from models.client import Client

cl = Client("juan", "juan@gmail.com", "09898123")
print(f"Client dict '{cl.to_dict(hors={'hide': ['oid', 'updated_at', '_sa_instance_state', 'created_at']})}'")