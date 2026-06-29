from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model

    model = YOLO(r'/root/001_Code/DQCF-Net/ultralytics/cfg/models/DQCF-Net-T.yaml')  # build a new model from YAML
   
    model.info() 

