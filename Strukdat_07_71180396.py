class PrefixConverter:
    def __init__(self):
        self.stackList = ['?']
    
    #method untuk menambahkan data baru
    def push(self, data):
        self.stackList.append(data)
    
    #method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return 'Isi stack kosong'
    
    #method untuk menghapus data paling atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return 'Isi stack kosong'

    def cekValidExpression(self, expression):
        if '(' in expression or ')' in expression:
            return False
        return True

    def infixToPrefix(self, expression):
        if not self.cekValidExpression(expression):
            return 'Expresi Infix yang anda masukkan tidak valid !!'
        
        output = ''
        for char in expression:
            #cek jika operand
            if (char >= 'a' and char <= 'z') and (char >= '0' and char <= '9') and (char >= 'A' and char <= 'Z'):
                output += char

            #cek stack kosong
            elif len(self.stackList) == 0:
                self.stackList.append(char)

            #cek prioritas operator
            else:
                while len(self.stackList) != 0 and self.stackList[-1] in '*/' and char in '+-':
                    output += self.stackList.pop()
                self.stackList.append(char)
        
        while len(self.stackList) != 0:
            output += self.stackList.pop()
        
        return output

if __name__ == '__main__':
    ekspresi1 = PrefixConverter()
    print(ekspresi1.infixToPrefix('1+2+3*4/2-1'))
    print(ekspresi1.infixToPrefix('A * (B - C) / D'))
    print(ekspresi1.infixToPrefix('(1+2)*3'))
    print(ekspresi1.infixToPrefix('20 * 3 - 10 + 289'))
    print(ekspresi1.infixToPrefix('100 * 30 / 600 - 30 + 100 * 777'))