

#This is an audio visualizer that reads direct audio input from the mic and takes the frequency and amplitude data to create appropiately sized and colored shapes.
#The frequency of the sampled audio data determines the color of the shape with low frequencies being associated with a given RGB value and higher frequencies being asscoited with different RGB values 
#The amplitude of the sampled audio data determines the size of the shapes
#Additional elements were added for the visualizer to be used for events and a amplitude threshold variable was added to adjust the sensitivty of the program. 

import pyaudio
import pygame
import numpy as np
import random
import struct 
import math 
import cv2

# Set up the Pygame window
window_width = 1920
window_height = 1080
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("CASA Visualizer")

video = cv2.VideoCapture("leblanc.mp4")
success, video_image = video.read()
fps = video.get(cv2.CAP_PROP_FPS)
clock = pygame.time.Clock()


#Default Image Size
DEFAULT_IMAGE_SIZE = (1078,480)
#images
c_Img = pygame.image.load('IMG_9428.png')
c2_Img = pygame.image.load('CASA Neon Effect.png')
cloud = pygame.image.load('/Users/joshtran/AV Project /cloudblueneon.png')
cheshire = pygame.image.load('smile_red.png')
default_bg = (0,0,0)
alice_falling_bg = pygame.image.load('alice falling.png')
alice_falling_neon_bg = pygame.image.load('alice falling neon.png')
afr = pygame.image.load('alice falling reverse.png')
afnr = pygame.image.load('alice falling neon reverse.png')
rook = pygame.image.load('rook.png').convert_alpha()
alicejump = pygame.image.load('alice jumping neon.png')
alicejumpr = pygame.image.load('alice jumping neon reverse.png')


#Image functions
def scaleImage(image, DEFAULT_IMAGE_SIZE):
    scaledImg = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
    return scaledImg 


def Img(scaledImg, x,y):
    screen.blit(scaledImg, (x,y))

def draw_spiral(screen, x, y, theta, radius, color):
    for i in range(200):
        theta += math.pi/20
        radius += 0.075
        x += radius*math.cos(theta)
        y += radius*math.sin(theta)
        pygame.draw.circle(screen, color, (int(x), int(y)), 2)

#Rook class for falling rooks 
class Rook: 
    def __init__(self, x, y):
        self.surface = pygame.transform.scale(pygame.image.load('rook neon.png').convert_alpha(), (204,204))
        self.x = x 
        self.y = y 
        self.speed = random.randint(10,15)
        self.angle = 0 
        self.omega = 3
        self.vx = 0 
    def move(self):
        self.y += self.speed 
        self.x += self.vx 
        self.angle += self.omega
    def fall(self, screen):
        rotated_rook = pygame.transform.rotate(self.surface,self.angle)
        screen.blit(rotated_rook, (self.x,self.y))

rooks = []

def generate_rooks():
    x = random.randint(-200,window_width)
    y = -300 
    rooks.append(Rook(x,y))


#bounce variables 
bounce_speed = 5
bounce_height = 100
direction = 1
directionr = 1

#scaled images and starting positions 
alicejumpScaled = scaleImage(alicejump, (450, 611))
alicejumprScaled = scaleImage(alicejumpr, (450, 611))
character_x = 1200
character_xr = 200
character_y = window_height - alicejumpScaled.get_height() + 150
character_yr = window_height - alicejumprScaled.get_height() + 150

# Set up the Pyaudio input stream
chunk_size = 512
sample_rate = 11025
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate,
                input=True, frames_per_buffer=chunk_size)

clock = pygame.time.Clock()

running = success
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
     # Read the audio input from the Pyaudio stream
    success, video_image = video.read()
    if success:
        video_surf = pygame.image.frombuffer(
            video_image.tobytes(), video_image.shape[1::-1], "BGR")
    else:
        # Reset video capture to the beginning of the video
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        success, video_image = video.read()
        video_surf = pygame.image.frombuffer(
            video_image.tobytes(), video_image.shape[1::-1], "BGR")
    screen.blit(video_surf, (0, 0))
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

    low_freq_color = (255, 0, 0)   # Red
    high_freq_color = (0, 239, 255)  # Blue
    max_freq = max(freq_data)
    amplitude_threshold = 1000
    # Define the maximum lifespan of each shape (in milliseconds)
    max_lifespan = 1000
    # Store the creation time of each shape
    creation_times = []
    


    # Create the geometric shapes and patterns based on the audio input
    if max(amplitude_data) > amplitude_threshold:
        if rms_amplitude > 50000:
            # Fill the background with white
            screen.fill(white)
            casaRandom = random.randint(0,1)
            Img(casa_scaled, 450, 300)
            #cloud_scaled = scaleImage(cloud, (353,217))
            #Img(cloud_scaled, random.randint(-353, 1567), random.randint(-217, 863))

        if rms_amplitude < 4100:
            # screen.fill(default_bg) 
            casaRandom = random.randint(0,1)
            Img(casa_scaled, 360, 300)
            if random.random()<0.1:
                generate_rooks()
    
            for rook in rooks:
                rook.move()
                rook.fall(screen)
                rooks = [rook for rook in rooks if rook.y < window_height + 100]
            
   
            # Move the character up and down to mimic a bounce
            character_y += direction * bounce_speed
            if character_y < 600:
                direction = 1
            elif character_y > 700:
                direction = -1

            character_yr += directionr * bounce_speed
            if character_yr < 600:
                directionr = 1
            elif character_yr > 700:
                directionr = -1

            # Draw the character and update the screen
            screen.blit(alicejumpScaled, (character_x, character_y))
            screen.blit(alicejumprScaled, (character_xr, character_yr))

            if casaRandom == 0:
                Img(afnr,0,0)
                Img(alice_falling_neon_bg, 600,0)
                Img(afnr,30,0)
                Img(alice_falling_neon_bg, 570,0)
                Img(casa_scaled, 360, 300)
            else: 
                Img(alice_falling_bg, 600,0)
                Img(afr, 0,0)
                Img(casa_scaled, 360, 300)
                cheshire_scaled = scaleImage(cheshire, DEFAULT_IMAGE_SIZE)
                # Img(cheshire, 680, 500)
        for i in range(round(len(freq_data)/10)):
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
            #draw_spiral(screen, x_pos, y_pos, 0, 0, shape_color )
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

    clock.tick(60)
