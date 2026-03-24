# Diabetes Prediction — ML Classification Project
## Project Goal

Разработка модели машинного обучения для прогнозирования наличия диабета на основе демографических и медицинских показателей.

Цель проекта — построить модель, пригодную для **первичного медицинского скрининга**, с минимизацией пропущенных случаев заболевания.

Dataset Overview

Данные содержат:

**Числовые признаки**

- `age`

- `bmi`

- `HbA1c_level`

- `blood_glucose_level`

🏷 **Категориальные признаки**

- `gender`

- `hypertension`

- `heart_disease`

- `smoking_history`

**Target**

- `diabetes` (0 — No, 1 — Yes)

## Exploratory Data Analysis
### Корреляция числовых признаков с диабетом

| Feature             | Correlation |
| ------------------- | ----------- |
| blood_glucose_level | **0.42**    |
| HbA1c_level         | **0.40**    |
| age                 | 0.26        |
| bmi                 | 0.21        |

### Вывод

Наиболее сильная связь наблюдается у показателей сахара крови и HbA1c, что соответствует медицинской логике.

### Категориальные признаки (χ² + Cramér’s V)

| Feature         | Cramér’s V | Interpretation   |
| --------------- | ---------- | ---------------- |
| hypertension    | **0.20**   | умеренная связь  |
| smoking_history | 0.14       | слабая–умеренная |
| gender          | 0.04       | очень слабая     |

### Вывод

- Гипертония — значимый фактор риска.

- Курение оказывает влияние.

- Пол практически не влияет на вероятность диабета.

## Preprocessing Pipeline

- Удалён редкий класс `gender = other`

- Создан бинарный признак `smoking_unknown`

- One-Hot Encoding для категориальных признаков

- StandardScaler для числовых признаков

-  `ColumnTransformer`

- Полный pipeline построен через sklearn.Pipeline

## Models
### 1️ Logistic Regression (Baseline)

- ROC-AUC: 0.886

- Высокий recall при низком threshold

- Использовалась как интерпретируемый baseline

### 2️ LightGBM (Final Model)

- ROC-AUC: 0.91

- Лучшее качество разделения классов

- Более устойчив к нелинейностям

## Threshold Optimization

Так как задача связана с медицинским скринингом, приоритет — **минимизация пропущенных случаев диабета (False Negatives)**.

Были протестированы три стратегии:

| Strategy             | Precision | Recall   | Interpretation            |
| -------------------- | --------- | -------- | ------------------------- |
| Max F1               | 0.96      | 0.70     | строгая модель            |
| High Recall (~0.95)  | 0.40      | 0.95     | агрессивный скрининг      |
| Final (Compromise) | **0.46**  | **0.92** | сбалансированный скрининг |

### Final Selected Threshold
```
Precision (diabetes=1): 0.46  
Recall (diabetes=1):    0.92  
Accuracy:               0.90  
ROC-AUC:                0.91
```
#### Интерпретация

- Пропускается лишь ~8% случаев диабета

- Умеренное количество ложноположительных

- Подходит для сценария первичного медицинского скрининга

## Practical Application

Модель может использоваться как:

- Инструмент предварительного отбора пациентов

- Система поддержки принятия решений

- Risk scoring модель для клинического скрининга

⚠ Модель не предназначена для постановки диагноза без клинического подтверждения.

### Key Insights

- Биохимические показатели — основные предикторы

- Гипертония усиливает риск диабета

- Балансировка порога критически влияет на практическую применимость модели

- ROC-AUC недостаточно для выбора финальной модели — важен анализ стоимости ошибок

### Tech Stack

- Python

- Pandas / NumPy

- Scikit-Learn

- LightGBM

- Matplotlib / Seaborn

### Future Improvements

- Cross-validation

- Probability calibration

- SHAP-based interpretability

- Cost-sensitive learning

- Deployment as API

### Conclusion

В проекте разработана модель прогнозирования диабета с использованием LightGBM, демонстрирующая ROC-AUC 0.91. Порог классификации адаптирован под задачу медицинского скрининга, что позволило достичь recall ≈ 0.92 при приемлемом precision ≈ 0.46.

Модель ориентирована на минимизацию пропущенных случаев заболевания и может использоваться как инструмент раннего выявления групп риска.

### Data: https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset
