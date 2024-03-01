import numpy as np
from functools import partial
# from Models_generation import create_linear_models
def increasing_models(models):
    ret = []
    for model in models:
        # 获取模型系数
        if hasattr(model, 'keywords') and model.keywords:
            a = model.keywords.get('a', None)
            b = model.keywords.get('b', None)
        elif hasattr(model, 'func') and model.func.__defaults__:
            # 这是一个备用方案，用于处理使用位置参数的情形
            defaults = model.func.__defaults__
            a, b = defaults[-3], defaults[-2]  # 假设a和b是倒数第三和第二个参数
        else:
            continue  # 如果没有找到参数，跳过这个模型

        # 检查a和b是否都非负
        if a is not None and b is not None and a >= 0 and b >= 0:
            ret.append(model)
    return ret


def decreasing_models(models):
    ret = []
    for model in models:
        # 获取模型系数
        if hasattr(model, 'keywords') and model.keywords:
            a = model.keywords.get('a', None)
            b = model.keywords.get('b', None)
        elif hasattr(model, 'func') and model.func.__defaults__:
            # 这是一个备用方案，用于处理使用位置参数的情形
            defaults = model.func.__defaults__
            a, b = defaults[-3], defaults[-2]  # 假设a和b是倒数第三和第二个参数
        else:
            continue  # 如果没有找到参数，跳过这个模型

        # 检查a和b是否都非负
        if a is not None and b is not None and a <= 0:
        # if a is not None and b is not None and a <= 0 and b <= 0:
            ret.append(model)
    return ret

# # 假设你已经有了一系列模型
# # models = create_linear_models(n)

# # 使用例子
# n = 3  # 假设我们想要生成 3 个模型
# models = create_linear_models(n, if_diff_mono=True)

# # 测试这些模型
# x_values = np.array([1, 2, 3])  # 为x提供一组值
# y_values = np.array([4, 5, 6])  # 为y提供一组值

# for i, model in enumerate(models):
#     result = model(x_values, y_values)
#     print(f"Model {i + 1}: {result}")

# # 过滤出所有系数a和b都非负的模型
# increased_models = increasing_models(models)

# # 测试和验证
# print(f"Filtered {len(increased_models)} out of {len(models)} models as increasing.")
