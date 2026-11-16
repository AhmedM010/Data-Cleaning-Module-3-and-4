import numpy as np

sensor_columns = ['acc_x','acc_y','acc_z',
                'gyr_x','gyr_y','gyr_z',
                'grav_x','grav_y','grav_z']

def window_cutting (df):
    # 1. set the variables
    values = df[sensor_columns].values
    window_size = 128
    step = 64
    windows = []

    # 2. cutting df into 128 sample windows at 64 step
    for sample in range(0, len(values) - window_size + 1, step):
        windows.append(values[sample:sample + window_size])

    # 3. check if the windows were made
    assert len(windows) > 0, "no windows were made: not enough samples"

    # 4. convert in array
    windows = np.array(windows)

    # 5. check the shape of the windows is (n, 128, 9)
    assert windows.shape[1:] == (128, 9), f"bad shape: {windows.shape}"  

    # 6. return
    return windows

