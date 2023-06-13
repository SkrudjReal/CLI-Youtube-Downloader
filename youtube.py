#!/bin/python3
from yt_dlp import YoutubeDL
from os.path import exists
from rich import print
import shutil
import os
from colorama import Fore

os.system('clear')

green = Fore.LIGHTGREEN_EX
lcyan = Fore.LIGHTCYAN_EX
lmagenta = Fore.LIGHTMAGENTA_EX
lyellow = Fore.LIGHTYELLOW_EX
lblue = Fore.LIGHTBLUE_EX
lred = Fore.LIGHTRED_EX
magenta = Fore.MAGENTA
green = Fore.GREEN
black = Fore.LIGHTBLACK_EX
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
clear = '\033[39m'

mp = 'mp4'
ma = 'm4a'
descriptions_dir = 'descriptions'
sortdirmp4 = 'mp4'
sortdirm4a ='m4a'
sorttxt = 'sorttxt.txt'

print("Developer: [bold cyan]Scrooge[/bold cyan]", ":wine_glass:")
print("Visit my [bold magenta]https://t.me/OnlyLinksuy[/bold magenta] channel!")
print("[italic bold red]Don't forget remove archive or be error[/italic bold red]", ":point_up:")

try:
    start = input(lgreen+'\n(m)'+'mpv live & playlist \n\n'+lcyan+"(enter)"+clear+"video/sound \n"+lmagenta+"(a)"+clear+"v/s/sort/desc/photo \n"+lyellow+"(ac)"+clear+"channel \n"+lblue+"(d)"+clear+"description \n"+lred+"(s)"+clear+"sort files"+cyan+"\n(p)"+clear+"preview of video"+clear+"\n\nWhich one?: "+clear)
except KeyboardInterrupt:
    print()
    exit()


def startm():
    link = input("Link to youtube video/playlist/channel: ")
    e_video_audio = input("(v)video & (s)sound?: ")
    
    if e_video_audio == 'v':
        
        if 'watch?v' in link:
        
            with YoutubeDL() as ydl: 
                info_dict = ydl.extract_info(link, download=False)
                video_resolution = info_dict.get('resolution')
            print("\nYour video resolution: "+video_resolution) # не баг а фича, так красиво.
        
            quality = input("\n1 - 144p \n2 - 240p \n3 - 360p \n4 - 480p \n5 - 720p \n6 - 1080p"+"\nChoose quality: ")
        
            if quality == '1':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?256][height<=?144][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            if quality == '2':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?426][height<=?240][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            if quality == '3':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?480][height<=?360][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            if quality == '4':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?640][height<=?480][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            if quality == '5':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?1280][height<=?720][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            elif quality == '6':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?1920][height<=?1080][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            else:
                print("Not correct answer!")
                exit()
    
        else:
        
            quality = input("\n1 - 144p \n2 - 240p \n3 - 360p \n4 - 480p \n5 - 720p \n6 - 1080p"+"\nChoose quality: ")
        
            if quality == '1':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?256][height<=?144][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            if quality == '2':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?426][height<=?240][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            if quality == '3':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?480][height<=?360][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            if quality == '4':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?640][height<=?480][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            if quality == '5':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?1280][height<=?720][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            elif quality == '6':
                os.system(f"mpv --ytdl-format='bestvideo[width<=?1920][height<=?1080][fps<=?30][vcodec!=?h264]+bestaudio/best[fps<=?30]' {link}")
            else:
                print("Not correct answer!")
                exit()
            
    elif e_video_audio == 's':
        os.system(f"mpv --ytdl-format='bestaudio' --no-video {link}")
    
    else:
        print("Not correct answer!")
        exit()

    print(lgreen+"successfully")
    exit()


def ifstartenter():
    link = input("Link to youtube video/playlist/channel: ")
    e_video_audio = input("(v)video & (s)sound?: ")
    filesize = input("Set a max file size like - 10M or pass: ")
    
    
    if 'M' in filesize:
        if e_video_audio == "v":
                os.system(f"yt-dlp -f '[filesize<={filesize}]' --merge-output-format mp4 {link} --embed-thumbnail -o '%(title)s.%(ext)s'")
        elif e_video_audio == "s":
            os.system(f"yt-dlp -f '[filesize<={filesize}]' -x --audio-format {ma} {link} --embed-thumbnail -o '%(title)s.%(ext)s'")
        else:
            print('Not correct answer')
    else:
        if e_video_audio == "v":
            quality = input("\n1 - 144p \n2 - 240p \n3 - 360p \n4 - 480p \n5 - 720p \n6 - 1080p"+"\nChoose quality: ")
            
            if quality == '1':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=256][height<=144]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} --embed-thumbnail -o '%(title)s144p'")
            if quality == '2':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=426][height<=240]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} --embed-thumbnail -o '%(title)s240p'")
            if quality == '3':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=480][height<=360]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} --embed-thumbnail -o '%(title)s360p'")
            if quality == '4':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=640][height<=480]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} --embed-thumbnail -o '%(title)s480p'")
            if quality == '5':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=1280][height<=720]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} --embed-thumbnail -o '%(title)s720p'")
            elif quality == '6':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=1920][height<=1080]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} --embed-thumbnail -o '%(title)s1080p'")
            else:
                print('Not correct answer')
        elif e_video_audio == "s":
            os.system(f"yt-dlp -f 'ba' -x --audio-format {ma} {link} --embed-thumbnail -o '%(title)s.%(ext)s'")
            
    print("successfully")
    exit()


