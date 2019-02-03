"""
Stack 클라이언트 - 산술표현식 계산

- 피연산자를 만나면 피연산자 스택에 넣는다.
- 연산자를 만나면 연산자 스택에 넣는다.
- 열림 괄호를 만나면 무시한다.
- 닫힌 괄호를 만나면 연산자와 그 연산자에 필요한 피연산자들을 스택에서 꺼낸다. 꺼내어진 연산자와 피연산자의 계산 값을 구하여 피연산자 스택에 넣는다.
"""
from stack import Stack
import math


class Client:
    def test(self, args):
        ops = Stack()
        vals = Stack()

        while args:
            item = args.pop(0)

            # operator
            if item is "(": pass
            elif item is "+": ops.push(item)
            elif item is "-": ops.push(item)
            elif item is "*": ops.push(item)
            elif item is "/": ops.push(item)
            elif item is "sqrt": ops.push(item)
            elif item is ")":
                op = ops.pop()
                v = vals.pop()
                if op is "+": v = vals.pop() + v
                elif op is "-": v = vals.pop() - v
                elif op is "*": v = vals.pop() * v
                elif op is "/": v = vals.pop() / v
                elif op is "sqrt": v = math.sqrt(v)
                vals.push(v)
            else:
                vals.push(float(item))
        print(vals.pop())


if __name__ == "__main__":
    stack_client = Client()
    # expression = "( 1 + ( ( 2 + 3 ) * ( 4 + 5 ) ) )"
    expression = "( ( 1 + sqrt ( 5.0 ) ) / 2.0 )"
    stack_client.test(expression.split(' '))
