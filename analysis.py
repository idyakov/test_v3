# Open the newly uploaded image
input_path_logo = "/mnt/data/logo1.png"
image_logo = Image.open(input_path_logo)

# Resize the image to 1024x1024 while maintaining aspect ratio
image_logo_resized = image_logo.resize((1024, 1024))

# Save the resized image in different formats
output_path_logo_jpeg = "/mnt/data/converted_logo_1024.jpeg"
output_path_logo_png = "/mnt/data/converted_logo_1024.png"
output_path_logo_bmp = "/mnt/data/converted_logo_1024.bmp"
output_path_logo_ico = "/mnt/data/converted_logo_1024.ico"

# Convert to RGB before saving as JPEG
image_logo_resized_rgb = image_logo_resized.convert("RGB")
image_logo_resized_rgb.save(output_path_logo_jpeg, "JPEG")
image_logo_resized.save(output_path_logo_png, "PNG")
image_logo_resized.save(output_path_logo_bmp, "BMP")
image_logo_resized.save(output_path_logo_ico, "ICO")

#output_path_logo_jpeg, output_path_logo_png, output_path_logo_bmp, output_path_logo_ico