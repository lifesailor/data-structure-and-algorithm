"""
queue 클라이언트
"""
from queue import Queue


class Client:
    def test(self, args):
        queue = Queue()

        while args:
            item = args.pop(0)
            if item is not "-":
                queue.enqueue(item)
            elif not queue.is_empty():
                print(queue.dequeue(), end=' ')
        print("(" + str(queue.size()) + " left on the queue" + ")")


if __name__ == "__main__":
    queue_client = Client()
    words =['to', 'be', 'or', 'not', 'to', '-', 'be', '-', '-', 'that', '-', '-', '-', 'is']
    queue_client.test(words)


