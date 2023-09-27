import numpy as np

# Template of the file:
# MxN,stride
# kernel[0]
# kernel[1]
# ...
def parseInput(file: str):
    lines = open(file, "r").read().split("\n")

    # Remove the header from the "lines" list while splitting it into M x N and stride
    dimensions, stride = lines.pop(0).split(",")
    # Convert everything to int
    m, n = map(lambda x: int(x), dimensions.split("x"))
    stride = int(stride)

    # More or less than the number of lines defined in the header
    if len(lines) - m != 0:
        raise Exception(
            f"Você definiu um filtro com {m} linhas, porém enviou {len(lines)}."
        )

    # Create an M x N float array (for kernels like average)
    kernel = np.empty((m, n), float)

    for i, line in enumerate(lines):
        columns = line.split(",")

        # More or less than the number of columns defined in the header
        if len(columns) - n != 0:
            raise Exception(
                f"Você definiu um filtro com {m} colunas, porém enviou {len(columns)} na linha {i + 2}."
            )

        for j in range(n):
            # eval() allows us to support fractions and the like, allowing for better UX at the cost of security
            columns[j] = eval(columns[j])

        # Assign columns to line i
        kernel[i] = np.array(columns, dtype=float)

    return [kernel, stride]
