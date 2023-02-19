import glob
import os
import SimpleITK as sitk
from util.image_util.image_window import get_image_path_by_id

def get_C3_seg_array_by_id(patient_id,c3_slice_manual,seg_dir):
    
    seg_path = get_image_path_by_id(patient_id,seg_dir)
    seg_sitk =  sitk.ReadImage(seg_path)
    seg_array  = sitk.GetArrayFromImage(seg_sitk)[c3_slice_manual,:,:]

    muscle_seg = (seg_array==1)*1.0
    
    return muscle_seg

def get_C3_image_array_by_id(patient_id,c3_slice_manual,image_dir):
    
    image_path = get_image_path_by_id(patient_id,image_dir)
    image_sitk =  sitk.ReadImage(image_path)
    image_array = sitk.GetArrayFromImage(image_sitk)[c3_slice_manual,:,:]
    
    return image_array