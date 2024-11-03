import cv2
import numpy as np

# Load the main image and the icon template image
main_image = cv2.imread('main_image.png')
icon_template = cv2.imread('backarrow_icon_dark.png')

if main_image is None:
    print("Error: Could not open or find the main image.")
    exit()
if icon_template is None:
    print("Error: Could not open or find the icon template image.")
    exit()

# Convert both images to grayscale
main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(icon_template, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise in both images
main_gray = cv2.GaussianBlur(main_gray, (5, 5), 0)
template_gray = cv2.GaussianBlur(template_gray, (5, 5), 0)

# Get the dimensions of the template
template_height, template_width = template_gray.shape[:2]

# Perform template matching
result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# Set a threshold based on the maximum matching score
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
threshold = max_val * 0.8  # Set threshold as 80% of max score

# Find locations above the threshold
locations = np.where(result >= threshold)

# Non-maximum suppression to avoid multiple detections for the same icon
detected_positions = []
center_positions = []
for pt in zip(*locations[::-1]):
    # Check if the new point overlaps with existing detected points
    if all(abs(pt[0] - p[0]) > template_width or abs(pt[1] - p[1]) > template_height for p in detected_positions):
        detected_positions.append(pt)
        
        # Calculate the center of the detected icon
        center_x = pt[0] + template_width // 2
        center_y = pt[1] + template_height // 2
        center_positions.append((center_x, center_y))
        
        # Draw a rectangle around the matched region
        cv2.rectangle(main_image, pt, (pt[0] + template_width, pt[1] + template_height), (0, 255, 0), 2)
        
        # Draw a circle at the center for visualization
        cv2.circle(main_image, (center_x, center_y), 5, (255, 0, 0), -1)

# Resize the image for display while maintaining the aspect ratio
aspect_ratio = main_image.shape[1] / main_image.shape[0]
new_width = 400
new_height = int(new_width / aspect_ratio)
display_image = cv2.resize(main_image, (new_width, new_height))

# Display the image with detected icons and centers
cv2.imshow("Detected Icons with Centers", display_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the coordinates of detected icons and their centers
print("Detected icon coordinates (top-left corner):", detected_positions)
center_positions = [(x + template_width // 2, y + template_height // 2) for (x, y) in detected_positions]
print("Center coordinates of detected icons:", center_positions)
