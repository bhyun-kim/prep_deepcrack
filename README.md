# Preprocessing for DeepCrack Dataset.

This repository provides a simple code for converting the format of the [DeepCrack](https://github.com/yhlleo/DeepCrack) dataset, a dataset used for crack detection in images. The original DeepCrack dataset is provided in a binary format with pixel values ranging from 0 to 255, which might be incompatible with datasets that require multiple classes for various tasks.

The 'prep_deepcrack.py' script included in this repository enables users to convert the DeepCrack dataset into a more compatible format with other datasets. Specifically, it converts the pixel values of the label images to binary values \[0, 1\], ensuring seamless integration with other datasets requiring mutli-class labels. The converted labels are saved with the suffix '\_binary_label.png' for easy identification.

If you wish to use the DeepCrack dataset with the modified labels, please download the original dataset from the following link: \[[dropbox](https://www.dropbox.com/s/sfz7avv9zlathte/preprocessed_deepcrack.zip?dl=0)\].

---

## To get started

### Installation

```
pip install -r requirements.txt
```

Run Script

```
python prep_deepcrack.py --path "path_to_dataset"
```
