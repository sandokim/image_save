# numpy save
np.save('/UNETR/BTCV/val_outputs', val_outputs[0])
output = np.load('./val_outputs.npy')

# nibabel save
img = nib.Nifti1Image(val_outputs[0], np.eye(4))
img.get_data_dtype() == np.dtype(np.int16)
nib.save(img, '/UNETR/BTCV/val_outputs.nii.gz')
