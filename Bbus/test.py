from tkinter import *
from PIL import Image, ImageTk, ImageSequence

# Create a window
window = Tk()

# Load the GIF image
gifImage = Image.open("image/main_image_gif.gif")

# Create an iterator to iterate through the frames of the GIF
iterator = ImageSequence.Iterator(gifImage)

# Create a PhotoImage object to display the first frame of the GIF
photo = ImageTk.PhotoImage(next(iterator))

# Create a label to display the GIF
label = Label(window, image=photo)
label.pack()

# GIF frame update function
def update_frame():
    global gifImage, iterator
    try:
        # Update the GIF image
        gifImage.seek(gifImage.tell() + 1)
        photo.paste(next(iterator))
    except EOFError:
        # If it reaches the last frame, go back to the first frame
        gifImage.seek(0)
        iterator = ImageSequence.Iterator(gifImage)
        photo.paste(next(iterator))

    # Update the PhotoImage object



    # Schedule the next frame update
    window.after(100, update_frame)  # Update every 10ms (0.1 seconds)

# Schedule the first frame update
window.after(100, update_frame)

# Start the main loop
window.mainloop()