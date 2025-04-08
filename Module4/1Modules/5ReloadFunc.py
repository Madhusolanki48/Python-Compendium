print('Hello World !')
import sample

import importlib
import sample

importlib.reload(sample)

import importlib
import filechanges
def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass

for i in range(5):
    changes()
    input('Hit enter to reload...')
