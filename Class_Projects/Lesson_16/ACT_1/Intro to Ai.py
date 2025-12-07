from ultralytics import YOLO
from PIL import Image
import cv2

def detect_objects_in_image():

    print("🎨 Welcome to the Magic Image Detector! 🎨")
    print("=" * 50)
    
    image_path = input("\n📸 Enter the path to your image file: ")
    
    try:
  
        print("\n🧠 Loading the AI brain...")
        model = YOLO('yolov8n.pt')
        

        print("🔍 Looking for objects in your image...")
        results = model(image_path)
        

        detections = results[0]
        
        print("\n✨ Here's what I found: ✨")
        print("=" * 50)
        
        if len(detections.boxes) == 0:
            print("🤔 I couldn't find any objects. Try another image!")
        else:
    
            for i, box in enumerate(detections.boxes):
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                object_name = model.names[class_id]
                
                print(f"{i+1}. 🎯 {object_name.upper()} - "
                      f"Confidence: {confidence*100:.1f}%")
        

        output_path = "detected_" + image_path.split('/')[-1]
        annotated_image = detections.plot()
        cv2.imwrite(output_path, annotated_image)
        
        print(f"\n💾 Saved result as: {output_path}")
        print("✅ Done! Check out the image to see the boxes!")
        
    except FileNotFoundError:
        print("❌ Oops! I couldn't find that image. Check the path!")
    except Exception as e:
        print(f"❌ Something went wrong: {e}")
if _name_ == "_main_":
    detect_objects_in_image()
    
    again = input("\n🔄 Want to try another image? (yes/no): ")
    if again.lower() in ['yes', 'y']:
        detect_objects_in_image() 