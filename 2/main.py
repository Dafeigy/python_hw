from turtle import *
import random
import json



class QA_pair():
    '''
    算式(Q)-答案(A)对是该生成系统下的基本元素。它由`操作数`、`操作符号`、`计算结果`以及`算式合法标志`四个基本属性组成。

    同时具备了返回渲染的字符串结果、检查算式合法性的函数，方便生成更多样的二元四则运算的算式。
    '''
    operator_dict={
        '+': '+',
        '-': '-',
        '*': '×',
        '/': '÷'
    }
    def __init__(self, operator:str, num1:int, num2: int):
        self.operator = operator
        self.num1 = num1
        self.num2 = num2
        self.result = eval(f"{self.num1}{self.operator}{self.num2}")
        self.able_flag = self.check_available()

    def generate_A(self):
        return "{:>3}".format(f"{self.num1}") + "{:>2}".format(f"{self.operator_dict[self.operator]}") + "{:>3}".format(f"{self.num2}") + " = "
    
    def generate_Q(self):
        return "{:>3}".format(f"{self.num1}") + "{:>2}".format(f"{self.operator_dict[self.operator]}") + "{:>3}".format(f"{self.num2}") + " = " + "{:>3}".format(f"{int(self.result)}")
    
    def check_available(self):
        return (self.result % 1 == 0) and (100 > self.result > 0) and (False if (self.num2 == 1 and self.operator == '/') else True)
    
class Paper():
    '''
    用于产生试题。
    '''
    def __init__(self, config) -> None:
        self.cfg = config
        self.Q, self.A = self.generate_data()
        
    def render_paper(self):

        screensize(1920,1080)
        speed(0)
        hideturtle()
        color('black')
        penup()
        goto(-300,400)
        pendown()
        write("试题",font=("宋体", 22, "bold"))
        pu()
        goto(-300,450)
        x, y = -300, 400
        goto(x,y)
        for k,each in enumerate(P.A):
            if k % 3 == 0:
                y -= 50
                x = -300
        
            goto(x, y)
            pendown()
            write(each,font=("宋体",13, "bold"))
            # write('□',font=("宋体",20, "bold"))
            penup()
            goto(x+120,y)
            pendown()
            draw_squre()
            penup()
            x += 200

        goto(-300,80)
        x,y= -300, 30
        goto(x,y)
        
        write("答案",font=("宋体", 22, "bold"))
        for k,each in enumerate(P.Q):
            if k % 3 == 0:
                y -= 50
                x = -300
        
            goto(x, y)
            pendown()
            write(each,font=("宋体",13, "bold"))
            # write('□',font=("宋体",20, "bold"))
            penup()
            goto(x+120,y)
            pendown()
            draw_squre()
            penup()
            x += 200
        exitonclick()

    def generate_data(self):
        data_Q = []
        data_A = []
        
        for k,v in self.cfg.items():
            counter = 0
            while counter < v :
                tmp = QA_pair(k, random.randint(1,99), random.randint(1,99))
                if tmp.able_flag:
                    if tmp.generate_A() not in data_A:
                        data_A.append(tmp.generate_A())
                        data_Q.append(tmp.generate_Q())
                        counter += 1
        print("Data generated.")
        return data_Q, data_A


def draw_squre():
    pendown()
    for i in range(4):
        fd(30)
        left(90)


if __name__ == "__main__":
    with open("config.json",'r', encoding='UTF-8') as f:
        config = json.load(f)
    P = Paper(config)
    P.render_paper()

