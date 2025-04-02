"Calculating the resistance of the load using the Ganzuniv & TENMA method"
import numpy as np

# define function
def Calculres(U_mla, R_va, U_mlb, R_vb):
    R_gl = (U_mla * R_vb * R_va - U_mlb * R_va * R_vb) / (U_mlb * R_va - U_mla * R_vb)
    return R_gl

def CalculC(U_ml, R_v, R_gl):
    C = U_ml / R_v * R_gl
    return C

numbers = np.zeros(10)  # 创建长度为 10 的 NumPy 数组，初始值全为 0

"Ganzuniv"
U_mla = 2.1
R_va = 316 * 10**3

"TENMA"
U_mlb =2.41
R_vb = 10 * 10**6

"HM8012"
U_mlc = 2.6
R_vc = 1 * 10**9

"Ganzuniv & TENMA"
# 调用函数
result = Calculres(U_mla, R_va, U_mlb, R_vb)
numbers[0] = result
print("Ganzuniv & TENMA", result, "ohm")

"TENMA & HM8012"
# 调用函数
result = Calculres(U_mlb, R_vb, U_mlc, R_vc)
numbers[1] = result
print("TENMA & HM8012", result, "ohm")

"Ganzuniv & HM8012"
# 调用函数
result = Calculres(U_mla, R_va, U_mlc, R_vc)
numbers[2] = result
print("Ganzuniv & HM8012", result, "ohm")

# 计算平均值
average = np.mean(numbers)

print("数值数组:", numbers)
print("平均值:", average)

"Ganzuniv"
C_a = CalculC(U_mla, R_va, average)
print("C_a:", C_a, "V")

"TENMA"
C_b = CalculC(U_mlb, R_vb, average)
print("C_b:", C_b, "V")

"HM8012"
C_c = CalculC(U_mlc, R_vc, average)
print("C_c:", C_c, "V")
