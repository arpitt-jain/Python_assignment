def check_prefix_suffix(string, prefix, suffix):
    if string.startswith(prefix):
        print(f"The string '{string}' starts with the prefix '{prefix}'")
    else:
        print(f"The string '{string}' does not start with the prefix '{prefix}'")

    if string.endswith(suffix):
        print(f"The string '{string}' ends with the suffix '{suffix}'")
    else:
        print(f"The string '{string}' does not end with the suffix '{suffix}'")


string = "hello_world"
prefix = "hello"
suffix = "_world"

check_prefix_suffix(string, prefix, suffix)