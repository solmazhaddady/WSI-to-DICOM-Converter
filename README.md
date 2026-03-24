# WSI-to-DICOM-Converter
Convert whole slide images (SVS, MRXS) to DICOM format for computational pathology 
### WSI to DICOM Converter

This repository provides a Python-based workflow to convert **Whole Slide Images (WSIs)** from proprietary formats (`.svs`, `.mrxs`, `.mirax`) into **Digital Imaging and Communications in Medicine (DICOM)** format using the open-source tool `wsidicomizer`.

This conversion enables standardized storage, interoperability, and compatibility with DICOM-based viewers and medical AI pipelines.

---

## Motivation

Whole slide images are typically stored in vendor-specific formats that are not fully interoperable. Converting WSIs to DICOM allows:

- Standardized data representation  
- Integration with clinical imaging systems  
- Improved reproducibility in research
- Decrease computational cost 
- Compatibility with large-scale archives such as TCIA  

---

## Features

- Supports `.svs`, `.mrxs`, and `.mirax` formats  
- Batch processing of multiple slides  
- Skips already converted slides  
- Generates DICOM-compliant tiled output  
- Optional per-slide JSON metadata integration  
- Preserves native resolution and pyramid structure  

---

## Requirements

Install dependencies:

*bash
pip install wsidicomizer[openslide]

also ensure:
- OpenSlide is installed.
- Python 3.8 or higher recommended .


## Input and Output structure

### Input Folder : 
Folder contains WSI files : .svs , .mrxs , .mirax files 

### Output Folder :
Each slide will generate its own DICOM subfolder with DCOM **.dcm ** tiles :
- .........0.dcm
- .........1.dcm
- .........2.dcm
.
.
.

## Optional Metadata Support(JSON)
you may optionally provide a** metadata ** folder with one JSON file per slide , these will be passed to** wsidicomizer** via **--metadata flag **.

## Conversion Parameters
The script uses :

- JPEG tile encoding
- No label image (--no-label)
- No overview image (--no-overview)
- Native resolution preserved

## Usage 
Update input/output paths in the script and run :

python convert_wsi_to_dicom.py

## Author 
Solmaz Haddady

Johannes Kepler University Linz (JKU), Austria 

## Related Work 
This tool was developed as part of a dermatopathology dataset preparation pipeline for TCIA (link to be added).

