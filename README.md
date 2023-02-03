# Automated-Segmentation-CT-Skeletal-Muscle

Code base for auto segmenting the skeletal muscle mass from 3D CT images

Consists of two deep-learning models: Slice Selection Model and Segmentation Model


Scripts to train and test

1) Preprocessing (optional) : This is an optional step for processing CT inages that are different from MDACC files. The pre-processing does normalizetion of files.

2) Data-Prep : This script processes .nrrd or .nifti format files and prepares the traiing files needed for both Slice Selection Model and Segmentation Model training.

3) Train-Models : This script will train the Slice Selection Model and SM-training script will train the Segmentation Model. The trained models are copied into the model/test folder.

4) Test-Pipeline:  This script will run the Automated pipeline on the test cohort of CT scans.

5) Analysis-post-testing : This script will generate the evaluation metrics for the full pipeline.

