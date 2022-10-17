# futtatáskor minden sort futtat ami indentation level 0 szinten van

def func():
    print("FUNC() in one.py ")

print("Top level in one.py")

if __name__ == "__main__":
    # RUN THE SCRIPT
    print("one.py is being run directly!")
else:
    print("one.py has been imported")   