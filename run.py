from pathlib import Path
import sys, main, converter

folder = Path('./photos_input')

count_all = len(list(folder.glob("*.heic")))
count = 1

for pathFile in folder.glob('*.heic'):
    converter.heic_to_jpg(pathFile, count_all, count)
    count += 1


count_all = len(list(folder.glob("*.jpg"))) + len(list(folder.glob("*.jpeg"))) + len(list(folder.glob("*.png")))
count = 1

for pathFile in folder.glob('*.jpg'):
    main.main(pathFile, count_all, count, True)
    count += 1

for pathFile in folder.glob('*.jpeg'):
    main.main(pathFile, count_all, count, True)
    count += 1

for pathFile in folder.glob('*.png'):
    main.main(pathFile, count_all, count, True)
    count += 1

sys.exit("Finish!")