from pathlib import Path

filename = input("Enter file name: ").strip()
extension = Path(filename).suffix

if extension:
    print("Extension:", extension[1:])
else:
    print("The file has no extension.")
