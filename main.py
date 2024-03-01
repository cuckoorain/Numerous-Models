import numpy as np
import tqdm
import Models_generation
import Models_mono
from numerous_PATH import PathProcessor
import trade_off
def main():
    n = 40
    m = 10
    ModelsA = Models_generation.create_linear_models_2inputs(number_of_models=n, if_diff_mono = True)
    ModelsB = Models_generation.create_linear_models_1input(number_of_models=m, if_diff_mono = True)
    ModelsA_increasing = Models_mono.increasing_models(ModelsA)
    ModelsA_decreasing = Models_mono.decreasing_models(ModelsA)
    ModelsB_increasing = Models_mono.increasing_models(ModelsB)
    ModelsB_decreasing = Models_mono.decreasing_models(ModelsB) # no need for demonstration
    PATH_increase_increase = PathProcessor([ModelsA_increasing, ModelsB_increasing])
    PATH_decrease_increase = PathProcessor([ModelsA_decreasing, ModelsB_increasing])
    r_space = Models_generation.generate_r_space()
    r1 = np.array([r_space[i][0] for i in range(len(r_space))])
    r2 = np.array([r_space[i][1] for i in range(len(r_space))])
    f2_PATH_increase_increase = []
    f2_PATH_decrease_increase = []
    # f2_PATH_increase_increase = PATH_increase_increase.process(r1=r1, r2=r2)
    # f2_PATH_decrease_increase = PATH_decrease_increase.process(r1=r1, r2=r2)
    for j in tqdm.tqdm(range(len(r_space))):
        r1 = np.array([r_space[j][0]])
        r2 = np.array([r_space[j][1]])
        f2_PATH_increase_increase.append(PATH_increase_increase.process(r1=r1, r2=r2))
        f2_PATH_decrease_increase.append(PATH_decrease_increase.process(r1=r1, r2=r2))
    trade_off.plot_trade_off_pure_mono(f2_PATH_increase_increase, r_space, given_f = 50)
    trade_off.plot_trade_off_diff_mono(f2_PATH_increase_increase, f2_PATH_decrease_increase, r_space, given_f = 50, if_just_line = True)
    trade_off.plot_trade_off_diff_mono(f2_PATH_increase_increase, f2_PATH_decrease_increase, r_space, given_f = 50, if_just_line = False)

if __name__ == "__main__":
    main()