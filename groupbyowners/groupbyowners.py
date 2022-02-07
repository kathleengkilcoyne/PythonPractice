def group_by_owners(files):
    v = {}

    for key, value in sorted(files.items()):
        v.setdefault(value, []).append(key)
    return v


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))