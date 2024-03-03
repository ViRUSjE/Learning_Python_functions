dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Stars Wars"
}

def message(dict):
    if all(key in dict for key in ["name", "role", "movie"]):
        return f"In {dict['movie']}, {dict['name']} is a {dict['role']}."
    else:
        return None

print(message(dict))