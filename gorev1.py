import colorDetection as color
import time
import cv2


def get_sensor_data():
    return 2.0


def yon_kontrolu(detected_objects):
    for obj in detected_objects:
        label = obj.label
        x = obj.x
        y = obj.y
        width = obj.width
        height = obj.height
        rotation = obj.rotation
        if label == "Red":
            print(f"{label}: Object Coordinates - x: {x}, y: {y}, width: {width}, height: {height}, rotation: {rotation}")
            print("Sağa dön")
        elif label == "Green":
            print(f"{label}: Object Coordinates - x: {x}, y: {y}, width: {width}, height: {height}, rotation: {rotation}")
            print("Sola dön")
        elif label == "Yellow":
            print(f"{label}: Object Coordinates - x: {x}, y: {y}, width: {width}, height: {height}, rotation: {rotation}")
            if x < 320:
                print("Sarı nesne kameranın solunda, sağa yönel")
            elif x > 640:
                print("Sarı nesne kameranın sağında, sola yönel")
            else:
                print("Sarı nesne kameranın ortasında, zikzak yönel")


if __name__ == "__main__":
    while True:
        distance = get_sensor_data()
        if distance <= 2.0:
            detected_objects = color.color_detect()
            yon_kontrolu(detected_objects)
            cap = color.cap
            if not cap.isOpened():
                break
        else:
            print("2 metre uzaklıkta nesne tespit edilmedi")
