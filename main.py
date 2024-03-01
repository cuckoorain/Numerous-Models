import numpy as np

import Models_generation
import Models_mono
from numerous_PATH import PathProcessor
import trade_off
def main():
    n = 40
    m = 10
    ModelsA = Models_generation.create_linear_models(number_of_models=n, if_diff_mono = False)
    ModelsB = Models_generation.create_linear_models(number_of_models=m)
    ModelsA_increasing = Models_mono.increasing_models(ModelsA)
    ModelsA_decreasing = Models_mono.decreasing_models(ModelsA)
    ModelsB_increasing = Models_mono.increasing_models(ModelsB)
    ModelsB_decreasing = Models_mono.decreasing_models(ModelsB) # no need for demonstration
    PATH_increase_increase = PathProcessor([ModelsA_increasing, ModelsB_increasing])
    PATH_decrease_increase = PathProcessor([ModelsA_decreasing, ModelsB_increasing])
    r_space = Models_generation.generate_r_space()
    f1_PATH_increase_increase = []
    f1_PATH_decrease_increase = []
    f2_PATH_increase_increase = []
    f2_PATH_decrease_increase = []
    r1 = np.array([r_space[i][0] for i in range(len(r_space))])
    r2 = np.array([r_space[i][1] for i in range(len(r_space))])
    for i in
    f1_PATH_increase_increase.append(PATH_increase_increase.process(r1, r2)[0])
    f1_PATH_decrease_increase.append(PATH_decrease_increase.process(r1, r2)[0])
    f2_PATH_increase_increase.append(PATH_increase_increase.process(r1, r2)[1])
    f2_PATH_decrease_increase.append(PATH_decrease_increase.process(r1, r2)[1])
    trade_off.plot_trade_off_pure_mono(f2_PATH_increase_increase, r_space, given_f = 50)
    trade_off.plot_trade_off_diff_mono(f2_PATH_increase_increase, f2_PATH_decrease_increase, r_space, given_f = 50)

if __name__ == "__main__":
    main()