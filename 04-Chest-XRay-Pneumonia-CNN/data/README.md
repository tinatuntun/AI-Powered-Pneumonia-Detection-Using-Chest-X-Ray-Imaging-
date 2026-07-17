# Dataset Folder

This project expects the Chest X-Ray Pneumonia dataset to be placed here before training.

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

You can also keep the dataset elsewhere and set:

```powershell
$env:CHEST_XRAY_DATASET="D:\path\to\chest_xray"
```

The dataset images are not included in this repository because medical image datasets are large and should be downloaded from their original source.
