from kivy.app import App
from kivy.lang import Builder
import os

class ExcelOpener(App):
    def open_excel_file(self, instance):
        # Đoạn mã mở file Excel ở đây
        excel_file_path = "khong_ma.xlsx"  # Thay đổi đường dẫn tới file Excel của bạn

        # Kiểm tra nếu file tồn tại
        if os.path.exists(excel_file_path):
            try:
                # Mở file Excel
                os.system(f'start excel "{excel_file_path}"')  # Mở file Excel trên Windows
                # Trong trường hợp bạn đang sử dụng hệ điều hành khác, hãy thay đổi lệnh mở file Excel phù hợp
            except Exception as e:
                print("Error:", e)
        else:
            print("File not found.")

    def build(self):
        return Builder.load_file('project.kv')

if __name__ == '__main__':
    ExcelOpener().run()
