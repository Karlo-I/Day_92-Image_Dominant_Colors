import colorgram
from collections import Counter
from PIL import Image
from color_utils import rgb_distance, rgb_to_hex

# Most dominant colours incl. percentages
def get_colour_dominance(image_path, num_colours=10, tolerance=50):
    colours = colorgram.extract(image_path, num_colours)
    img = Image.open(image_path)
    pixels = list(img.getdata())

    extracted_colours = [tuple(colour.rgb) for colour in colours] # Extracted colors in a list of RGB tuples

    matched_colours = [] # List of matched colors with a tolerance level

    # For each pixel, match it with the extracted colours within tolerance level
    for pixel in pixels:
        matched = False
        for colour in extracted_colours:
            if rgb_distance(pixel, colour) < tolerance:
                matched_colours.append(colour)
                matched = True
                break
        if not matched:
            matched_colours.append(None)  # No match, but still count it

    colour_counts = Counter(matched_colours) # Occurrences of each matched color

    total_pixels = len(pixels) # Total number of pixels

    # Output for each color, calculate the percentage of its occurrence
    colour_info = []
    for colour in extracted_colours:
        count = colour_counts[colour]
        percentage = (count / total_pixels) * 100
        hex_code = rgb_to_hex(*colour)
        colour_info.append((colour, hex_code, percentage))

    colour_info.sort(key=lambda x: x[2], reverse=True) # Percentage sorted in descending order

    return colour_info