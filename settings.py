#Task 1 and 2
def add_setting(settings, setting_pairs):
    key, value = setting_pairs
    value = value.lower()
    key = key.lower()

    if key in settings:
        return f"Setting {key} already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting {key} added with value {value} successfully!"
        

#Task 3 and 4
def update_setting(settings, setting_pairs):
    key, value = setting_pairs
    value = value.lower()
    key = key.lower()

    if key in settings:
        settings[key] = value
        return f"Setting {key} updated to {value} successfully!"
    else:
        return f"Setting {key} does not exist! Cannot update a non-existing setting."

#Task 5 and 6
def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return f"Setting not found!"
    else:
        settings.pop(key)
        return f"Setting {key} deleted successfully!"

#Task 7 and 8
def view_settings(settings):

    if not settings:
        return "No settings available."
    else:
        result = "Current User Settings:"
        for key, value in settings.items():
            result += f"\n{key.capitalize()}: {value}"
        return result

test_settings = {"theme": "dark", "notifications": "enabled", "volume": "high"}

print(add_setting(test_settings, ("language", "English")))
print(add_setting(test_settings, ("theme", "light")))




