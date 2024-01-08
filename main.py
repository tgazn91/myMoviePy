from moviepy.editor import VideoFileClip

# Replace 'your_video_file.mkv' with the path to your actual video file
video_path = r"C:\Users\Copy&PasteYourVideoFilePathHere.mkv"

# Load the video file into the 'video' variable
video = VideoFileClip(video_path)

# Define the start and end times for the clip you want to cut out (in seconds)
start_time = "00:00:00.00"  # The time the clip should start at
end_time = "00:00:05.00"    # The time the clip should end at

# Cut the clip between start_time and end_time
cut_video = video.subclip(start_time, end_time)

# Define the coordinates for the top-left and bottom-right corners of the crop
# Adjust accordingly
x1 = 0    # Left
y1 = 110  # Top
x2 = 1295 # Right
y2 = 685  # Bottom

# Now that 'cut_video' has been defined, you can crop it
cropped_video = cut_video.crop(x1=x1, y1=y1, x2=x2, y2=y2)

# Write the cropped and cut video to a file
cropped_video.write_videofile("cropped_output.mkv", codec='libx264')
