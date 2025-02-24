COLOUR_TO_HEX = {"amaranth": "#e52b50", "antiquewhite": "#faebd7", "apricot": "#fbceb1", "aqua": "#00ffff",
                 "beaver": "#9f8170", "beige": "#f5f5dc", "bistre": "#3d2b1f", "bittersweet": "#fe6f5e",
                 "blueviolet": "#8a2be2", "brass": "#b5a642"}
maximum_colour_length = max(len(code) for code in COLOUR_TO_HEX.keys())

for colour_name, hex_code in COLOUR_TO_HEX.items():
    print(f"{colour_name:<{maximum_colour_length}} is {hex_code}")

colour_name = input("Enter short state: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid short state")
    hex_code = input("Enter short state: ").lower()
