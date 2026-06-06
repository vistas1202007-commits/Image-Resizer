import os
from PIL import Image  # image open aur resize ke liye

print("--- Image Resizer Tool ---")

# single image resize karne ka function
def resize_single(path, width, height):
    if not os.path.exists(path):
        print("File not found!")
        return
    
    img = Image.open(path)  # image open karo
    resized = img.resize((width, height), Image.LANCZOS)  # resize karo
    
    # output file ka naam banao
    name, ext = os.path.splitext(path)
    output = name + "_resized" + ext
    
    resized.save(output)  # save karo
    print(f"Done! Saved as: {output}")

# folder ke saare images resize karne ka function
def resize_batch(folder, width, height):
    if not os.path.isdir(folder):
        print("Folder not found!")
        return
    
    # resized images ke liye alag folder banao
    output_folder = os.path.join(folder, "resized")
    os.makedirs(output_folder, exist_ok=True)
    
    # jo formats support karte hain
    formats = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
    count = 0
    
    for file in os.listdir(folder):
        if file.lower().endswith(formats):
            input_path = os.path.join(folder, file)
            output_path = os.path.join(output_folder, file)
            
            img = Image.open(input_path)
            img.resize((width, height), Image.LANCZOS).save(output_path)
            count += 1
            print(f"Resized: {file}")
    
    print(f"\n{count} images resized!")
    print(f"Saved in: {output_folder}")

# main menu
while True:
    print("\n1. Resize Single Image")
    print("2. Resize All Images in Folder")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        path = input("Enter image path: ")
        w = int(input("Enter width: "))
        h = int(input("Enter height: "))
        resize_single(path, w, h)
        
    elif choice == "2":
        folder = input("Enter folder path: ")
        w = int(input("Enter width: "))
        h = int(input("Enter height: "))
        resize_batch(folder, w, h)
        
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice!")
