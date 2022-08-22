def file_read():
    file_for_reading = None
    try:
        file_for_reading = open("resources/file_read_write.txt", "r")
        print("read() demo: " + file_for_reading.read())

        #print("readline() demo: " + file_for_reading.readline())

        #print("readlines() demo, printing line by line: ")
        #lines = file_for_reading.readlines()
        #for line in lines:
        #    print(line)

    except FileNotFoundError as fne:
        print("error encountered while reading the file" + str(fne))
    finally:
        file_for_reading.close()


def file_write():
    file_for_writing = None
    try:
        file_for_writing = open("resources/file_write.txt", "w")
        file_for_writing.write("\n Toby - Human Resources")
    except FileNotFoundError as fne:
        print("Error trying to open file for writing: " + str(fne))
    finally:
        file_for_writing.close()

file_read()
file_write()
