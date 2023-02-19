import numpy as np
import SimpleITK as sitk
from util.image_util.image_window import get_image_path_by_id

def get_c3_slice_area(patient_id,c3_slice,seg_dir):
       
    seg_path = get_image_path_by_id(patient_id,seg_dir)
    seg_sitk =  sitk.ReadImage(seg_path)
    seg_array  = sitk.GetArrayFromImage(seg_sitk)[c3_slice,:,:]
    area_per_pixel =  seg_sitk.GetSpacing()[0]*seg_sitk.GetSpacing()[1]

    muscle_seg = (seg_array==1)*1.0
    
    muscle_area = np.sum(muscle_seg)*area_per_pixel/100
    
    return muscle_area

def get_c3_slice_density(patient_id,c3_slice,seg_dir,img_dir):
    
    image_path = get_image_path_by_id(patient_id,img_dir)
    image_sitk =  sitk.ReadImage(image_path)
    c3_array = sitk.GetArrayFromImage(image_sitk)[c3_slice,:,:]
    
    seg_path = get_image_path_by_id(patient_id,seg_dir)
    seg_sitk =  sitk.ReadImage(seg_path)
    seg_array  = sitk.GetArrayFromImage(seg_sitk)[c3_slice,:,:]

    muscle_seg = (seg_array==1)*1.0
    
    muscle_hu = np.sum(muscle_seg*c3_array)/np.sum(muscle_seg)
    
    return muscle_hu