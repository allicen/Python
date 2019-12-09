import os
import os.path

paths = set()

os.listdir('path')
for current_dir, dirs, files in os.walk('.'):
    for file in files:
        if file[-3:] == '.py':
            paths.add(current_dir)

listPath = list(paths)
listPath.sort()
result = ''

for path in listPath:
    result += path
    result += '\n'


print(result.replace('.\\path\\', 'main\\').replace('.\path', 'main').replace('.\n', ''))
