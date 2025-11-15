"""
Simple helper to inspect flagged examples produced by the Gradio app.

Usage:
    python review_flags.py

What it does:
- Lists files and subfolders under `flagged/`.
- Prints the first few lines of any CSV, JSON, or JSONL files it finds.
- Prints image file paths that were saved as part of flagged examples.
"""
from pathlib import Path
import json
import csv

FLAG_DIR = Path(__file__).parent / "flagged"

if not FLAG_DIR.exists():
    print("No flagged folder found (no examples have been flagged yet).")
    raise SystemExit(0)

print(f"Inspecting flagged folder: {FLAG_DIR}\n")

files = list(FLAG_DIR.rglob("*"))
if not files:
    print("Flagged folder is empty.")
    raise SystemExit(0)

# Group by extension
by_ext = {}
for p in files:
    if p.is_dir():
        continue
    ext = p.suffix.lower()
    by_ext.setdefault(ext, []).append(p)

# Print summary
print("Summary:")
for ext, paths in by_ext.items():
    print(f" - {ext or '[no-ext]'}: {len(paths)} files")
print()

# Helper to print head of text files
def print_head(path, n=10):
    print(f"--- {path} ---")
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"Could not read: {e}\n")
        return
    lines = text.splitlines()
    for i, L in enumerate(lines[:n], start=1):
        print(f"{i:3}: {L}")
    if len(lines) > n:
        print(f"... ({len(lines)-n} more lines)\n")
    else:
        print()

# Show CSVs
for p in by_ext.get('.csv', []):
    print_head(p)

# Show JSON / JSONL
for p in by_ext.get('.json', []) + by_ext.get('.jsonl', []):
    # Try to pretty-print first object
    print(f"--- {p} ---")
    try:
        text = p.read_text(encoding="utf-8", errors="replace").strip()
        if not text:
            print("(empty)\n")
            continue
        # JSONL can be multiple JSON objects per line
        if '\n' in text and text.count('\n') >= 1 and text.lstrip().startswith('{'):
            # treat as jsonl
            lines = text.splitlines()
            print(f"(JSONL with {len(lines)} entries) — first entry:")
            print(json.dumps(json.loads(lines[0]), indent=2))
            print()
        else:
            obj = json.loads(text)
            print(json.dumps(obj, indent=2))
            print()
    except Exception as e:
        print(f"Could not parse JSON: {e}\n")

# List image-like files
image_exts = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
images = []
for ext in image_exts:
    images.extend(by_ext.get(ext, []))

if images:
    print(f"Found {len(images)} image files saved with flagged examples. Paths:")
    for p in images:
        print(f" - {p}")
    print()

print("Done. To inspect an example in detail, open the files shown above (images) and check the associated JSON/CSV entries for inputs/outputs/flag_reason.")
