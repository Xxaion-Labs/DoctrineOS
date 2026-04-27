import os

required = ["# Node:", "## Definition", "## Usage", "## Example", "## ID"]

for f in os.listdir("nodes"):
    if f.endswith(".md"):
        c = open("nodes/"+f, encoding="utf-8").read()
        for r in required:
            if r not in c:
                print("FAIL", f, r)
                exit(1)

print("OK")
