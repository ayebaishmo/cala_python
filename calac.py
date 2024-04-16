class Calc:
    def __init__(self, answer):
        self.answer = answer
    
    def addition(self, first_number, second_number):
        self.answer = first_number + second_number
        return self.answer

    def subtract(self, first_number, second_number):
        self.answer = first_number - second_number
        return self.answer
    
    def multiplication(self, first_number, second_number):
        self.answer = first_number * second_number
        return self.answer
    

    def __repr__(self):
        return str(self.answer)
    
if __name__=='__main__':
    Calc1  = Calc(20)
    print(Calc1)
    Calc2 = Calc(1) # isinstance or instaiating an object
    add  = Calc2.addition(8, 9)
    sub = Calc2.subtract(9, 9)
    mult = Calc2.multiplication(2, 3)
    print(add)
    print(sub)
    print(mult)