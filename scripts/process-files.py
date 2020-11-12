import csv
import datetime
import random
import sys
import os
import time
import argparse
import pandas as pd
import json

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

BASE_DIR = "/Users/jrtorres/Documents/JRTDocs/Development/General_Projects/cpd-workshop-health-care/data/"
OUTPUT_DIR = "/Users/jrtorres/tmp/"

LOINC_CODES_NAMES = { 
    "8302-2": "Height", 
    "29463-7": "Weight", 
    "6690-2": "Leukocytes", 
    "789-8": "Erythrocytes",
    "718-7": "Hemoglobin", 
    "4544-3": "Hematocrit", 
    "787-2": "MCV", 
    "785-6": "MCH", 
    "786-4": "MCHC", 
    "777-3": "Platelets", 
    "8462-4": "Diastolic Blood Pressure", 
    "8480-6": "Systolic Blood Pressure", 
    "39156-5": "Body Mass Index", 
    "2093-3": "Total Cholesterol", 
    "2571-8": "Triglycerides", 
    "18262-6": "LDL Cholesterol", 
    "2085-9": "HDL Cholesterol", 
    "4548-4": "A1c Hemoglobin Total", 
    "2339-0": "Glucose", 
    "6299-2": "Urea Nitrogen", 
    "38483-4": "Creatinine", 
    "49765-1": "Calcium", 
    "2947-0": "Sodium", 
    "6298-4": "Potassium", 
    "2069-3": "Chloride", 
    "20565-8": "Carbon Dioxide", 
    "14959-1": "Microalbumin Creatinine Ratio", 
    "38265-5": "DXA Bone density", 
    "26464-8": "White Blood Cell", 
    "26453-1": "Red Blood Cell", 
    "30385-9": "RBC Distribution Width", 
    "26515-7": "Platelet Count"
}

def subset_files_by_patient(num_patients, base_directory=BASE_DIR, output_directory=OUTPUT_DIR):
    patients_df = pd.read_csv(base_directory + "/patients.csv") 
    allergies_df = pd.read_csv(base_directory + "/allergies.csv") 
    conditions_df = pd.read_csv(base_directory + "/conditions.csv") 
    encounters_df = pd.read_csv(base_directory + "/encounters.csv")
    immunizations_df = pd.read_csv(base_directory + "/immunizations.csv") 
    medications_df = pd.read_csv(base_directory + "/medications.csv") 
    observations_df = pd.read_csv(base_directory + "/observations.csv") 

    patients_small_df = patients_df[:num_patients]

    # Files with just patient related data
    allergies_small_df = allergies_df[allergies_df["PATIENT"].isin(patients_small_df["ID"])]
    conditions_small_df = conditions_df[conditions_df["PATIENT"].isin(patients_small_df["ID"])]
    encounters_small_df = encounters_df[encounters_df["PATIENT"].isin(patients_small_df["ID"])]
    immunizations_small_df = immunizations_df[immunizations_df["PATIENT"].isin(patients_small_df["ID"])]
    medications_small_df = medications_df[medications_df["PATIENT"].isin(patients_small_df["ID"])]
    observations_small_df = observations_df[observations_df["PATIENT"].isin(patients_small_df["ID"])]

    print("Patients: ", patients_df.shape, "\t\tPatients Subset: ", patients_small_df.shape)
    print("Allergies: ", allergies_df.shape, "\t\tAllergies Subset: ", allergies_small_df.shape)
    print("Conditions: ", conditions_df.shape, "\t\tConditions Subset: ", conditions_small_df.shape)
    print("Encounters: ", encounters_df.shape, "\t\tEncounters Subset ", encounters_small_df.shape)
    print("Immunizations: ", immunizations_df.shape, "\t\tImmunizations Subset ", immunizations_small_df.shape)
    print("Medications: ", medications_df.shape, "\t\tMedications Subset: ", medications_small_df.shape)
    print("Observations: ", observations_df.shape, "\t\tObservations Subset: ", observations_small_df.shape)

    try:
        patients_small_df.to_csv(output_directory + "/patients.csv", index=False)
        allergies_small_df.to_csv(output_directory + "/allergies.csv", index=False)
        conditions_small_df.to_csv(output_directory + "/conditions.csv", index=False)
        encounters_small_df.to_csv(output_directory + "/encounters.csv", index=False)
        immunizations_small_df.to_csv(output_directory + "/immunizations.csv", index=False)
        medications_small_df.to_csv(output_directory + "/medications.csv", index=False)
        observations_small_df.to_csv(output_directory + "/observations.csv", index=False)
    except Error as e:
        print("Error: ", e)

