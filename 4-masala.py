import os

class FindFile:
    @staticmethod
    def check_file():
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')  
        file_path = os.path.join(downloads_folder, 'product_list.docx')  
        
        if os.path.exists(file_path):
            return True
        else:
            return False


file_checker = FindFile()
if file_checker.check_file():
    print("product_list.docx fayli downloads papkasida mavjud.")
else:
    print("product_list.docx fayli downloads papkasida mavjud emas.")
