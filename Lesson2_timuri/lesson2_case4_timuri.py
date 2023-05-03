path = r"""C:\Users\Mister X\Desktop\L.D. Nero - I'm Burning (Slowed).mp3"""
path_folder = path.split('\\')[-2]
path_disk = path.split('\\')[0]
path_file = path.split('\\')[-1]

print('Имя файла - ', path_file[:path_file.rfind('.')])
print('Имя диска - ', path_disk[0:-1])
print('Имя папки - ', path_folder)
