import os
import datetime
import re
import shutil
import sys

# Customize any skipped folders or files below
excluded_folders = ['TORRENTS', 'DLKEEPS', 'OLDHD']
excluded_files = ['de_dup.py','mv_dls.py','mv_dls.exe','.crdownload']

# Manually set the default directory for the script below
# example: default_directory = 'C:\\Users\\s3711\\Downloads'
default_directory = ''

if default_directory == '':
    default_directory = os.path.dirname(os.path.realpath(sys.argv[0]))

os.chdir(default_directory)
print("This is going to move a lot of things, be sure the directory below is correct:")
print(default_directory)
print("\nEnter y to continue, or ctrl + c to exit")
while input() != 'y':
    print("\nEnter y to continue, or ctrl + c to exit")

moved = 0
created = 0
skipped = 0
skipped_files = []
skipped_f = 0
skipped_folders = []
failed = 0
failed_files = []
file_list = os.listdir(default_directory)

for f in file_list:
    fcd = datetime.datetime.fromtimestamp(os.path.getmtime(f)).strftime('%m.%d.%Y')

    if datetime.datetime.now().date().strftime('%m.%d.%Y') == fcd:
        continue
    elif re.match(r'\d\d\.\d\d\.\d\d\d\d', f) != None:
        continue
    elif os.path.isfile(f) and f in excluded_files:
        skipped += 1
        skipped_files.append(f)
        continue
    elif os.path.isdir(f) and f in excluded_folders:
        skipped_f +=1
        skipped_folders.append(f)
        continue
    else:
        try:
            if not os.path.exists(fcd):
                os.mkdir(fcd)
                created += 1
            shutil.move(f,str(fcd +'\\'))
            moved += 1
        except shutil.Error as e:
            failed +=1
            failed_files.append(f)
            continue
print(f"DIRECTORIES CREATED: {created}")
print(f"FILES MOVED: {moved}")
print(f"FILES SKIPPED: {skipped}")
for f in skipped_files:
    print(f"    {f}")
print(f"\nDIRECTORIES SKIPPED: {skipped_f}")
for d in skipped_folders:
    print(f"    {d}")
print(f"\nFILES FAILED: {failed}")
for f in failed_files:
    print(f"    {f}")
input("\nPress Any Key")
            



