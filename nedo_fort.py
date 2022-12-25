#!/usr/bin/env python3

from abc import ABC, abstractmethod
import sys
import numpy as np
class LineInterpreter(ABC):
    '''
    Интерпретатор произвольного языка c 1 операцией на строку
    '''

    def __init__(self, source_file_name: str) -> None:
        '''
        Создать интерпретатор для данного исходного файла
        :param str source_file_name: Имя исходного файла
        '''
        self.source_file_name: str = source_file_name
        with open(source_file_name, 'r', encoding='utf8') as source_file:
            self._lines: list[str] = [l.rstrip() for l in source_file]
        self._current_line_idx: int = 0 if len(self._lines) else -1
        if len(self._lines) == 0:
            self.quit(f"Empty source file: {source_file_name}")

    def quit(self, message: str = ""):
        '''
        Завершить работу интерпретатора
        '''
        if message != "":
            print(message, file=sys.stderr)
        sys.exit(0)

    def current_line(self) -> str:
        if not (0 <= self._current_line_idx < len(self._lines)):
            self.quit("Program is over")
        return self._lines[self._current_line_idx]

    def abs_jump(self, line_no: int) -> None:
        self._current_line_idx = line_no

    def rel_jump(self, offset: int) -> None:
        self._current_line_idx += offset

    def step(self) -> None:
        self.rel_jump(1)

    @abstractmethod
    def execute_current_line(self) -> None:
        ...

    def run(self) -> None:
        while True:
            self.execute_current_line()
            self.step()


class NedoFort(LineInterpreter):
    def __init__(self, source_file_name: str) -> None:
        super().__init__(source_file_name)
        self.stack: list[float] = []

    def __repr__(self) -> str:
        return "Stack: " + repr(self.stack)

    def execute_current_line(self) -> None:
        # print(f"{self._current_line_idx}: {self.current_line()}")
        l = self.current_line()

        if len(l) == 0 or l.startswith('#'):
            return  # Пустая строка или комментарий или shebang
        else:
            match l:
                case 'стек' | 'stack':
                    print(self.stack)
                case 'вершина' | 'top':
                    print(self.stack[-1])
                case 'ввод' | 'input':
                    self.stack.append(float(input("> ")))
                case '+':
                    y = self.stack.pop()
                    x = self.stack.pop()
                    self.stack.append(x + y)
                case '-':
                    y = self.stack.pop()
                    x = self.stack.pop()
                    self.stack.append(x - y)
                case '*':
                    y = self.stack.pop()
                    x = self.stack.pop()
                    self.stack.append(x * y)
                case '/':
                    y = self.stack.pop()
                    x = self.stack.pop()
                    self.stack.append(x / y)
                case '**':
                    y = self.stack.pop()
                    x = self.stack.pop()
                    self.stack.append(x ** y)
                case 'взять' | 'take':
                    x = self.stack.pop()
                    self.stack.append(self.stack[int(x)])
                case 'корень' | 'sqrt':
                    x = self.stack.pop()
                    self.stack.append(x ** 0.5)
                case 'кос' | 'cos':
                    x = self.stack.pop()
                    self.stack.append(np.cos(np.radians(x)))
                case 'син' | 'sin':
                    x = self.stack.pop()
                    self.stack.append(np.sin(np.radians(x)))
                case 'peek' | 'взять с конца':
                    x = -self.stack.pop()
                    self.stack.append(self.stack[int(x)])
                case 'reljump' | 'отпрыг':
                    self.rel_jump(float(self.stack.pop()) - 1)
                case other:
                    self.stack.append(float(l))


if __name__ == '__main__':
    fi = NedoFort('proverka_nedofort.nf')
    fi.run()