def print_unique_observation_codedescriptions(observation_fname):
    observations_df = pd.read_csv(observation_fname)
    print("Total number of observations: ", len(observations_df))
    codes = observations_df.CODE.unique()
    print("Number of unique observation codes: ", len(codes))
    for c in codes:
        t_df = observations_df[observations_df.CODE == c].iloc[0]
        print('{:15s} {}'.format(c, t_df.loc['DESCRIPTION']))

def transpose_observations(observation_fname, output_fname):
    observations_df = pd.read_csv(observation_fname)
    #cur_obs_df = observations_df[observations_df["CODE"].isin(list(loinc_observations.keys()))].filter(items=["DATE", "PATIENT", "ENCOUNTER", "VALUE", "CODE"])
    #cur_obs_df.to_csv("/Users/jrtorres/tmp/test_process_obs.csv", index=False)

    final_observations_df = pd.DataFrame() #None
    for loinc_code, obs_name in LOINC_CODES_NAMES.items():
        print("========================================================")
        print("Starting columns: ", list(final_observations_df))
        col_name = obs_name + " [" + loinc_code + "]"
        #print("Capturing Code: ", loinc_code, "Column Name: ", col_name)
        cur_obs_df = pd.DataFrame()
        cur_obs_df = observations_df[observations_df["CODE"] == loinc_code].filter(items=["DATE", "PATIENT", "ENCOUNTER", "VALUE"])
        cur_obs_df.rename(columns = {'VALUE':col_name.upper()}, inplace = True)         
        if final_observations_df.empty:
            final_observations_df = cur_obs_df.copy()
        else:
            if not cur_obs_df.empty:
                print("Attemptin merge of: ", list(cur_obs_df))
                final_observations_df = pd.merge(final_observations_df, cur_obs_df, on=["DATE","PATIENT", "ENCOUNTER"], how="outer")
            else:
                print("No observations for: ", col_name)
        print("Ending columns: ", list(final_observations_df))
        print("========================================================")

    print("Final Schema: ") 
    final_observations_df.info()
    final_observations_df.to_csv(output_fname, index=False)

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or higher version is required for this script.")

    parser = argparse.ArgumentParser(prog="python %s)" % os.path.basename(__file__), description="Script that manages healthcare dataset.")
    parser.add_argument("-output-base-directory", dest="out_base_dir", required=False, default=None, help="Directory to store output files.")
    parser.add_argument("-input-base-directory", dest="in_base_dir", required=False, default=None, help="Directory with healthcare data set.")
    parser.add_argument("-num-patients", dest="num_records", required=False, type=int, default=0, help="Number of patients.")

    print("Starting script.\n")
    args = parser.parse_args()
    started_time = time.time()

    if args.num_records is not 0:
        subset_files_by_patient(args.num_records)

    #print_unique_observation_codedescriptions("/Users/jrtorres/tmp/observations_small.csv")

    #transpose_observations("/Users/jrtorres/tmp/observations_small_test.csv", "/Users/jrtorres/tmp/test_process_obs2.csv")
    transpose_observations(BASE_DIR+"observations.csv", OUTPUT_DIR+"observations_processed.csv")

    elapsed = time.time() - started_time
    print("\nFinished script. Elapsed time: %f" % elapsed)
