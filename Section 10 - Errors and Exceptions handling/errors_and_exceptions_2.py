try:
    f = open("testfile.txt", 'r') # OSError with mode='r'
    f.write("This is a test lien")
except TypeError:
    print("There was a TypeError")
except OSError:
    print("Hey, you have an OSError")
except:
    print("All other exceptions")
finally:
    print("I always run")

#################################################

def ask_for_int():

    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("That's not a number!")
            continue
        else:
            print("Yes, this is a number!")
            break
        finally:
            print("End of try-except-finally")
            print("I will always run at the and")
            print("\nI'm going to ask you again!")

ask_for_int()