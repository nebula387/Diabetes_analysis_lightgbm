import os
import shutil
import kagglehub

data_path = "Kaggle/Diabetes_prediction/data"
os.makedirs(data_path, exist_ok=True)

print("Структура проекта создана")

# Download latest version
path = kagglehub.dataset_download("iammustafatz/diabetes-prediction-dataset")

print("Path to dataset files:", path)


file_path = path.replace('\\', "/")
file_path


# откуда
source_folder = file_path

# посмотрим что внутри
print("data_file: ", os.listdir(source_folder)[0])

data_file = os.listdir(source_folder)[0]

source_file = os.path.join(source_folder, data_file)

destination_folder = data_path
os.makedirs(destination_folder, exist_ok=True)

destination_file = os.path.join(destination_folder, data_file)

shutil.copy(source_file, destination_file)

print("Файл скопирован!")