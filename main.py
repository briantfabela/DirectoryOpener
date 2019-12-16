# Python 3.7.1 - Briant J. Fabela 12/16/19
# WINDOWS ONLY - use subprocess library for cross OS solution

from os import startfile

def main():
    opendir(folder_paths)

def opendir(dirs):
    for directory in dirs:
        startfile(directory)

folder_paths = [ # put all the folder paths that you want to open here as list
    r"P:\ITS GIS\P&Z_Mapping", # location for mxd's
    r"N:\ZoningMapping\OFFICIAL_ZONING_ATLAS_FINAL" # location for pdf atlas
]

if __name__ == "__main__":
    main()