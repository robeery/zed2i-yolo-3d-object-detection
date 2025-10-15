import cv2
import numpy as np
import pyzed.sl as sl

def main():
    zed = sl.Camera()
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720
    init_params.coordinate_units=sl.UNIT.METER
    init_params.depth_mode=sl.DEPTH_MODE.PERFORMANCE

    err=zed.open(init_params)
    if err!=sl.ERROR_CODE.SUCCESS:
        print("\neroare: probleme deschidere cameraa\n")
        exit()

    obj_param = sl.ObjectDetectionParameters()
    obj_param.enable_tracking = True
    obj_param.enable_segmentation = True
    obj_param.detection_model = sl.OBJECT_DETECTION_MODEL.MULTI_CLASS_BOX_MEDIUM

    if obj_param.enable_tracking:
        positional_tracking_param = sl.PositionalTrackingParameters()
        zed.enable_positional_tracking(positional_tracking_param)

    err = zed.enable_object_detection(obj_param)

    objects = sl.Objects()
    obj_runtime_param = sl.ObjectDetectionRuntimeParameters()
    obj_runtime_param.detection_confidence_threshold = 30

    cv2.namedWindow("ZED", cv2.WINDOW_NORMAL)

    while True:

        if zed.grab() == sl.ERROR_CODE.SUCCESS:
            zed.retrieve_objects(objects, obj_runtime_param)

            img = sl.Mat()
            zed.retrieve_image(img,  sl.VIEW.LEFT)

            img_cv = img.get_data()


            if objects.is_new:
                obj_arr = objects.object_list
                print(str(len(obj_arr)))

                for obj in obj_arr:
                    top_left = obj.bounding_box_2d[0] #3d
                    bottom_right = obj.bounding_box_2d[2]

                    cv2.rectangle(img_cv, (int(top_left[0]), int(top_left[1])), (int(bottom_right[0]), int(bottom_right[1])), (0,255,0), 2) #ultimile doua culoare si thickness

                    label = f"{obj.label} ({int(obj.confidence)}%)"
                    cv2.putText(img_cv, label, (int(top_left[0]), int(top_left[1]-10)), fontFace=1, fontScale=1.0, color=[255.0, 0.0, 255.0])


            img_cv = np.array(img_cv)
            print(type(img_cv))
            cv2.imshow("Object detection with ZED", img_cv)
            print("hei")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    zed.disable_object()
    zed.close()
    cv2.destroyAllWindows()


    



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
