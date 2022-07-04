import os, sys
import shutil


name = sys.argv[1]
TEMP_PATH = sys.argv[2]
source_dir = os.path.join(TEMP_PATH, name)

if __name__ == '__main__':
    os.chdir(TEMP_PATH)
    os.system(f'npx --yes react-native init {name} --template react-native-template-typescript')
    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), TEMP_PATH)
    shutil.rmtree(source_dir, ignore_errors=True)

