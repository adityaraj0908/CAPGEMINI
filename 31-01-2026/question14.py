n = int(input())

if n == 0:
    print(-1)
else:
    files = input().split()
    max_version = -1

    for file in files:
        if file.startswith("File_"):
            part = file.split("_")
            if part[1].isdigit():
                version = int(part[1])
                if version > max_version:
                    max_version = version

    print(max_version)
