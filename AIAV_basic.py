import pyaudio
import pygame
import numpy as np
import random
import struct 
import math 

#This is an audio visualizer that reads direct audio input from the mic and takes the frequency and amplitude data to create appropiately sized and colored shapes.
#The frequency of the sampled audio data determines the color of the shape with low frequencies being associated with a given RGB value and higher frequencies being asscoited with different RGB values 
#The amplitude of the sampled audio data determines the size of the shapes
#Additional elements were added for the visualizer to be used for events and a amplitude threshold variable was added to adjust the sensitivty of the program. 


# Set up the Pygame window
window_width = 1920
window_height = 1080
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("CASA Visualizer")
#Default Image Size
DEFAULT_IMAGE_SIZE = (1078,480)
#images
c_Img = pygame.image.load('IMG_9428_purple.png')
c2_Img = pygame.image.load('CASA Neon Effect.png')
cloud = pygame.image.load('/Users/joshtran/AV Project /cloudblueneon.png')
default_bg = (0,0,0)
def scaleImage(image, DEFAULT_IMAGE_SIZE):
    scaledImg = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
    return scaledImg 
def Img(scaledImg, x,y):
    screen.blit(scaledImg, (x,y))


# Set up the Pyaudio input stream
chunk_size = 512
sample_rate = 11025
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate,
                input=True, frames_per_buffer=chunk_size)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
     # Read the audio input from the Pyaudio stream
    data = stream.read(chunk_size, exception_on_overflow=False)
    # Convert the data to integers
    int_data = struct.unpack(f"{chunk_size}h", data)

    # Calculate the root mean square (RMS) amplitude of the audio input
    amplitude_data = [abs(x) for x in int_data]
    rms_amplitude = math.sqrt(sum([(x ** 2) for x in amplitude_data]) / len(amplitude_data))

    # Convert the data to a numpy array
    data_array = np.frombuffer(data, dtype=np.int16)
    # Apply the Fast Fourier Transform (FFT) to the data array
    fft_data = np.fft.rfft(data_array)
    # Extract the frequency and amplitude data from the FFT data
    freq_data = np.abs(fft_data)
    amp_data = np.abs(freq_data) / chunk_size
    # Create a list to store the shapes
    casa_scaled = scaleImage(c_Img, DEFAULT_IMAGE_SIZE)
    casa2_scaled = scaleImage(c2_Img, DEFAULT_IMAGE_SIZE)


    white = (255, 255, 255)
    shapes = []

    # Define the maximum lifespan of each shape (in frames)
    max_lifespan = 1

    low_freq_color = (231, 6, 255)   # Red
    high_freq_color = (10, 252, 252)  # Blue
    max_freq = max(freq_data)
    amplitude_threshold = 2000
    # Define the maximum lifespan of each shape (in milliseconds)
    max_lifespan = 1000
    # Store the creation time of each shape
    creation_times = []

    # Create the geometric shapes and patterns based on the audio input
    if max(amplitude_data) > amplitude_threshold:
        if rms_amplitude > 2100:
            # Fill the background with white
            screen.fill(white)
            casaRandom = random.randint(0,1)
            if casaRandom == 0:
                Img(casa_scaled, 450, 300)
            else: 
                Img(casa2_scaled, 450, 300)
            cloud_scaled = scaleImage(cloud, (353,217))
            Img(cloud_scaled, random.randint(-353, 1567), random.randint(-217, 863))
        if rms_amplitude < 2100:
            screen.fill(default_bg) 
            casaRandom = random.randint(0,1)
            if casaRandom == 0:
                Img(casa_scaled, 450, 300)
            else: 
                Img(casa2_scaled, 450, 300)
            cloud_scaled = scaleImage(cloud, (353,217))
            Img(cloud_scaled, random.randint(-353, 1567), random.randint(-217, 863))
        for i in range(round(len(freq_data)/6)):
            shape_size = 50
            x_pos = random.randint(0, window_width - shape_size)
            y_pos = random.randint(0, window_height - shape_size)
            shape_type = random.choice(["circle", "square"])
            shape_thickness = random.randint(1, 5)
            shape_size = int(freq_data[i] / 1000)
            if shape_size <= 0:
                shape_size = 1
            shape_lifespan = max_lifespan
            # Calculate the color based on the frequency
            freq_ratio = freq_data[i] / max_freq
            shape_color = tuple(int(low_freq_color[c] + freq_ratio * (high_freq_color[c] - low_freq_color[c])) for c in range(3))
            shape = {
                "x_pos": x_pos,
                "y_pos": y_pos,
                "type": shape_type,
                "color": shape_color,
                "thickness": shape_thickness,
                "size": shape_size
            }
            shapes.append(shape)
            # Store the creation time of the shape
            creation_times.append(pygame.time.get_ticks())

        # Draw the shapes on the screen
        for i, shape in enumerate(shapes):
            x_pos = shape["x_pos"]
            y_pos = shape["y_pos"]
            shape_type = shape["type"]
            shape_color = shape["color"]
            shape_thickness = shape["thickness"]
            shape_size = shape["size"]
            pygame.draw.circle(screen, shape_color, (x_pos, y_pos), shape_size, shape_thickness) if shape_type == "circle" else pygame.draw.rect(screen, shape_color, (x_pos, y_pos, shape_size, shape_size), shape_thickness)
            # Check if the shape has exceeded its maximum lifespan
            if pygame.time.get_ticks() - creation_times[i] >= max_lifespan:
                # Remove the shape from the list and the creation time from the creation_times list
                shapes.pop(i)
                creation_times.pop(i)
    # Draw the shapes and patterns on the Pygame window
    pygame.display.flip()

    # Update the Pygame window
    pygame.display.update()
