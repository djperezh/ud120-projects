
#!/usr/bin/python


def dos2unix(original = "", destination = ""):
    """
    convert dos linefeeds (crlf) to unix (lf)
    usage: dos2unix.py 
    """

    original = "../final_project/final_project_dataset.pkl"
    destination = "../final_project/final_project_dataset_unix.pkl"

    # original = "../tools/python2_lesson06_keys.pkl"
    # destination = "../tools/python2_lesson06_keys_unix.pkl"

    content = ''
    outsize = 0
    with open(original, 'rb') as infile:
        content = infile.read()
    with open(destination, 'wb') as output:
        for line in content.splitlines():
            outsize += len(line) + 1
            output.write(line + str.encode('\n'))

    print("Done. Saved %s bytes." % (len(content)-outsize))