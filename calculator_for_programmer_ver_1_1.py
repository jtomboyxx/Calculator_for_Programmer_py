import tkinter as tk
import math

class ProgrammerCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("程式設計猿計算機 ver 1.1")
        self.root.geometry("1000x1000")  # Increase height to accommodate the new field
        
        # 顯示框：運算輸入欄位
        self.input_display = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
        self.input_display.grid(row=0, column=0, columnspan=3)

        # 顯示框：結果輸出欄位
        self.result_display = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
        self.result_display.grid(row=0, column=3, columnspan=2)

        # 顯示框：二進制輸出欄位
        self.binary_display = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
        self.binary_display.grid(row=1, column=0, columnspan=5)
        
        # 顯示框：十進制輸出欄位
        self.decimal_display = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
        self.decimal_display.grid(row=2, column=0, columnspan=5)

        # 使按下 Enter 鍵有等於的效果
        self.root.bind('<Return>', self.enter_key)  # 綁定 Enter 鍵

        # 按鈕布局
        self.create_buttons()

    def create_buttons(self):
        base_row = 3  # Adjust to start from row 3 to fit the new display field
        base_col = 1
        # 基本運算按鈕
        buttons = [
            ('7', base_row + 1, 0), ('8', base_row + 1, 1), ('9', base_row + 1, 2), ('/', base_row + 1, 3), 
            ('4', base_row + 2, 0), ('5', base_row + 2, 1), ('6', base_row + 2, 2), ('*', base_row + 2, 3),
            ('1', base_row + 3, 0), ('2', base_row + 3, 1), ('3', base_row + 3, 2), ('-', base_row + 3, 3),
            ('0', base_row + 4, 0), ('.', base_row + 4, 1), ('+', base_row + 4, 2), ('=', base_row + 4, 3)
        ]
        
        # 進階功能按鈕
        advanced_buttons = [
            ('√',   base_row + 1, 4), ('log', base_row + 2, 4), ('^',   base_row + 3, 4), ('(',   base_row + 4, 4),
            (')',   base_row + 5, 0), ('C',   base_row + 5, 1), ('<<',  base_row + 5, 2), ('>>',  base_row + 5, 3),
            ('AND', base_row + 6, 0), ('OR',  base_row + 6, 1), ('XOR', base_row + 6, 2), ('NOT', base_row + 6, 3),
            ('0x',  base_row + 7, 0)  # 16進制的前綴
        ]
        
        # 轉換按鈕
        convert_button = tk.Button(self.root, text="轉換", width=5, height=2, font=("Arial", 14), command=self.convert)
        convert_button.grid(row=base_row + 7, column=1)
        
        # 創建基本運算按鈕
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
        
        # 創建進階功能按鈕
        for (text, row, col) in advanced_buttons:
            button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def enter_key(self, event):
        """當按下 Enter 鍵時模擬按下等於按鈕"""
        self.on_button_click('=')

    def on_button_click(self, button_text):
        """根據按鈕點擊進行處理"""
        current_text = self.input_display.get()

        if button_text == '=':
            try:
                # 計算時將 16進制數字轉換為10進制數字運算
                result = eval(current_text)
                
                # 更新16進制、二進制、十進制顯示
                hex_result = self.to_hex(result)  # 顯示16進制，帶 '0x' 前綴
                binary_result = self.to_binary(result)  # 顯示對應的2進制，帶底線
                decimal_result = str(result)  # 十進制顯示結果

                # 顯示16進制
                self.result_display.delete(0, tk.END)
                self.result_display.insert(tk.END, hex_result)
                
                # 顯示二進制
                self.binary_display.delete(0, tk.END)
                self.binary_display.insert(tk.END, binary_result)

                # 顯示十進制
                self.decimal_display.delete(0, tk.END)
                self.decimal_display.insert(tk.END, decimal_result)

            except Exception as e:
                self.result_display.delete(0, tk.END)
                self.result_display.insert(tk.END, "錯誤")
                self.binary_display.delete(0, tk.END)
                self.decimal_display.delete(0, tk.END)

        elif button_text == 'C':
            self.input_display.delete(0, tk.END)
            self.result_display.delete(0, tk.END)
            self.binary_display.delete(0, tk.END)
            self.decimal_display.delete(0, tk.END)

        elif button_text == '√':
            try:
                result = math.sqrt(int(current_text, 16))  # 將16進制轉為10進制進行計算
                hex_result = self.to_hex(int(result))  # 顯示結果為16進制，帶 '0x' 前綴
                binary_result = self.to_binary(int(result))  # 顯示對應的2進制，帶底線
                decimal_result = str(result)  # 十進制顯示結果
                
                # 顯示16進制
                self.result_display.delete(0, tk.END)
                self.result_display.insert(tk.END, hex_result)
                
                # 顯示二進制
                self.binary_display.delete(0, tk.END)
                self.binary_display.insert(tk.END, binary_result)
                
                # 顯示十進制
                self.decimal_display.delete(0, tk.END)
                self.decimal_display.insert(tk.END, decimal_result)
            except ValueError:
                self.result_display.delete(0, tk.END)
                self.result_display.insert(tk.END, "錯誤")
                self.binary_display.delete(0, tk.END)
                self.decimal_display.delete(0, tk.END)

        # Additional cases for other operations (log, ^, <<, >>, AND, OR, XOR, NOT, etc.)
        # Each case should follow the same structure as the one above for correct updates of all fields.

        else:
            self.input_display.insert(tk.END, button_text)

    def convert(self):
        """在16進制與10進制之間進行轉換，顯示結果區域的轉換"""
        result_text = self.result_display.get()
        if result_text.startswith("0x"):
            # 如果結果顯示為16進制，轉換為10進制
            try:
                decimal_value = int(result_text, 16)
                self.result_display.delete(0, tk.END)
                self.result_display.insert(tk.END, str(decimal_value))  # 顯示為10進制
            except ValueError:
                self.result_display.delete(0, tk.END)
                self.result_display.insert(tk.END, "錯誤")
        else:
            # 如果結果顯示為10進制，轉換為16進制
            try:
                hex_value = self.to_hex(int(result_text))  # 顯示為16進制，帶 '0x'
                self.result_display.delete(0, tk.END)
                self.result_display.insert(tk.END, hex_value)
            except ValueError:
                self.result_display.delete(0, tk.END)
                self.result_display.insert(tk.END, "錯誤")

    def to_hex(self, num):
        """將數字轉換為16進制，並加上 '0x' 前綴"""
        return "0x" + hex(num)[2:].upper()  # 返回16進制並去除 '0x' 前綴，顯示為大寫

    def to_binary(self, num):
        """將數字轉換為2進制並且每4個bit加底線分隔"""
        binary_str = bin(num)[2:].zfill(4 * ((num.bit_length() + 3) // 4))  # 保證每4位為一組
        # 插入底線每4位
        return '_'.join([binary_str[i:i+4] for i in range(0, len(binary_str), 4)])

# 創建 Tkinter 主視窗並運行計算機
root = tk.Tk()
calculator = ProgrammerCalculator(root)
root.mainloop()
