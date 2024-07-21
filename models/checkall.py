import os
import importlib.util

def get_python_files(directory):
    """Get a list of .py files in the specified directory."""
    return [f for f in os.listdir(directory) if f.endswith('.py') and not f.startswith('__')]

def import_module_from_file(file_path):
    """Dynamically import a module from a file path."""
    module_name = os.path.basename(file_path).replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def get_class_name_from_file(file_name):
    """Map file names to their corresponding class names."""
    class_name_mapping = {
        'vehicle_model': 'VehicleModel',
        'vehicle_brand': 'VehicleBrand'
    }
    base_name = file_name.replace('.py', '')
    return class_name_mapping.get(base_name, base_name.replace('_', '').capitalize())

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    py_files = get_python_files(current_dir)
    
    instances = {}
    
    for file in py_files:
        if file == 'checkall.py':
            continue
        
        module = import_module_from_file(os.path.join(current_dir, file))
        class_name = get_class_name_from_file(file)
        
        if hasattr(module, class_name):
            cls = getattr(module, class_name)
            if class_name != 'Common':
                instances[class_name] = cls()
        else:
            print(f"Warning: No class named '{class_name}' in '{file}'\n")
    
    for name, instance in instances.items():
        print(f"Instance of {name}: {'.' * (30 - len(name))} {instance}")

if __name__ == "__main__":
    main()