def starta():
    link = input("Link to youtube video/playlist/channel: ")
        
    e_video_audio = input("(v)video & (s)sound?: ")
    name_of_dir = input("enter the name of the directory to be created for download: ")
    filesize = input("Set a max file size like - 10M or pass: ")
    
    
    if 'M' in filesize:
        if e_video_audio == 'v':
            os.system(f"yt-dlp -f '[filesize<={filesize}]' --merge-output-format mp4 {link} -o '{name_of_dir}/%(title)s.%(ext)s' --write-thumbnail --write-subs --sub-format 'srt' --sub-langs 'en,ru,ua' --download-archive archive.txt")
              
        elif e_video_audio == 's':
            os.system(f"yt-dlp -f '[filesize<={filesize}]' -x --audio-format {ma} {link} -o '{name_of_dir}/%(title)s.%(ext)s' --write-thumbnail --write-subs --sub-format 'srt' --sub-langs 'en,ru,ua' --download-archive archive.txt")

        else:
            print("Not correct answer!")
            exit()
    else:
        if e_video_audio == "v":
            quality = input("\n1 - 144p \n2 - 240p \n3 - 360p \n4 - 480p \n5 - 720p \n6 - 1080p"+"\nChoose quality: ")
            
            if quality == '1':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=256][height<=144]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} -o '{name_of_dir}/%(title)s.%(ext)s' --write-thumbnail --write-subs --sub-format 'srt' --sub-langs 'en,ru,ua' --download-archive archive.txt")
            if quality == '2':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=426][height<=240]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} -o '{name_of_dir}/%(title)s.%(ext)s' --write-thumbnail --write-subs --sub-format 'srt' --sub-langs 'en,ru,ua' --download-archive archive.txt")
            if quality == '3':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=480][height<=360]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} -o '{name_of_dir}/%(title)s.%(ext)s' --write-thumbnail --write-subs --sub-format 'srt' --sub-langs 'en,ru,ua' --download-archive archive.txt")
            if quality == '4':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=640][height<=480]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} -o '{name_of_dir}/%(title)s.%(ext)s' --write-thumbnail --write-subs --sub-format 'srt' --sub-langs 'en,ru,ua' --download-archive archive.txt")
            if quality == '5':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=1280][height<=720]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} -o '{name_of_dir}/%(title)s.%(ext)s' --write-thumbnail --write-subs --sub-format 'srt' --sub-langs 'en,ru,ua' --download-archive archive.txt")
            elif quality == '6':
                os.system(f"yt-dlp -f 'bestvideo[ext=mp4][width<=1920][height<=1080]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 {link} -o '{name_of_dir}/%(title)s.%(ext)s' --write-thumbnail --write-subs --sub-format 'srt' --sub-langs 'en,ru,ua' --download-archive archive.txt")
            else:
                print("Not correct answer!")
                exit()

        elif e_video_audio == 's':
            os.system(f"yt-dlp -f 'ba' -x --audio-format {ma} {link} -o '{name_of_dir}/%(title)s.%(ext)s' --write-thumbnail --write-subs --sub-format 'srt' --sub-langs 'en,ru,ua' --download-archive archive.txt")
        else:
            print("Not correct answer!")
            exit()

    print("successfully")
    exit()


def startac():
    link = input("Link to youtube video/playlist/channel: ")
        
    e_video_audio = input("(v)video & (s)sound?: ")
    name_of_ch = input("Name of channel file.txt: ")
    filesize = input("Set a max file size like - 10M or pass: ")
    
    
    if 'M' in filesize:
        if e_video_audio == 'v':
            os.system(f"yt-dlp -f '[filesize<={filesize}]' --merge-output-format mp4 --embed-thumbnail --embed-metadata --download-archive {name_of_ch} {link} -o '%(channel)s/%(title)s.%(ext)s'")
        elif e_video_audio == 's':
            os.system(f"yt-dlp -f ''[filesize<={filesize}]' -x --audio-format m4a --embed-thumbnail --embed-metadata --download-archive {name_of_ch} {link} -o '%(channel)s/%(title)s.%(ext)s'")
        else:
            print("Not correct answer!")

    else:
        if e_video_audio == 'v':
            quality = input("\n1 - 144p \n2 - 240p \n3 - 360p \n4 - 480p \n5 - 720p \n6 - 1080p"+"\nChoose quality: ")
            if quality == '1':
                os.system(f"yt-dlp -f 'bv*[ext=mp4][width<=256][height<=144]+ba' --merge-output-format mp4 --embed-thumbnail --embed-metadata --download-archive {name_of_ch} {link} -o '%(channel)s/%(title)s.%(ext)s'")
            if quality == '2':
                os.system(f"yt-dlp -f 'bv*[ext=mp4][width<=426][height<=240]+ba' --merge-output-format mp4 --embed-thumbnail --embed-metadata --download-archive {name_of_ch} {link} -o '%(channel)s/%(title)s.%(ext)s'")
            if quality == '3':
                os.system(f"yt-dlp -f 'bv*[ext=mp4][width<=480][height<=360]+ba' --merge-output-format mp4 --embed-thumbnail --embed-metadata --download-archive {name_of_ch} {link} -o '%(channel)s/%(title)s.%(ext)s'")
            if quality == '4':
                os.system(f"yt-dlp -f 'bv*[ext=mp4][width<=640][height<=480]+ba' --merge-output-format mp4 --embed-thumbnail --embed-metadata --download-archive {name_of_ch} {link} -o '%(channel)s/%(title)s.%(ext)s'")
            if quality == '5':
                os.system(f"yt-dlp -f 'bv*[ext=mp4][width<=1280][height<=720]+ba' --merge-output-format mp4 --embed-thumbnail --embed-metadata --download-archive {name_of_ch} {link} -o '%(channel)s/%(title)s.%(ext)s'")
            elif quality == '6':
                os.system(f"yt-dlp -f 'bv*[ext=mp4][width<=1920][height<=1080]+ba' --merge-output-format mp4 --embed-thumbnail --embed-metadata --download-archive {name_of_ch} {link} -o '%(channel)s/%(title)s.%(ext)s'")
            else:
                print("Not correct answer!")
                exit()
        elif e_video_audio == 's':
            os.system(f"yt-dlp -f 'ba' -x --audio-format m4a --embed-thumbnail --embed-metadata --download-archive {name_of_ch} {link} -o '%(channel)s/%(title)s.%(ext)s'")
        else:
            print("Not correct answer!")
            exit()
    print("successfully")
    exit()


def ifstartd():
    link = input("Link to youtube video/playlist/channel: ")
        
    if exists(descriptions_dir):
        pass
    if not exists(descriptions_dir):
            
# Make dir for descriptions
        os.mkdir(descriptions_dir)
# get info about video            
    with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(link, download=False)
        video_title = info_dict.get('title')
        video_title = (video_title+'.txt')
        video_descriptions = info_dict.get('description')

    readyforquotes = (descriptions_dir+'/'+video_title)
    readyforquotes1 = readyforquotes.replace("\\", "")
    readyforquotes2 = readyforquotes1.replace("/", "")
    readyforquotes3 = (f"'{readyforquotes2}'")
    video_title1 = video_title.replace("\\", "")
    video_title2 = video_title1.replace("/", "")

# Check if exists and move to descriptions folder
    print(readyforquotes3)
    if not exists(readyforquotes3):
        with open(video_title2, 'w') as txtdsk:
            txtdsk.write(video_descriptions)
        shutil.move(video_title2, descriptions_dir)
    else:
        print('file is exists, txt not created')
        exit()
    print("successfully")
    exit()


def starts():
    if exists(sortdirmp4):
        pass
    else:
        os.mkdir(sortdirmp4)
    if exists(sortdirm4a):
        pass
    else:
        os.mkdir(sortdirm4a)
        
    os.system(f"mv *.{mp} {sortdirmp4}")
    os.system(f"mv *.{ma} {sortdirm4a}")
    os.system("rm *.webm *.webp *.part")
    print("files has been successfully sorted!")
    exit()


def startp():
    link = input("Link to youtube video/playlist/channel: ")

    with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(link, download=False)
        thumbnail = info_dict.get('thumbnail')
        ydl.download([thumbnail])

if start == 'a':
    starta()
if start == 'd':
    ifstartd()
if start == 'ac':
    startac()
if start == 's':
    starts()
if start == 'm':
    startm()
elif start == 'p':
    startp()
else:
    ifstartenter()

"""
SHELL get description - os.system(f"yt-dlp --add-metadata --write-description {link}")

ради того, чтобы переменную link не показывало еслли выбираешь def starts или s,я поместил link и exit() вкаждый деф, а также отказался от while loop.
"""
