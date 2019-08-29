def README():
    print(open('README.md').read())

def start(here, settingsFile):
    print("Starting Text Interface in " + here + " with " + settingsFile + " for Settings.")

def fusion_files(keysFile, valuesFile):
    print("The keys from " + keysFile + " are being fused with the values from " + valuesFile + ".")

def test_files_xsd(target, xsd):
    print("The " + target + " XML has been succesfully tested against the " + xsd + "XSD. No errors were found.")
