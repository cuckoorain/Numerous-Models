import numpy as np
from functools import partial



# 定义独立的二元线性函数
def linear_model_2var(x, y, a, b, c):
    return a * x + b * y + c

def linear_model_1var(x, a, b, c):
    return a * x + b + c

def create_linear_models_2inputs(number_of_models, if_diff_mono = False):
    res = []
    if if_diff_mono == True:
        increase_num = number_of_models // 2
        decrease_num = number_of_models - increase_num
    else:
        increase_num = number_of_models
    for i in range(increase_num):
        a = np.random.rand()  # 生成正数系数a
        b = np.random.rand()  # 生成正数系数b
        c = np.random.randn()  # 随机生成常数项c，可以是任意实数

        # 使用partial创建绑定了特定系数的linear_model版本
        model_temp = partial(linear_model_2var, a=a, b=b, c=c)

        res.append(model_temp)

    if if_diff_mono == True:
        for i in range(decrease_num):
            a = -6.0*np.random.rand()  # 生成负数系数a
            b = 6.0*np.random.rand()  # 生成负数系数b
            c = 10  # 随机生成常数项c，可以是任意实数

            # 使用partial创建绑定了特定系数的linear_model版本
            model_temp = partial(linear_model_2var, a=a, b=b, c=c)

            res.append(model_temp)

    return res

def create_linear_models_1input(number_of_models, if_diff_mono = False):
    res = []
    if if_diff_mono == True:
        increase_num = number_of_models // 2
        decrease_num = number_of_models - increase_num
    else:
        increase_num = number_of_models
    for i in range(increase_num):
        a = np.random.rand()  # 生成正数系数a
        b = np.random.rand()  # 生成正数系数b
        c = np.random.randn()  # 随机生成常数项c，可以是任意实数

        # 使用partial创建绑定了特定系数的linear_model版本
        model_temp = partial(linear_model_1var, a=a, b=b, c=c)

        res.append(model_temp)

    if if_diff_mono == True:
        for i in range(decrease_num):
            a = -np.random.rand()  # 生成负数系数a
            b = -np.random.rand()  # 生成负数系数b
            c = np.random.randn()  # 随机生成常数项c，可以是任意实数

            # 使用partial创建绑定了特定系数的linear_model版本
            model_temp = partial(linear_model_1var, a=a, b=b, c=c)

            res.append(model_temp)

    return res

#
# # 使用例子
# n = 3  # 假设我们想要生成 3 个模型
# models = create_linear_models(n)
#
# # 测试这些模型
# x_values = np.array([1, 2, 3])  # 为x提供一组值
# y_values = np.array([4, 5, 6])  # 为y提供一组值
#
# for i, model in enumerate(models):
#     result = model(x_values, y_values)
#     print(f"Model {i + 1}: {result}")


def generate_r_space():
    ret = []
    for i in range(100):
        for j in range(100):
            ret.append([i, j])
    return ret

