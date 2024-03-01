import matplotlib.pyplot as plt
import tqdm
import numpy as np
def plot_trade_off_pure_mono(f2, r_space, given_f=50):
    selected_r1 = []
    selected_r2 = []
    final_r1 = []
    final_r2 = []
    for i in tqdm.tqdm(range(len(r_space))):
        for j in range(len(f2[i])):
            for k in range(len(f2[i][j])):
                if f2[i][j][k] >= given_f:
                    selected_r1.append(r_space[i][0])
                    selected_r2.append(r_space[i][1])
    temp_r1 = selected_r1[0]
    min_r2 = selected_r2[0]
    for i in range(len(selected_r1)):
        if temp_r1 != selected_r1[i]:
            if min_r2 == selected_r2[0]:
                pass
            else:
                final_r1.append(temp_r1)
                final_r2.append(min_r2)
            temp_r1 = selected_r1[i]
            min_r2 = selected_r2[i]
        else:
            if selected_r2[i] < min_r2:
                min_r2 = selected_r2[i]
        


    # 绘图
    plt.figure(figsize=(10, 6))  # 设置图形大小
    plt.scatter(final_r1, final_r2, color='blue', label='Selected Points')  # 绘制选中点
    plt.title('Trade-off Plot')
    plt.xlabel('r1')
    plt.ylabel('r2')
    plt.legend()
    plt.grid(True)
    plt.show()



def plot_trade_off_diff_mono(f2_PATH1, f2_PATH2, r_space, given_f=50, if_just_line = True):
    selected_r1_PATH1 = []
    selected_r2_PATH1 = []
    selected_r1_PATH2 = []
    selected_r2_PATH2 = []
    for i in tqdm.tqdm(range(len(r_space))):
        for j in range(len(f2_PATH1[i])):
            for k in range(len(f2_PATH1[i][j])):
                if f2_PATH1[i][j][k] >= given_f:
                    selected_r1_PATH1.append(r_space[i][0])
                    selected_r2_PATH1.append(r_space[i][1])
        for m in range(len(f2_PATH2[i])):
            for n in range(len(f2_PATH2[i][m])):
                if f2_PATH2[i][m][n] >= given_f:
                    selected_r1_PATH2.append(r_space[i][0])
                    selected_r2_PATH2.append(r_space[i][1])
    if if_just_line == True:
        temp_r1 = selected_r1_PATH1[0]
        min_r2 = selected_r2_PATH1[0]
        final_r2_PATH1 = []
        final_r1_PATH1 = []
        for i in range(len(selected_r1_PATH1)):
            if temp_r1 != selected_r1_PATH1[i]:
                if min_r2 == selected_r2_PATH1[0]:
                    pass
                else:
                    final_r1_PATH1.append(temp_r1)
                    final_r2_PATH1.append(min_r2)
                temp_r1 = selected_r1_PATH1[i]
                min_r2 = selected_r2_PATH1[i]
            else:
                if selected_r2_PATH1[i] < min_r2:
                    min_r2 = selected_r2_PATH1[i]
        
        temp_r1 = selected_r1_PATH2[0]
        min_r2 = selected_r2_PATH2[0]
        final_r2_PATH2 = []
        final_r1_PATH2 = []
        for i in range(len(selected_r1_PATH2)):
            if temp_r1 != selected_r1_PATH2[i]:
                if min_r2 == selected_r2_PATH2[0]:
                    pass
                else:
                    final_r1_PATH2.append(temp_r1)
                    final_r2_PATH2.append(min_r2)
                temp_r1 = selected_r1_PATH2[i]
                min_r2 = selected_r2_PATH2[i]
            else:
                if selected_r2_PATH2[i] < min_r2:
                    min_r2 = selected_r2_PATH2[i]

        # 绘图
        plt.figure(figsize=(10, 6))  # 设置图形大小
        plt.scatter(final_r1_PATH1, final_r2_PATH1, color='blue', label='Selected Points PATH1')  # 绘制PATH1选中点
        plt.scatter(final_r1_PATH2, final_r2_PATH2, color='red', label='Selected Points PATH2')  # 绘制PATH2选中点
        plt.title('Trade-off Plot')
        plt.xlabel('r1')
        plt.ylabel('r2')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        plt.figure(figsize=(10, 6))  # 设置图形大小
        plt.scatter(selected_r1_PATH1, selected_r2_PATH1, color='blue', label='Selected Points PATH1')  # 绘制PATH1选中点
        plt.scatter(selected_r1_PATH2, selected_r2_PATH2, color='red', label='Selected Points PATH2')  # 绘制PATH2选中点
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
