
from abc import ABC, abstractmethod
from mutagen.oggopus import OggOpus
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
import mutagen.mp3


def createFileObject(fileLocation):
    if fileLocation.endswith(".opus"):
        return OGGFile(fileLocation)
    elif fileLocation.endswith(".m4a") or fileLocation.endswith(".mp4"):
        return MP4File(fileLocation)
    elif fileLocation.endswith(".flac"):
        return FLACFile(fileLocation)
    elif fileLocation.endswith(".mp3"):
        return MP3File(fileLocation)
    else:
        return None



class SongFile(ABC):
    def getMetadataField(self, field):
        try:
            return self.file[field][0]
        except:
            return ""
    
    def setMetadataField(self, field, value):
        self.file[field] = value


    def getTitle(self):
        return self.getMetadataField("title")
    def setTitle(self, value):
        self.setMetadataField("title", value)

    def getArtist(self):
        return self.getMetadataField("artist")
    def setArtist(self, value):
        self.setMetadataField("artist", value)

    def getAlbum(self):
        return self.getMetadataField("album")
    def setAlbum(self, value):
        self.setMetadataField("album", value)

    def getDate(self):
        return self.getMetadataField("date")
    def setDate(self, value):
        self.setMetadataField("date", value)

    def getGenre(self):
        return self.getMetadataField("genre")
    def setGenre(self, value):
        self.setMetadataField("genre", value)

    def getComposer(self):
        return self.getMetadataField("composer")
    def setComposer(self, value):
        self.setMetadataField("composer", value)

    def getURL(self):
        return self.getMetadataField("purl")
    def setURL(self, value):
        self.setMetadataField("purl", value)

    def getDescription(self):
        return self.getMetadataField("description")
    def setDescription(self, value):
        self.setMetadataField("description", value)

    def getComment(self):
        return self.getMetadataField("comment")
    def setComment(self, value):
        self.setMetadataField("comment", value)

    def getAllFileMetadata(self):
        return self.file.pprint()

    def saveMetadata(self):
        self.file.save()
    


class OGGFile(SongFile):
    def __init__(self, fileLocation):
        self.file = OggOpus(fileLocation)

class FLACFile(SongFile):
    def __init__(self, fileLocation):
        self.file = FLAC(fileLocation)
    
    def getURL(self):
        return self.getMetadataField("url")
    def setURL(self, value):
        self.setMetadataField("url", value)

class MP3File(SongFile):
    def __init__(self, fileLocation):
        self.file = MP3(fileLocation)

    def getTitle(self):
        return self.getMetadataField("TIT2")
    def setTitle(self, value):
        self.setMetadataField("TIT2", value)

    def getArtist(self):
        return self.getMetadataField("TPE1")
    def setArtist(self, value):
        self.setMetadataField("TPE1", value)

    def getAlbum(self):
        return self.getMetadataField("TALB")
    def setAlbum(self, value):
        self.setMetadataField("TALB", value)

    def getDate(self):
        return str(self.getMetadataField("TDRC"))
    def setDate(self, value):
        self.setMetadataField("TDRC", value)

    def getGenre(self):
        return self.getMetadataField("TCON")
    def setGenre(self, value):
        self.setMetadataField("TCON", value)

    def getComposer(self):
        return self.getMetadataField("TCOM")
    def setComposer(self, value):
        self.setMetadataField("TCOM", value)

#TODO Investigate URL and Comment not showing
    def getURL(self):
        return self.getMetadataField("WXXX")
    def setURL(self, value):
        self.setMetadataField("WXXX", value)

    def getDescription(self):
        return self.getMetadataField("TIT1")
    def setDescription(self, value):
        self.setMetadataField("TIT1", value)

    def getComment(self):
        return self.getMetadataField("COMM")
    def setComment(self, value):
        self.setMetadataField("COMM", value)

class MP4File(SongFile):
    def __init__(self, fileLocation):
        self.file = MP4(fileLocation)

    def getTitle(self):
        return self.getMetadataField("\xa9nam")
    def setTitle(self, value):
        self.setMetadataField("\xa9nam", value)

    def getArtist(self):
        return self.getMetadataField("\xa9ART")
    def setArtist(self, value):
        self.setMetadataField("\xa9ART", value)

    def getAlbum(self):
        return self.getMetadataField("\xa9alb")
    def setAlbum(self, value):
        self.setMetadataField("\xa9alb", value)

    def getDate(self):
        return self.getMetadataField("\xa9day")
    def setDate(self, value):
        self.setMetadataField("\xa9day", value)

    def getGenre(self):
        return self.getMetadataField("\xa9gen")
    def setGenre(self, value):
        self.setMetadataField("\xa9gen", value)

    def getComposer(self):
        return self.getMetadataField("\xa9wrt")
    def setComposer(self, value):
        self.setMetadataField("\xa9wrt", value)

    def getURL(self):
        return self.getMetadataField("purl")
    def setURL(self, value):
        self.setMetadataField("purl", value)

    def getDescription(self):
        return self.getMetadataField("desc")
    def setDescription(self, value):
        self.setMetadataField("desc", value)

    def getComment(self):
        return self.getMetadataField("\xa9cmt")
    def setComment(self, value):
        self.setMetadataField("\xa9cmt", value)

