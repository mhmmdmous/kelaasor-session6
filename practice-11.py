class Buttons:  
    def __init__(self, buttons_counts):  
        self.buttons_counts = buttons_counts  
    
    def processed_buttons(self):  
        new_buttons_counts = [[0] * 3 for _ in range(3)]  
        for i in range(3):  
            for j in range(3):  
                total = self.buttons_counts[i][j]  
                
                # افزودن دکمه‌های مجاور  
                if i > 0:  
                    total += self.buttons_counts[i-1][j]  # بالا  
                if i < 2:  
                    total += self.buttons_counts[i+1][j]  # پایین  
                if j > 0:  
                    total += self.buttons_counts[i][j-1]  # چپ  
                if j < 2:  
                    total += self.buttons_counts[i][j+1]  # راست  
                
                new_buttons_counts[i][j] = total  
        
        return new_buttons_counts  # برگرداندن تعداد فشرده شدن دکمه‌ها  


class LightBulb:  
    def __init__(self):  
        self.lights_list = [[1, 1, 1],  
                            [1, 1, 1],  
                            [1, 1, 1]]  
    
    def turn_on(self, i, j):  
        self.lights_list[i][j] = 1  

    def turn_off(self, i, j):  
        self.lights_list[i][j] = 0  

    def toggle(self, buttons):  
        processed = buttons.processed_buttons()  # دریافت تعداد فشرده شدن دکمه‌ها  
        for i in range(3):  
            for j in range(3):  
                if processed[i][j] % 2 == 0:  
                    self.turn_on(i, j)  # اگر تعداد دکمه‌های فشرده زوج است، لامپ روشن می‌شود  
                else:  
                    self.turn_off(i, j)  # در غیر این صورت لامپ خاموش می‌شود  
        return self.lights_list    

    def show_lights(self):  
        return self.lights_list  


def get_user_input():  
    first_line = input().split()  
    second_line = input().split()  
    third_line = input().split()  
    buttons_lines = [list(map(int, first_line)),   
                     list(map(int, second_line)),   
                     list(map(int, third_line))]  
    return buttons_lines  

 
user_input = get_user_input()  
if user_input:  # بررسی اینکه ورودی موفقیت‌آمیز بود یا نه  
    buttons_counts = Buttons(user_input)  # ایجاد شیء از کلاس Buttons  
    light_bulb = LightBulb()  # ایجاد شیء از کلاس LightBulb  
    light_bulb.toggle(buttons_counts)  # تغییر وضعیت لامپ‌ها بر اساس دکمه‌ها  
    print(light_bulb.show_lights())  # نمایش وضعیت لامپ‌ها