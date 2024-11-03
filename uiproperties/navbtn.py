from PIL import Image

# Open the uploaded image
image_path = 'screen.png'
image = Image.open(image_path)

# Display the dimensions of the image
coordinate_x = image.size[0]
coordinate_y = image.size[1]


# To analyze the exact coordinates of each bottom navigation button, we'll calculate approximate positions
# based on a typical layout where buttons are evenly spaced at the bottom.

# Assuming the navigation bar is at the bottom of the image
bottom_nav_y = coordinate_y - 100  # Approximate Y-coordinate from the bottom (adjustable as needed)

# Each button width (assuming equal spacing and 5 buttons)
button_width = coordinate_x // 5

# Calculating approximate X-coordinates for each button's center
home_button_x = button_width * 0.5
search_button_x = button_width * 1.5
add_button_x = button_width * 2.5
reels_button_x = button_width * 3.5
profile_button_x = button_width * 4.5

# Defining button coordinates as tuples (x, y)
coordinates_bottom_nav = {
    "home_button": (int(home_button_x), bottom_nav_y),
    "search_button": (int(search_button_x), bottom_nav_y),
    "add_button": (int(add_button_x), bottom_nav_y),
    "reels_button": (int(reels_button_x), bottom_nav_y),
    "profile_button": (int(profile_button_x), bottom_nav_y)
}


acivity_button_x = button_width * 3.7
messege_button_x = button_width * 4.7

top_nav_y = int(coordinate_y / 14)
coordinates_top_nav = {
    "acivity_button": (int(acivity_button_x), top_nav_y),
    "messege_button": (int(search_button_x), top_nav_y),
    
}

