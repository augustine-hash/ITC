import sys

def jerkins():
    print("Jenkins Test Script Runnin...")
    print("Python version: ", sys.version)
    print("This is successful")
    return 0

if __name__ == "_jerkins_":
    exit(jerkins())