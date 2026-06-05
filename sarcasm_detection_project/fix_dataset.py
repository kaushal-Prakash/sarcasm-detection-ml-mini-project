import json

input_file = "dataset/sarcasm_dataset.json"
output_file = "dataset/fixed_dataset.json"

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        line = line.strip() # Remove leading/trailing whitespace

        # remove trailing comma if exists
        if line.endswith(","):
            line = line[:-1]

        # skip empty lines or brackets
        if line in ["[", "]", ""]:
            continue

        try:
            obj = json.loads(line)
            f_out.write(json.dumps(obj) + "\n")
        except:
            continue

print("✅ Fixed dataset created!")