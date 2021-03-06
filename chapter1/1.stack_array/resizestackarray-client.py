"""
ResizeStackArray(배열 크기 변경 구현) 클라이언트
"""
from resizestackarray import ResizeStackArray


class Client:
    def test(self, args):
        stack = ResizeStackArray()

        while args:
            item = args.pop(0)
            if item is not "-":
                stack.push(item)
            elif not stack.is_empty():
                print(stack.pop(), end=' ')
        print("(" + str(stack.size()) + " left on the stack" + ")")


if __name__ == "__main__":
    stack_client = Client()
    words =['to', 'be', 'or', 'not', 'to', '-', 'be', '-', '-', 'that', '-', '-', '-', 'is']
    stack_client.test(words)


