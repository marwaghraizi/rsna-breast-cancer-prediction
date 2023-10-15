# rsna-breast-cancer-prediction
## Rename image files
This script removes the patient id from file names 
```
python rename_image_files.py /source/directory /destination/directory
```
## Separate into cancerous and healthy
the train.csv path is hard coded
```
python separate_cancerous_healthy.py /source/directory /healthy/output/directory /cancerous/output/directory
```

## Create train and test within class 
Randomly shuffles the images within a class and separates them into train and test with a 5:1 ratio
Target file organization:
---healthy
------train
------test
---cancerous
------train
------test

```
python create_train_test_within_class.py /healthy/directory /cancerous/directory
```

## Combine train and test
Target file organization:
---train
------cancerous
------healthy
---test
------cancerous
------healthy

The base directory is where the original healthy and cancerous directories are and the destination directory is where we want the new file structure to be
```
python combine_train_test.py /base/directory /destination/directory
```
