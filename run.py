import pandas as pd
import lightgbm as lgb
import sys


#  Check if the argument is a valid file path
def check_CLI_arg():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        sys.exit(1)


def check_file_path(file_path):
    try:
        open(file_path)
        return True
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    check_CLI_arg()

    # Check if the file path is valid
    if check_file_path(sys.argv[1]):
        data = pd.read_csv(sys.argv[1])
        uuid = data['uuid']

        selected_features = ['MEAN_RR', 'MEDIAN_RR', 'SDRR_RMSSD_REL_RR', 'LF_NU', 'HF_NU', 'HF_PCT', 'HF_LF', 'RMSSD',
                             'SDSD', 'pNN25', 'pNN50', 'SDRR_REL_RR', 'SDSD_REL_RR', 'VLF', 'TP', 'KURT', 'SD2', 'LF']
        data = data[selected_features]

        # Load the model
        model_path = 'lgb_model.txt'
        model = lgb.Booster(model_file=model_path)

        # Predict the labels
        predictions = model.predict(data)

        # Save the predictions to a csv file
        predictions_df = pd.DataFrame({'uuid': uuid, 'HRV': predictions})
        predictions_df.to_csv('results.csv', index=False)

    else:
        print("File path is invalid")
        sys.exit(1)
