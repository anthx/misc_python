import os, time
from tkinter import filedialog, Tk
from shutil import make_archive
root = Tk()

# Uses some code examples from:
# http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html


def get_path_to_watch():
    path = filedialog.askdirectory()
    root.update()
    return str(path)


def get_zip_name():
    _zip = filedialog.asksaveasfilename()
    if _zip[-4:] == ".zip":
        _zip = _zip[:-4]
    root.destroy()
    return _zip

path_to_watch = get_path_to_watch()
zip_file_name = get_zip_name()
print(path_to_watch)


def make_zip():
    make_archive(zip_file_name, 'zip', path_to_watch)

before = {}
for f in os.listdir(path_to_watch):
    before[f] = os.stat(os.path.join(path_to_watch, f)).st_mtime

print(before)
while 1:
    time.sleep(5)
    after = dict([(f, os.stat(os.path.join(path_to_watch, f)).st_mtime) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    modified = [f for f in after if before[f] != after[f]]
    if added: print("Added: ", ", ".join(added))
    if removed: print("Removed: ", ", ".join(removed))
    if modified: print("Modified: ", ", ".join(modified))
    if added or removed or modified:
        make_zip()
    before = after