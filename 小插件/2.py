import numpy as np

def is_smooth(trajectory, velocity_threshold=1.0, acceleration_threshold=0.5):
    """
    判断一条轨迹是否平滑。通过计算相邻点的速度变化率和加速度变化率来确定平滑度。
    
    参数:
    - trajectory: [80, 2] 的数组，表示一条轨迹。
    - velocity_threshold: 速度变化率的阈值，超过该值认为不平滑。
    - acceleration_threshold: 加速度变化率的阈值，超过该值认为不平滑。
    
    返回:
    - bool: 如果轨迹平滑，返回 True；否则返回 False。
    """
    # 计算相邻点的速度（使用欧几里得距离）
    velocities = np.linalg.norm(np.diff(trajectory, axis=0), axis=1)
    
    # 计算相邻速度的变化率（加速度）
    accelerations = np.abs(np.diff(velocities))
    
    # 判断是否有速度变化率或加速度变化率超过阈值
    if np.any(velocities > velocity_threshold) or np.any(accelerations > acceleration_threshold):
        return False
    
    return True

def filter_smooth_trajectories(trajectories, velocity_threshold=1.0, acceleration_threshold=0.5):
    """
    过滤不平滑的轨迹。
    
    参数:
    - trajectories: [K, 80, 2] 的数组，表示 K 条轨迹。
    - velocity_threshold: 速度变化率的阈值。
    - acceleration_threshold: 加速度变化率的阈值。
    
    返回:
    - np.ndarray: 过滤后的平滑轨迹数组。
    """
    smooth_trajectories = []
    
    for trajectory in trajectories:
        if is_smooth(trajectory, velocity_threshold, acceleration_threshold):
            smooth_trajectories.append(trajectory)
    
    return np.array(smooth_trajectories)

# 示例使用
K = 100  # 假设有100条轨迹
trajectories = np.random.rand(K, 80, 2)  # 随机生成的轨迹数据

# 过滤平滑的轨迹
smooth_trajectories = filter_smooth_trajectories(trajectories, velocity_threshold=1.0, acceleration_threshold=0.5)

print(f"过滤后的平滑轨迹数: {smooth_trajectories.shape[0]}")
