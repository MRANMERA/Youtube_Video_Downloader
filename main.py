from pytube import YouTube
import os

def download_video():
    while True:
        try:
            url = input("Enter the YouTube video URL (or 'quit' to exit): ")
            if url.lower() == 'quit':
                print("Exiting video downloader.")
                break

            video = YouTube(url)
            title = video.title

            # Check if 720p stream is available, otherwise use the highest resolution stream
            stream_720p = video.streams.filter(res="720p", file_extension="mp4", progressive=True).first()
            if stream_720p:
                stream = stream_720p
            else:
                stream = video.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()

            if stream is None:
                print("No suitable video stream found. Please try another video.")
                continue

            # Download video
            stream.download(output_path=os.getcwd(), filename=f"{title}.mp4")
            print(f"{title}.mp4 has been downloaded.")

            choice = input("Do you want to download another video? (yes/no): ")
            if choice.lower() != 'yes':
                print("Exiting video downloader.")
                break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    download_video()

