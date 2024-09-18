from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from PIL import Image
import os

def generatePDF(image_files):
    # PDF file output
    pdf_file = "multiple_images_grid.pdf"
    pdf = canvas.Canvas(pdf_file, pagesize=A4)

    # Get A4 page size
    page_width, page_height = A4

    # Grid settings
    cols = 2  # Number of columns in the grid
    rows = 3  # Number of rows in the grid
    grid_cell_width = page_width / cols  # Width of each grid cell
    grid_cell_height = page_height / rows  # Height of each grid cell
    margin = 0.25 * inch  # Margin between the grid cells

    # Loop through each image and add to the PDF
    current_x = 0
    current_y = page_height

    for idx, image in enumerate(image_files):
        image_path = os.path.join("images_folder/", image)
        
        # Open image to get dimensions
        with Image.open(image_path) as img:
            img_width, img_height = img.size
            aspect_ratio = img_width / img_height
            
            # Calculate the width and height of the image, preserving the aspect ratio
            if aspect_ratio > 1:  # Image is wider than tall
                img_display_width = grid_cell_width - 2 * margin
                img_display_height = img_display_width / aspect_ratio
            else:  # Image is taller than wide
                img_display_height = grid_cell_height - 2 * margin
                img_display_width = img_display_height * aspect_ratio

            # Check if the current image fits on the page, if not, create a new page
            if idx % (cols * rows) == 0 and idx > 0:
                pdf.showPage()  # Start a new page
                current_x = 0
                current_y = page_height  # Reset y position for new page

            # Calculate position within the grid cell
            x_pos = current_x + (grid_cell_width - img_display_width) / 2
            y_pos = current_y - (grid_cell_height - img_display_height) / 2 - img_display_height
            
            # Draw the image
            pdf.drawImage(image_path, x_pos, y_pos, width=img_display_width, height=img_display_height)
            
            # Update x position for the next image
            current_x += grid_cell_width

            # If we've filled a row, move to the next row
            if (idx + 1) % cols == 0:
                current_x = 0
                current_y -= grid_cell_height

    # Save the PDF
    pdf.save()

    print(f"PDF with multiple images in a grid created successfully: {pdf_file}")

# Example usage
# image_files = ['D:\\OneDrive\\Desktop\\raw\\flowC.png', 'D:\\OneDrive\\Desktop\\raw\\googlelogo.png', 'D:\\OneDrive\\Desktop\\raw\\log file creation.png', 'D:\\OneDrive\\Desktop\\raw\\loginPage_Img.jpeg', 'D:\\OneDrive\\Desktop\\raw\\phases.png', 'D:\\OneDrive\\Desktop\\raw\\sameer.jpg', 'D:\\OneDrive\\Desktop\\raw\\Signature .jpg', 'D:\\OneDrive\\Desktop\\raw\\usecase.png']
# generatePDF(image_files)
