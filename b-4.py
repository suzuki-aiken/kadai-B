"""
課題B-4: カウンターその2
次のコードが正しく動作するような MyCounterV2 クラスを実装してください
counter1 = MyCounterV2(value=0, step=1)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV2(value=0, step=3)
print(counter2.value)  # 0

counter2.count_up()
print(counter2.value)  # 3

counter2.count_up()
print(counter2.value)  # 6
"""


class MyCounterV2:
    def __init__(self,):


def main():
    counter1 = MyCounterV2(value=0, step=1)
    print(counter1.value)  # 0

    counter1.count_up()
    print(counter1.value)  # 1

    counter1.count_up()
    print(counter1.value)  # 2

    counter2 = MyCounterV2(value=0, step=3)
    print(counter2.value)  # 0

    counter2.count_up()
    print(counter2.value)  # 3

    counter2.count_up()
    print(counter2.value)  # 6

if __name__ == '__main__':
    main()