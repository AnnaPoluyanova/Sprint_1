#ии подсказал как красиво вывести
import json 
class TestCase():
    
    def __init__(self,steps={},result=None,case = {}):
        self.case_steps = steps
        self.case_result = result
        self.case = case
    def set_step(self,step_number,step_text):
        self.case_steps[step_number] = step_text # Добавляем шаги
    def delete_step(self,step_number):
        del self.case_steps[step_number] # Удаляем шаги
    def set_result(self,result):
        self.case_result = result # Добавляем результат
    def get_test_case(self):
        self.case['Шаги']=self.case_steps
        self.case['Ожидаемый результат']=self.case_result
        print(json.dumps(self.case, indent=4, ensure_ascii=False)) # выводим кейс

        

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 