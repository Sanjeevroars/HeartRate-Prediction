# AI Cure - PARSEC 4.0

## Team Name: JellyNuts
## Team Members:
- Sanjeev Sitaraman (Team Leader)
  - Email: ss5952@srmist.edu.in
  - Phone: +91 9145404703
- Rounak Paul
  - Email: rp1256@srmist.edu.in
  - Phone: +91 6292190956
- Soham Roy Choudhury
  - Email: sr3243@srmist.edu.in
  - Phone: +91 9773904711

## Problem Statement
The goal is to construct an advanced model capable of accurately predicting an individual's heart rate.The dataset encompasses diverse attributes derived from signals measured through ECG recordings for various individuals, each exhibiting different heart rates at the respective time of measurement. These features collectively contribute to determining the heart rate at the specific moment for each individual.

## Installation and Usage
### 1. Clone the repository
```bash
git clone https://github.com/Sanjeevroars/HeartRate-Prediction.git
```
### 2. Install the requirements
```bash
pip install -r requirements.txt
```
### 3. Run the CLI in your Terminal (make sure you are in the cloned repository)
```bash
python3 run.py <path_to_input_file>
```

#### Note: The output will be stored in the cloned repository as 'results.csv'.

## File Description
- `run.py` - The CLI for the project.
- `requirements.txt` - The requirements file for the project.
- `README.md` - The README file for the project.
- `Experimental Jupyter Notebook.ipynb` - The Jupyter Notebook containing the experiments performed.
- `Final Jupyter Notebook.ipynb` - The Jupyter Notebook containing the final model.
- `lgb_model.txt` - The trained LightGBM model.
- `train_data.csv` - The training dataset.
- `sample_test_data.csv` - The sample test dataset.
- `sample_output_generated.csv` - The sample output generated for the sample test dataset.
- `Report.pdf` - The report for the project.

#### Note: The `results.csv` file is not included in the repository as it is generated after running the CLI.