import json
import os
import shutil
import time
from datetime import datetime
from time import gmtime, strftime

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'harsh':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        if extension == '':
                            continue
                        else:
                            extension = 'noname'

                    folder_destination_path = extensions_folders[extension]
                    folder_destination_path = folder_destination_path + "/" 


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)


folder_to_track = '/Users/harsh/Downloads'
folder_destination = '/Users/harsh/Downloads'

extensions_folders = {
#No name
    'noname' : "/Users/harsh/Downloads/Miscellaneous",
#Text
    '.txt'    : "/Users/harsh/Downloads/Text",
    '.doc'    : "/Users/harsh/Downloads/Text",
    '.docx'   : "/Users/harsh/Downloads/Text",
    '.odt '   : "/Users/harsh/Downloads/Text",
    '.pdf'    : "/Users/harsh/Downloads/Text",
    '.rtf'    : "/Users/harsh/Downloads/Text",
    '.tex'    : "/Users/harsh/Downloads/Text",
    '.wks '   : "/Users/harsh/Downloads/Text",
    '.wps'    : "/Users/harsh/Downloads/Text",
    '.wpd'    : "/Users/harsh/Downloads/Text",
# Video
    '.3g2'    : "/Users/harsh/Downloads/Media",
    '.3gp'    : "/Users/harsh/Downloads/Media",
    '.avi'    : "/Users/harsh/Downloads/Media",
    '.flv'    : "/Users/harsh/Downloads/Media",
    '.h264'   : "/Users/harsh/Downloads/Media",
    '.m4v'    : "/Users/harsh/Downloads/Media",
    '.mkv'    : "/Users/harsh/Downloads/Media",
    '.mov'    : "/Users/harsh/Downloads/Media",
    '.mp4'    : "/Users/harsh/Downloads/Media",
    '.mpg'    : "/Users/harsh/Downloads/Media",
    '.mpeg'   : "/Users/harsh/Downloads/Media",
    '.rm'     : "/Users/harsh/Downloads/Media",
    '.swf'    : "/Users/harsh/Downloads/Media",
    '.vob'    : "/Users/harsh/Downloads/Media",
    '.wmv'    : "/Users/harsh/Downloads/Media",
#Images
    '.ai'     : "/Users/harsh/Downloads/Images",
    '.bmp'    : "/Users/harsh/Downloads/Images",
    '.gif'    : "/Users/harsh/Downloads/Images",
    '.ico'    : "/Users/harsh/Downloads/Images",
    '.jpg'    : "/Users/harsh/Downloads/Images",
    '.jpeg'   : "/Users/harsh/Downloads/Images",
    '.png'    : "/Users/harsh/Downloads/Images",
    '.ps'     : "/Users/harsh/Downloads/Images",
    '.psd'    : "/Users/harsh/Downloads/Images",
    '.svg'    : "/Users/harsh/Downloads/Images",
    '.tif'    : "/Users/harsh/Downloads/Images",
    '.tiff'   : "/Users/harsh/Downloads/Images",
    '.CR2'    : "/Users/harsh/Downloads/Images",
#Compressed
    '.7z'   : "/Users/harsh/Downloads/Compressed",
    '.arj'  : "/Users/harsh/Downloads/Compressed",
    '.deb'  : "/Users/harsh/Downloads/Compressed",
    '.pkg'  : "/Users/harsh/Downloads/Compressed",
    '.rar'  : "/Users/harsh/Downloads/Compressed",
    '.rpm'  : "/Users/harsh/Downloads/Compressed",
    '.tar.gz': "/Users/harsh/Downloads/Compressed",
    '.z'    : "/Users/harsh/Downloads/Compressed",
    '.zip'  : "/Users/harsh/Downloads/Compressed",
#Disc
    '.bin'  : "/Users/harsh/Downloads/Compressed",
    '.dmg'  : "/Users/harsh/Downloads/Compressed",
    '.iso'  : "/Users/harsh/Downloads/Compressed",
    '.toast': "/Users/harsh/Downloads/Compressed",
    '.vcd'  : "/Users/harsh/Downloads/Compressed",
#Presentations
    '.key': "/Users/harsh/Downloads/Presentations",
    '.odp': "/Users/harsh/Downloads/Presentations",
    '.pps': "/Users/harsh/Downloads/Presentations",
    '.ppt': "/Users/harsh/Downloads/Presentations",
    '.pptx': "/Users/harsh/Downloads/Presentations",
#Programming
    '.c'    : "/Users/harsh/Downloads/Programming",
    '.class': "/Users/harsh/Downloads/Programming",
    '.dart' : "/Users/harsh/Downloads/Programming",
    '.py'   : "/Users/harsh/Downloads/Programming",
    '.sh'   : "/Users/harsh/Downloads/Programming",
    '.swift': "/Users/harsh/Downloads/Programming",
    '.html' : "/Users/harsh/Downloads/Programming",
    '.xml' : "/Users/harsh/Downloads/Programming",
    '.json' : "/Users/harsh/Downloads/Programming",
    '.h'    : "/Users/harsh/Downloads/Programming",
#Spreadsheets
    '.ods' : "/Users/harsh/Downloads/Excel",
    '.xlr' : "/Users/harsh/Downloads/Excel",
    '.xls' : "/Users/harsh/Downloads/Excel",
    '.csv' : "/Users/harsh/Downloads/Excel",
    '.xlsx': "/Users/harsh/Downloads/Excel",
#System
    '.bak' : "/Users/harsh/Downloads/System",
    '.cab' : "/Users/harsh/Downloads/System",
    '.cfg' : "/Users/harsh/Downloads/System",
    '.cpl' : "/Users/harsh/Downloads/System",
    '.cur' : "/Users/harsh/Downloads/System",
    '.dll' : "/Users/harsh/Downloads/System",
    '.dmp' : "/Users/harsh/Downloads/System",
    '.drv' : "/Users/harsh/Downloads/System",
    '.icns': "/Users/harsh/Downloads/System",
    '.ico' : "/Users/harsh/Downloads/System",
    '.ini' : "/Users/harsh/Downloads/System",
    '.lnk' : "/Users/harsh/Downloads/System",
    '.msi' : "/Users/harsh/Downloads/System",
    '.sys' : "/Users/harsh/Downloads/System",
    '.tmp' : "/Users/harsh/Downloads/System",
}
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
