with open("countup.json", "r") as f:
    import json

    entries = json.loads(f.read())

    for k, v in entries.items():
        print(f"- x{v} `{k}`")