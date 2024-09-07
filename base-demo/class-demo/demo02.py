
class Container:
    def __init__(self, *args):
        self.container = list(args)  # 初始化容器，接受可变数量的参数

    def __del__(self):
        print(f"对象 {id(self)} 正在被销毁。")

    def __repr__(self):
        return f"Container({self.container})"

    def __setitem__(self, key, value):
        self.container[key] = value  # 索引赋值

    def __getitem__(self, key):
        return self.container[key]  # 索引获取

    def __len__(self):
        return len(self.container)  # 获取容器长度

    def __cmp__(self, other):
        if not isinstance(other, Container):
            return NotImplemented
        return (self.container > other.container) - (self.container < other.container)

    def __call__(self, *args):
        print(f"Container 对象被调用，参数为：{args}")

    def __add__(self, other):
        if isinstance(other, Container):
            return Container(*(self.container + other.container))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Container):
            return Container(*(self.container[:-1] if len(self.container) >= len(other.container) else self.container))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Container(*(self.container * other))
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int) and other != 0:
            return Container(*(x / other for x in self.container))
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, int):
            return Container(*(x % other for x in self.container))
        return NotImplemented

    def __pow__(self, power):
        return Container(*(x ** power for x in self.container))

    def __str__(self):
        return f"Container 对象: {self.container}"

# 测试代码
if __name__ == "__main__":
    c1 = Container(1, 2, 3)
    c2 = Container(4, 5)
    print(f"c1: {c1}")  # 使用 __str__
    print(f"c2: {c2}")

    c1[1] = 20  # 使用 __setitem__
    print(f"c1 修改后: {c1}")

    print(c1[1])  # 使用 __getitem__
    print(len(c1))  # 使用 __len__

    c3 = c1 + c2  # 使用 __add__
    print(f"c1 + c2: {c3}")

    c4 = c1 - c2  # 使用 __sub__
    print(f"c1 - c2: {c4}")

    c5 = c1 * 2  # 使用 __mul__
    print(f"c1 * 2: {c5}")

    c6 = c1 / 2  # 使用 __truediv__
    print(f"c1 / 2: {c6}")

    c7 = c1 % 3  # 使用 __mod__
    print(f"c1 % 3: {c7}")

    c8 = c1 ** 2  # 使用 __pow__
    print(f"c1 ** 2: {c8}")

    c1(123)  # 使用 __call__



