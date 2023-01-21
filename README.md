# Automated-Segmentation-CT-Skeletal-Muscle

Code base for auto segmenting the muscle mass from CT images

Consists of two models: Slice Selection Model and Segmentation Model


Steps to train and test

1) The input data needs to be into the data folder into raw_data folder

2) Preprocessing script in the codebase folder will process the files by repacing to 1x1 on XY plane and bounded box cropping the iomage with 512x512 dimensions

3) The SS-training script will train the Slice Selection Model and SM-training script will train the Segmentation Model. The trained models are copied into the model/test folder.

4) Test-Pipeline script will run the Automated pipeline on the test cohort of CT scans.

5) Evaluate-Performance script will generate the evaluation metrics for the full pipeline

