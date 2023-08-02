
from abc import ABC, abstractmethod
from mutagen.oggopus import OggOpus
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3, TXXX


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
    
    def getMetadataFieldNumber(self, field):
        try:
            number = self.getMetadataField(field)
            return 0 if number == "" else int(number)
        except:
            return 0
    
    def setMetadataField(self, field, value):
        self.file[field] = value


    def getTrackNumberCurrent(self):
        return self.getMetadataFieldNumber("tracknumber")
    def setTrackNumberCurrent(self, value):
        self.setMetadataField("tracknumber", str(value))
    
    def getTrackNumberMaximum(self):
        return self.getMetadataFieldNumber("tracktotal")
    def setTrackNumberMaximum(self, value):
        self.setMetadataField("tracktotal", str(value))
    
    def getDiskNumberCurrent(self):
        return self.getMetadataFieldNumber("discnumber")
    def setDiskNumberCurrent(self, value):
        self.setMetadataField("discnumber", str(value))
    
    def getDiskNumberMaximum(self):
        return self.getMetadataFieldNumber("disctotal")
    def setDiskNumberMaximum(self, value):
        self.setMetadataField("disctotal", str(value))

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

    def getReplayGain(self):
        try:
            replayGain = self.getMetadataField("replaygain_track_gain")
            return 0 if replayGain == "" else self.convertReplayGainToFloat(replayGain)
        except:
            return 0
    def setReplayGain(self, value):
        self.setMetadataField("replaygain_track_gain", self.convertFloatToReplayGain(value))
    def convertReplayGainToFloat(self, value):
        return float(value.split()[0])
    def convertFloatToReplayGain(self, value):
        # https://stackoverflow.com/questions/6149006/how-to-display-a-float-with-two-decimal-places
        return "%.2f" % value + " dB"

    def getComment(self):
        return self.getMetadataField("comment")
    def setComment(self, value):
        self.setMetadataField("comment", value)

    def getDescription(self):
        return self.getMetadataField("description")
    def setDescription(self, value):
        self.setMetadataField("description", value)

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
        self.file = ID3(fileLocation)

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
        frames = self.file.getall("WXXX")
        for frame in frames:
            if frame.url:
                return frame.url
        return ""
    def setURL(self, value):
        self.setMetadataField("WXXX", value)

    def getReplayGain(self):
        # https://stackoverflow.com/questions/4040605/does-anyone-have-good-examples-of-using-mutagen-to-write-to-files
        # https://mutagen.readthedocs.io/en/latest/user/id3.html
        frames = self.file.getall("TXXX")
        for frame in frames:
            if frame.desc == "replaygain_track_gain":
                return self.convertReplayGainToFloat(frame.text[0])
        return 0.00
    def setReplayGain(self, value):
        self.setMetadataField("TXXX=replaygain_track_gain", self.convertFloatToReplayGain(value))

    def getComment(self):
        return self.getMetadataField("COMM")
    def setComment(self, value):
        self.setMetadataField("COMM", value)

    def getDescription(self):
        return self.getMetadataField("TIT1")
    def setDescription(self, value):
        self.setMetadataField("TIT1", value)


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

