from pytube import YouTube
from pathlib import Path    # To get the download folder path

if __name__ == "__main__":
    
    vid_url = input("Enter URL here: ")
    vid_name = input("Save as: ")
    vid_down_path = str(Path.home() / "Downloads")

    try:
        yt = YouTube(vid_url)
        yt.streams.filter(progressive=True, file_extension="mp4").first().download(
            output_path=vid_down_path, filename=vid_name)
        print(vid_name + " downloaded successfully")
    except:
        print("Video Cannot Be Downloaded")
