import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook

ws = load_workbook("files/Ch01_HW03_linear_regression_data.xlsx")["Sheet1"]

n = ws.max_row + 1
x = []

for i in range(2, n):
    x.append([ws[f"A{i}"].value, ws[f"B{i}"].value, ws[f"C{i}"].value])

x = np.array(x).reshape(-1, 3)
