# Chest X-Ray Pneumonia CNN

Biomedical image-processing and CNN classification project for detecting pneumonia from chest X-ray images.

## Overview

The main script loads chest X-ray images, preprocesses them, extracts image features, trains CNN models with PyTorch, and evaluates classification performance for `NORMAL` vs `PNEUMONIA` images.

## Tech Stack

- Python
- PyTorch
- NumPy
- SciPy
- scikit-image
- scikit-learn
- imageio
- Matplotlib

## Dataset

The image dataset is not included because medical image datasets are large and should be downloaded from their original source.

Expected structure:

```text
data/chest_xray/
  train/
    NORMAL/
    PNEUMONIA/
  val/
    NORMAL/
    PNEUMONIA/
  test/
    NORMAL/
    PNEUMONIA/
```

Alternatively, set the dataset path:

```powershell
$env:CHEST_XRAY_DATASET="D:\path\to\chest_xray"
```

## Setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```powershell
python src\biomedical_project.py
```

The script expects the dataset to exist before running.

## GitHub Readiness

Status: strong computer-vision CV project, but it needs dataset instructions and reproducible results before public upload.

Recommended before publishing:

- Add dataset source link/provenance.
- Add sample metrics and plots.
- Add a smaller smoke-test mode.
- Add command-line arguments for dataset path, epochs, batch size, and output folder.
- Add a license if public.
