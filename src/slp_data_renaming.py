import os

# Function to rename multiple files
def main():
   
    for i in range(3):
        start_folder = "data/SLP/danaLab/00" + str(i+100) + "/RGB/cover1"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45 * 3 + 9 * 45 * 3 + 90 * 45 * 3)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)
    
    for i in range(3):
        start_folder = "data/SLP/danaLab/00" + str(i+100) + "/RGB/cover2"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45 * 3 + 9 * 45 * 3 + 90 * 45 * 3 + 3 * 45)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)

    for i in range(3):
        start_folder = "data/SLP/danaLab/00" + str(i+100) + "/RGB/uncover"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45 * 3 + 9 * 45 * 3 + 90 * 45 * 3 + 3 * 45 * 2)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)
'''    for i in range(7):
        start_folder = "data/SLP/simLab/0000" + str(i+1) + "/RGB/cover1"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)

    for i in range(7):
        start_folder = "data/SLP/simLab/0000" + str(i+1) + "/RGB/cover2"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)

    for i in range(7):
        start_folder = "data/SLP/simLab/0000" + str(i+1) + "/RGB/uncover"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45 * 2)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)

    for i in range(9):
        start_folder = "data/SLP/danaLab/0000" + str(i+1) + "/RGB/cover1"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45 * 3)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)

    for i in range(9):
        start_folder = "data/SLP/danaLab/0000" + str(i+1) + "/RGB/cover2"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45 * 3 + 9 * 45)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)

    for i in range(9):
        start_folder = "data/SLP/danaLab/0000" + str(i+1) + "/RGB/uncover"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45 * 3 + 9 * 45 * 2)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)
    
    for i in range(90):
        start_folder = "data/SLP/danaLab/000" + str(i+10) + "/RGB/cover1"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45 * 3 + 9 * 45 * 3)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)

    for i in range(90):
        start_folder = "data/SLP/danaLab/000" + str(i+10) + "/RGB/cover2"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45 * 3 + 9 * 45 * 3 + 90 * 45)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)

    for i in range(90):
        start_folder = "data/SLP/danaLab/000" + str(i+10) + "/RGB/uncover"
        end_folder = "data/SLP"
        for count, filename in enumerate(os.listdir(start_folder)):
            dst =f"{str(1 + i * 45 + count + 7 * 45 * 3 + 9 * 45 * 3 + 90 * 45 * 2)}.jpg"
            src =f"{start_folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{end_folder}/{dst}"
            os.rename(src, dst)
'''
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()