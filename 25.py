def copy_file(src_file, dest_file):
    try:
        with open(src_file, 'r') as src:
            with open(dest_file, 'w') as dest:
                dest.write(src.read())
        print(f"Contents of {src_file} copied to {dest_file}")
    except FileNotFoundError:
        print(f"Error: {src_file} not found")
    except IOError:
        print(f"Error: Unable to read or write to file")

src_file = "source.txt"
dest_file = "destination.txt"

copy_file(src_file, dest_file)