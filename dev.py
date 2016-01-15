import os
import tidbits

USE_TYPES = ['txt']

for (dirpath, dirnames, filenames) in os.walk('/Users/fl/Data'):
    for filename in filenames:
        if filename in ['normalized.txt', 'README.txt', 'requirements.txt']:
            continue
        filepath = os.path.join(dirpath, filename)
        _, ext = os.path.splitext(filepath)
        ext = ext.replace('.', '').lower().strip()
        if ext not in USE_TYPES:
            continue

        with open(filepath, 'r') as fh:
            text = fh.read()
        if len(text.strip()) < 10:
            continue

        print filepath, len(text)
        for tb in tidbits.scan(text):
            print '  -> ', tb
