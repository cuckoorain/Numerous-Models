import matplotlib.pyplot as plt


def plot_trade_off_pure_mono(f2, r_space, given_f=50):
    selected_r1 = []
    selected_r2 = []
    for i in range(len(r_space)):  # 使用len(r_space)而不是直接r_space
        if f2[i] >= given_f:
            selected_r1.append(r_space[i][0])
            selected_r2.append(r_space[i][1])

    # 绘图
    plt.figure(figsize=(10, 6))  # 设置图形大小
    plt.scatter(selected_r1, selected_r2, color='blue', label='Selected Points')  # 绘制选中点
    plt.title('Trade-off Plot')
    plt.xlabel('r1')
    plt.ylabel('r2')
    plt.legend()
    plt.grid(True)
    plt.show()



def plot_trade_off_pure_mono(f2_PATH1, f2_PATH2, r_space, given_f=50):
    selected_r1_PATH1 = []
    selected_r2_PATH1 = []
    selected_r1_PATH2 = []
    selected_r2_PATH2 = []
    for i in range(len(r_space)):  # 使用len(r_space)而不是直接r_space
        if f2_PATH1[i] >= given_f:
            selected_r1_PATH1.append(r_space[i][0])
            selected_r2_PATH1.append(r_space[i][1])
        if f2_PATH2[i] >= given_f:
            selected_r1_PATH2.append(r_space[i][0])
            selected_r2_PATH2.append(r_space[i][1])
    # 绘图
    plt.figure(figsize=(10, 6))  # 设置图形大小
    plt.scatter(selected_r1_PATH1, selected_r1_PATH1, color='blue', label='Selected Points PATH1')  # 绘制选中点
    plt.scatter(selected_r1_PATH2, selected_r1_PATH2, color='red', label='Selected Points PATH2' )  # 绘制选中点
    plt.title('Trade-off Plot')
    plt.xlabel('r1')
    plt.ylabel('r2')
    plt.legend()
    plt.grid(True)
    plt.show()

# 假设 f2 和 r_space 已经根据你的需求定义好了
# 例如:
# f2 = [计算或定义好的f2值列表]
# r_space = [对应的(r1, r2)值的列表]

# plot_trade_off_pure_mono(f2, r_space)  # 调用函数绘图
