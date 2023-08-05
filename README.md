# music-metadata-editor
Python Music Metadata Editor

# Dependancies

pip install pyqt5 pyqt5-tools

QT Designer Location
C:\Users\ [YOUR USER] \AppData\Local\Programs\Python\Python38-32\Lib\site-packages\qt5_applications\Qt\bin

# TODO
    - ✓ Add Replay Gain Functionality
    - ✓ Add track and disk functionality
    - ✓ Figure out MP3 fields not showing
    - Remove data from form when everything is deselected
    - Bold changed fields' names
    - (FLAC) Perhaps add PURL and URL different fields because YTDL stores them as PURL, but AIMP stores them as URL
    - Add Try Catch to Set Metadata Fields
    - ✓ Fix Encoding, remove it from the object creations because it's probably not needed
    - Test all file types and ensure data is being read/saved correctly. Try emptying/deleting the fields with AIMP as well.
        - ✓ FLAC
        - OGG
        - MP4
        - M4A
        - ✓ MP3
    - Popup dialog when saving changes. Ask the user if they're okay with it, and show list of songs
    - Clean up project comments/spacing/imports etc.
    - Write down tutorial in README for compiling the .ui file and such