from pathlib import Path

for f in Path(".").iterdir():
    print(f)

    Path("nuevo1.txt").write_text("hola")

    print(Path("nuevo1.txt").exists)

