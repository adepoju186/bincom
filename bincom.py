from collections import Counter
import random
def sum_fibonacci(n):
    a, b = 0, 1
    total_sum=0

    for _ in range(n):
        total_sum += a
        a, b =  b, a = b


        return total_sum
    

colors  = [
        "GREEN","YELLOW" ,"GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", 
    "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
    
    "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", 
    "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE",
    
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", 
    "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE",
    
    "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", 
    "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",

    "GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", 
    "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"
]
color_frequencies = Counter(colors)

most_worn_color = max(color_frequencies, key=color_frequencies.get)
most_worn_count = color_frequencies[most_worn_color]


print(f"The most worn color is {most_worn_color}, worn {most_worn_count} times.")
sorted_frequencies = sorted(color_frequencies.items(), key=lambda x: x[1])

# Step 3: Extract frequencies and determine median index
frequencies = [freq for _, freq in sorted_frequencies]
n = len(frequencies)

if n % 2 == 1:  # Odd case
    median_frequency = frequencies[n // 2]
    median_color = [color for color, freq in sorted_frequencies if freq == median_frequency]
else:  # Even case
    median_frequency = (frequencies[n // 2 - 1] + frequencies[n // 2]) / 2
    median_color = [color for color, freq in sorted_frequencies if freq in (frequencies[n // 2 - 1], frequencies[n // 2])]

# Output the result
print(f"The median frequency is: {median_frequency}")
print(f"The color(s) corresponding to the median frequency is/are: {median_color}")




color_frequency= list(color_frequencies.values())


mean_frequency = sum(color_frequency) / len(frequencies)

squared_differences = [(f - mean_frequency) ** 2 for f in color_frequency]


variance = sum(squared_differences) / len(color_frequency)

print(f"The variance of the color frequencies is: {variance}")

# Step 1: RGB values for each color
color_rgb = {
    "GREEN": (0, 128, 0),
    "YELLOW": (255, 255, 0),
    "BROWN": (150, 75, 0),
    "BLUE": (0, 0, 255),
    "PINK": (255, 192, 203),
    "ORANGE": (255, 165, 0),
    "CREAM": (255, 253, 208),
    "RED": (255, 0, 0),
    "WHITE": (255, 255, 255),
    "ARSH": (0, 0, 0),  # Assigning placeholder (unknown color)
    "BLEW": (0, 0, 255),  # Assuming typo for "BLUE"
    "BLACK": (0, 0, 0)
}

# Step 2: Count frequencies of each color
color_frequencies = Counter(colors)

# Step 3: Calculate the weighted sum of RGB values
total_r, total_g, total_b = 0, 0, 0
total_count = 0

for color, freq in color_frequencies.items():
    r, g, b = color_rgb[color]
    total_r += r * freq
    total_g += g * freq
    total_b += b * freq
    total_count += freq

# Step 4: Compute the mean RGB values
mean_r = total_r / total_count
mean_g = total_g / total_count
mean_b = total_b / total_count

mean_color = (mean_r, mean_g, mean_b)

# Output the mean color (RGB)
print(f"Mean color (RGB): {mean_color}")



# Step 1: Generate a random 4-digit binary number
binary_number = ''.join(random.choice('01') for _ in range(4))

# Step 2: Convert the binary number (as a string) to base 10
base_10_number = int(binary_number, 2)

# Output the results
print(f"Generated binary number: {binary_number}")
print(f"Converted to base 10: {base_10_number}")
