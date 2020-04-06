import sys
import os


# (sys.path.insert(1, os.path.dirname(__file__)))
# sys.path.insert(2, '/Users/peeyushsingla/projects/learning_pandas/pandas_udemy_bootcamp/utilities')
# print(sys.path)
# print(os.path.dirname(__file__))

# print(os.listdir(path="pandas_udemy_bootcamp"))

# d = "pandas_udemy_bootcamp"
# def listdir_fullpath(d):
#     print([os.path.join(d, f) for f in os.listdir(d)])

# print((listdir_fullpath(d)))

# for dirname, dirnames, filenames in os.walk('pandas_udemy_bootcamp/src'):
#     # print path to all subdirectories first.
#     for subdirname in dirnames:
#         if subdirname != '.git':
#             print(os.path.join(dirname, subdirname))

path = 'pandas_udemy_bootcamp/src'
# pwd = os.path.dirname(__file__)
# print(pwd)
# def scan_dir(path):
#     print(list(map(os.path.abspath, os.listdir(pwd))))

# scan_dir(path)
dir_list = []

with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and not entry.name.endswith('.py'):
            dir_list.append(os.path.abspath(path) + "/" + entry.name)
            # print(entry.name)
    print(dir_list)        
    # print(list(map(os.path.abspath(path), )))

# print(os.path.abspath(path))

print(sys.path)
# print("\n")
print("\n")

for n in range(0, (len(dir_list))):
    sys.path.insert(n, dir_list[n])
print(sys.path)