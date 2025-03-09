def main():
    animals = {
        "cow": "moo",
        "horse": "neigh",
        "pig": "oink",
        "sheep": "baa",
        "dog": "bark"
    }

    old_mac = "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"

    for k, v in animals.items():
        print(old_mac)
        print(f"And on that farm he had a {k}, Ee-igh, Ee-igh, Oh!")
        print(f"With a {v}, {v} here and a {v}, {v} there.")
        print(f"Here a {v}, there a {v}, everywhere a {v}, {v}.")
        print(old_mac + "\n")


main()
