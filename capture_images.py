import picamera
from PIL import Image
import time

# Setup
num_images = 20
interval_seconds = 5
image_directory = "/path/to/save/directory/"  # Adjust to your desired path

with picamera.PiCamera() as camera:
    # Start the camera preview
    camera.start_preview()
    time.sleep(2)  # Give the camera some time to warm up
    
    for i in range(num_images):
        # Annotate the current image count on the preview
        camera.annotate_text = f"Capturing image {i+1} of {num_images}"
        
        image_name = f"image_{i+1}.jpg"
        image_path = image_directory + image_name
        
        # Capture and save the image
        camera.capture(image_path)
        print(f"Captured {image_name}")
        
        # Stop the preview
        camera.stop_preview()
        
        # Show the captured image using PIL for a brief moment
        img = Image.open(image_path)
        img.show()
        time.sleep(0.5)
        
        # Start the preview again
        camera.start_preview()
        
        # If it's not the last image, wait for the next interval minus the half-second "freeze"
        if i < num_images - 1:
            time.sleep(interval_seconds - 0.5)
    
    # Stop the camera preview
    camera.stop_preview()

print("Finished capturing images.")
