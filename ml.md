# machine learning stuff

## resources
Starting a ML from scratch is a bad idea. Lots of great code exists. Here are some places to start
* fastai https://docs.fast.ai/
* Hugging face. https://huggingface.co/
* timm https://rwightman.github.io/pytorch-image-models/
* segmentation. https://github.com/qubvel/segmentation_models.pytorch
* 3D modeling and tasks in ML. https://pytorch3d.org/
* Augmentations for images. https://albumentations.ai
* Fine tunning YoLo7. this is a good start. https://learnopencv.com/fine-tuning-yolov7-on-custom-dataset/

## labeling tools. 
* this list of tools is helpful https://github.com/heartexlabs/awesome-data-labeling
* I've used this one (which is ont the list) https://github.com/heartexlabs/labelImg
* 
## wrapper for common ML tasks. 
* FLAML helps with hyper parameters and other common tasks, so I can do more thinking, less boiler plate. https://github.com/microsoft/FLAML


## datat loader with bad data
```python
class MyDataSet(Dataset):
    def __getitem__(self, index):
        try:
            return myitem[index]
        expect:
        return None

def custom_collate(batch):
    batch2 = [item for item in batch if item is not None]
        if len(batch2) != len(batch):
            print("Removed a problem item when making the batch. ")
   return batch2

ds = MyDataSet()
dl = Dataloader(ds, collate_fn = custom_collate))
```
    
