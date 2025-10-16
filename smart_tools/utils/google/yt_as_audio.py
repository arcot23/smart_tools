import os
import yt_dlp


def download_youtube_audio(url: str, output_folder: str = ".", ffmpeg_location=r"c:\drivers\ffmpeg\bin") -> str:
    """
    Downloads audio from a YouTube video and saves it as an MP3 file.

    Parameters:
        url (str): YouTube video URL.
        output_folder (str): Directory where the MP3 file will be saved.

    Returns:
        str: Path to the saved MP3 file.
    """
    try:
        os.makedirs(output_folder, exist_ok=True)

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
            "ffmpeg_location": ffmpeg_location,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": False,
            "noplaylist": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get("title", None)
            mp3_path = os.path.join(output_folder, f"{title}.mp3")

        print(f"✅ Downloaded and saved as: {mp3_path}")
        return mp3_path

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Download YouTube video audio as MP3."
    )

    parser.add_argument(
        "-u", "--url",
        type=str,
        help="The YouTube video URL to download audio from."
    )

    parser.add_argument(
        "-o", "--output-folder",
        type=str,
        default=".",
        help="Target folder to save the downloaded MP3 (default: current directory)."
    )

    parser.add_argument(
        "-f", "--ffmpeg-location",
        type=str,
        default=r"c:\drivers\ffmpeg\bin",
        help="Path to ffmpeg/ffprobe binaries (default: local ffmpeg path)."
    )

    args = parser.parse_args()

    # 👇 Interactive fallback if not provided
    if not args.url:
        args.url = input("Enter YouTube video URL: ").strip()

    try:
        download_youtube_audio(
            url=args.url,
            output_folder=args.output_folder,
            ffmpeg_location=args.ffmpeg_location
        )
        print(f"✅ Audio downloaded successfully to: {args.output_folder}")
    except Exception as e:
        print(f"❌ Failed to download audio: {e}")
