def Conversion(mask):
    try:
        octets = mask.strip().split(".")
        if len(octets) != 4:
            raise ValueError

        wildcard = [str(255 - int(o)) for o in octets]
        return ".".join(wildcard)

    except:
        return "Invalid subnet mask"

# Loop so you can keep using it
while True:
    data = input("Enter subnet mask (or 'q' to quit): ")

    if data.lower() == "q":
        break

    result = Conversion(data)
    print("Wildcard mask:", result)
