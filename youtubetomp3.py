import os
from pytube import YouTube
from pydub import AudioSegment

def download_and_convert(url, output_path):
    try:
        # Download video using pytube
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        
        if stream:
            temp_file_path = "temp.mp4"
            stream.download(output_path=output_path, filename=temp_file_path)

            # Check if the file was downloaded successfully
            if os.path.exists(os.path.join(output_path, temp_file_path)):
                # Convert video to audio
                audio = AudioSegment.from_file(os.path.join(output_path, temp_file_path), format="mp4")

                # Get the title of the video
                video_title = yt.title 

                # Remove invalid characters from the filename
                video_title = ''.join(char for char in video_title if char.isalnum() or char in [' ', '.', '_'])

                # Define the full path for the output file
                output_file_path = os.path.join(output_path, f"{video_title}.mp3")

                # Export the audio to the specified output file path
                audio.export(output_file_path, format="mp3")

                # Delete temporary video file
                os.remove(os.path.join(output_path, temp_file_path))
                
                print(f"Successfully downloaded and converted: {video_title}.mp3")
            else:
                print("Failed to download the video.")
        else:
            print("No audio stream available for the provided URL.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = input("Enter the URL of the YouTube video: ")
output_directory = input("Enter the full path of the directory where you want to save the file: ")

# Call the function with the video URL and output directory
download_and_convert(video_url, output_directory)
