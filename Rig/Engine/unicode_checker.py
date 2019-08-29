from FSGate import swallow_file, dump_in_file
from sys import argv
from os.path import splitext
from chardet import UniversalDetector
from codecs import encode, decode

def convert_to_Unicode(text, possible_codec):
    return (encode(decode(text, possible_codec), 'utf-8'))

def check_unicode(contents, contents_name="This"):
    detector = UniversalDetector()
    for line in contents.split(b'\n'):
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    if detector.result['encoding'] != 'utf-8' and detector.result['encoding'] != 'ascii':
        print(contents_name + " is not Unicode!\nIt's detected as " + detector.result['encoding'] + " with a confidence degree of " + str(detector.result['confidence'] * 100) + '%.')
        return detector.result['encoding']
    return 'utf-8'

if __name__ == '__main__':
    for i in argv[1:]:
        contents = swallow_file(i)
        encoding = check_unicode(contents, i)
        if encoding != 'utf-8':
            recoded = convert_to_Unicode(contents, encoding)
            check_unicode(recoded)
            new_name = splitext(i)[0] + '_U' + splitext(i)[1]
            dump_in_file(new_name, recoded, byte_text=True)