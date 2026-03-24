"""
WSI to DICOM Converter

Converts Whole Slide Images (SVS, MRXS, MIRAX) to DICOM WSI format
using wsidicomizer.

Author: Solmaz Haddady
Affiliation: Johannes Kepler University Linz (JKU), Austria
"""

import os
import subprocess
from pathlib import Path

# =========================
# CONFIGURATION
# =========================

INPUT_FOLDER = Path("input_wsi")
OUTPUT_FOLDER = Path("output_dicom")
METADATA_FOLDER = None  # Set to Path("/path/to/metadata_json") if used

SUPPORTED_EXTENSIONS = [".svs", ".mrxs", ".mirax"]

# =========================
# INITIALIZATION
# =========================

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# =========================
# CONVERSION FUNCTION
# =========================

def convert_slide(slide_path: Path):
    slide_id = slide_path.stem
    output_path = OUTPUT_FOLDER / slide_id

    # Skip already converted slides
    if output_path.exists() and any(output_path.iterdir()):
        print(f"[SKIP] {slide_path.name} already converted.")
        return

    print(f"[CONVERT] {slide_path.name}")

    cmd = [
        "wsidicomizer",
        "-i", str(slide_path),
        "-o", str(output_path),
        "--format", "jpeg",
        "--no-label",
        "--no-overview",
    ]

    ## Optional metadata
    if METADATA_FOLDER:
        metadata_file = METADATA_FOLDER / f"{slide_id}.json"
        if metadata_file.exists():
            cmd.extend(["--metadata", str(metadata_file)])
        else:
            print(f"[INFO] No metadata JSON for {slide_id}")

    try:
        subprocess.run(cmd, check=True)
        print(f"[DONE] {slide_path.name}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to convert {slide_path.name}: {e}")

# =========================
# MAIN EXECUTION
# =========================

if __name__ == "__main__":
    for file in INPUT_FOLDER.iterdir():
        if file.suffix.lower() in SUPPORTED_EXTENSIONS:
            convert_slide(file)

    print("Conversion process completed.")
