""" This file contains the code for downloading audio and video from YouTube """

from pytube import YouTube
import os


class YoutubeHandler:
    def __init__(self, link):
        self.savePath = f"{os.getcwd()}\\Downloads"
        self.videoLink = link
        self.youtubeHandler = YouTube(self.videoLink)

    def getAudio(self, name=None):
        audioFile = self.youtubeHandler.streams.filter(type="audio").order_by("abr").desc().first()
        if name: audioFile.download(filename=name, output_upath=self.savePath)
        else: audioFile.download(output_path=self.savePath)

    def getVideo(self):
        videoFile = self.youtubeHandler.streams
        for vid in videoFile:
            print(vid)


if __name__ == '__main__':
    links = [
        "https://www.youtube.com/watch?v=EVPKj91hEcY"
    ]
    video = YoutubeHandler(links[0])
    video.getVideo()
    # for audio_link in links:
    #     video = YoutubeHandler(audio_link)
    #     video.audioLink()
    #     del video
