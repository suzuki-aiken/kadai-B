"""
課題B-2: 長方形オブジェクト
次のコードが正しく動作するような Rectangle クラスを実装してください
diagonal は 対角線(の長さ) という意味です。
rectangle1 = Rectangle(height=5, width=6)
rectangle1.area()  # 30.00
rectangle1.diagonal()  # 7.81

rectangle2 = Rectangle(height=3, width=3)
rectangle2.area()  # 9.00
rectangle2.diagonal()  # 4.24
"""
import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return print(f'{self.height * self.width:.2f}')

    def diagonal(self):
        return print(f'{math.sqrt(self.height ** 2 + self.width ** 2):.2f}')


def main():
    # 入力

    # 出力
    rectangle1 = Rectangle(height=5, width=6)
    rectangle1.area()  # 30.00
    rectangle1.diagonal()  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    rectangle2.area()  # 9.00
    rectangle2.diagonal()  # 4.24


if __name__ == '__main__':
    main()
