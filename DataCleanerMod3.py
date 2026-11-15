import pandas as pd


sensor_columns = ['acc_x','acc_y','acc_z',
                'gyr_x','gyr_y','gyr_z',
                'grav_x','grav_y','grav_z']
rate_hz = 50          # contract: Module 2 delivers 50 Hz
min_duration = 280    # 5 min chunk, 10s dropped at each edge

def clean_table(df):
    """
    Input:  one merged df (Module 2 output)
    Output: one cleaned copy; input is not modified
    """

    # 1. make sure the df actually exists and has something
    assert not df.empty, "no data at all..."
    
    # 2. sort by time
    df = df.sort_values('seconds_elapsed').reset_index(drop=True)

    # 3. drop first 10s and last 10s
    t_min = df['seconds_elapsed'].min()
    t_max = df['seconds_elapsed'].max()
    df = df[(df['seconds_elapsed'] > t_min + 10) &
            (df['seconds_elapsed'] < t_max - 10)]
    duration = df['seconds_elapsed'].max() - df['seconds_elapsed'].min()

    # 4. drop NaN in sensor columns only
    df = df.dropna(subset=sensor_columns)

    # 5. checks for usability
    assert not df.empty, "no rows left after cleaning"
    expected_rows = rate_hz * duration * 0.9   # maximum of 10% data dropout
    assert duration >= min_duration, f"duration too short: {duration}"
    assert len(df) >= expected_rows, f"rows too few: {len(df)} < {expected_rows}"

    # 6. return for mod 4
    return df.reset_index(drop=True)
