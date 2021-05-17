
import piexif
from exif import Image

image_path = "/Users/iqbal/Dev/Python Scripts/img.jpg"

with open("/Users/iqbal/Dev/Python Scripts/img.jpg", 'rb') as imageFile: 
    imageFile = Image(imageFile)

if imageFile.has_exif:
    print("Got data")

    # loading the image
    imageDict = piexif.load(image_path)

    # extract thumbnail data
    thumbnail = imageDict.pop('thumbnail')
    if thumbnail is not None:
        with open('thumbnail.jpg', 'wb') as f:
            f.write(thumbnail)


    def printData():
        
        # getting rest of the data
        for ifd in imageDict:
            for tag in imageDict[ifd]:
                tagName = piexif.TAGS[ifd][tag]["name"]
                tagValue = imageDict[ifd][tag]
                print(f'\t{tagName:25}: {tagValue}')


    printData()

    # # removing DateTime tag from extracted data
    # imageDict['0th'].pop(piexif.ImageIFD.DateTime)

    # # saving the updated data in the same image
    # modifiedDict = piexif.dump(imageDict)
    # piexif.insert(modifiedDict, image_path)

    # # print the data from the image again to verify the removal of 'DateTime' tag from '0th'
    # printData()
else:
    print("No Metadata in the image.")

