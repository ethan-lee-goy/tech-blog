import json

file_path = "/Users/ethan/Documents/workspace/tech-blog/reinforcement-learning/01_第一部分_基础理论/ch02_马尔可夫决策过程.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb.get("cells", []):
    if cell.get("cell_type") == "markdown":
        new_source = []
        for line in cell.get("source", []):
            # Fix smart quotes in math formulas
            new_line = line.replace("s’", "s'")
            # Fix stray \n after formula
            new_line = new_line.replace("$$ \\n\n", "$$\n")
            # Fix \\\vdots to \\ \vdots for better latex rendering
            new_line = new_line.replace("\\\\\\vdots", "\\\\ \\vdots")
            new_source.append(new_line)
        cell["source"] = new_source

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write('\n')
