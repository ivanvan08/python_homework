import time


def bubble_sort(data: list):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


if __name__ == '__main__':
    first_data = [
        "banana", "apple", "window", "river", "algorithm",
        "tree", "orange", "python", "keyboard", "mouse",
        "cloud", "stone", "computer", "book", "table",
        "chair", "screen", "phone", "network", "data",
        "server", "client", "memory", "disk", "folder",
        "file", "code", "variable", "function", "loop",
        "condition", "array", "list", "tuple", "dictionary",
        "class", "object", "method", "module", "package",
        "system", "process", "thread", "cache", "buffer",
        "stream", "socket", "protocol", "request", "response"
    ]
    second_data = words_var_length = [
        "a",
        "code",
        "python",
        "if",
        "loop",
        "data",
        "x",
        "algorithm",
        "list",
        "structure",
        "api",
        "function",
        "i",
        "object",
        "class",
        "variable",
        "ui",
        "network",
        "os",
        "thread",
        "cpu",
        "memory",
        "ram",
        "disk",
        "file",
        "cache",
        "buffer",
        "stack",
        "queue",
        "hash",
        "index",
        "binary",
        "tree",
        "graph",
        "node",
        "edge",
        "recursion",
        "lambda",
        "sync",
        "async",
        "socket",
        "server",
        "client",
        "process",
        "kernel",
        "interrupt",
        "virtualization",
        "microarchitecture"
    ]
    third_data = [
        "algorithm",
        "array",
        "binary",
        "buffer",
        "cache",
        "class",
        "client",
        "cloud",
        "code",
        "condition",
        "data",
        "database",
        "debug",
        "dictionary",
        "disk",
        "element",
        "file",
        "folder",
        "function",
        "hash",
        "index",
        "integer",
        "interface",
        "kernel",
        "library",
        "list",
        "logic",
        "loop",
        "memory",
        "method",
        "module",
        "network",
        "node",
        "object",
        "package",
        "process",
        "queue",
        "recursion",
        "resource",
        "script",
        "server",
        "socket",
        "stack",
        "stream",
        "structure",
        "system",
        "thread",
        "variable",
        "virtual",
        "while"
    ]
    start = time.time()
    bubble_sort(first_data)
    print(time.time() - start)
    start = time.time()
    bubble_sort(second_data)
    print(time.time() - start)
    start = time.time()
    bubble_sort(third_data)
    print(time.time() - start)
