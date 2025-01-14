import os
import subprocess
from typing import List, Tuple
import sys
from pathlib import Path

class FileTransfer:
    def __init__(self, server: str, username: str, local_path: str, identity_file: str = None):
        self.server = server
        self.username = username
        self.local_path = Path(local_path)
        self.identity_file = identity_file
        
        # 创建本地目录如果不存在
        self.local_path.mkdir(parents=True, exist_ok=True)
        
    def transfer_file(self, remote_path: str, filename: str) -> bool:
        """
        传输单个文件
        返回: 是否传输成功
        """
        try:
            remote_full_path = f"{self.username}@{self.server}:{remote_path}/{filename}"
            local_full_path = self.local_path / filename
            
            print(f"正在传输: {filename}")
            print(f"从: {remote_full_path}")
            print(f"到: {local_full_path}")
            
            # 构建scp命令
            cmd = ["scp"]
            if self.identity_file:
                cmd.extend(["-i", self.identity_file])
            cmd.extend([remote_full_path, str(local_full_path)])
            
            # 执行传输
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✓ {filename} 传输成功\n")
                return True
            else:
                print(f"✗ {filename} 传输失败")
                print(f"错误信息: {result.stderr}\n")
                return False
                
        except Exception as e:
            print(f"传输出错: {str(e)}\n")
            return False

def main():
    # 配置信息
    SERVER = "10.184.17.211"  # 服务器IP地址
    USERNAME = "yquan"        # 用户名
    LOCAL_PATH = r"C:\Users\19160\Desktop\wsycopy\1219"  # 本地保存路径
    IDENTITY_FILE = r"C:\Users\19160\Desktop\id_rsa"  # SSH私钥文件路径
    
    # 要传输的文件列表：(远程路径, 文件名)
    FILES_TO_TRANSFER: List[Tuple[str, str]] = [
        ("/data/yquan/llm-mcts/mcts/virtualhome", "llm_model.py"),
        ("/data/yquan/llm-mcts/mcts/virtualhome", "llm_policy.py"),
        ("/data/yquan/llm-mcts/mcts/virtualhome", "mcts_agent.py"),
        ("/data/yquan/llm-mcts/mcts/virtualhome", "belief.py"),
        ("/data/yquan/llm-mcts/mcts/virtualhome/mcts", "mcts.py"),
        # 在这里添加更多文件，格式: (远程路径, 文件名)
    ]
    
    # 创建传输器
    transfer = FileTransfer(SERVER, USERNAME, LOCAL_PATH, IDENTITY_FILE)
    
    # 统计
    total = len(FILES_TO_TRANSFER)
    success = 0
    failed = []
    
    # 开始传输
    print(f"开始传输 {total} 个文件...")
    print("-" * 50)
    
    for remote_path, filename in FILES_TO_TRANSFER:
        if transfer.transfer_file(remote_path, filename):
            success += 1
        else:
            failed.append(filename)
    
    # 打印总结
    print("=" * 50)
    print(f"传输完成！")
    print(f"总计: {total} 个文件")
    print(f"成功: {success} 个")
    print(f"失败: {len(failed)} 个")
    
    if failed:
        print("\n传输失败的文件:")
        for filename in failed:
            print(f"- {filename}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n传输被用户中断")
    finally:
        print("\n按回车键退出...")
        input()