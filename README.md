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
Randomly shuffles the images within a class and separates them into train and test with a 5:1 ratio <br />
Target file organization:<br />
---healthy <br />
------train <br />
------test <br />
---cancerous <br />
------train <br />
------test <br />

```
python create_train_test_within_class.py /healthy/directory /cancerous/directory
```

## Combine train and test
Target file organization:<br />
---train<br />
------cancerous<br />
------healthy<br />
---test<br />
------cancerous<br />
------healthy<br />

The base directory is where the original healthy and cancerous directories are and the destination directory is where we want the new file structure to be
```
python combine_train_test.py /base/directory /destination/directory
```
## Google colab 
1. upload the model_ready_data directory on your google drive. Data can be found [here](https://drive.google.com/drive/folders/1t9eJEc7yxk83lp_JszQyesw80nWy2ll9?usp=sharing)
2. [Colab Marwa](https://colab.research.google.com/drive/1JjGzMrDFRyuKYkfypWTtAyy4IjSyMl3H?usp=sharing)
   
