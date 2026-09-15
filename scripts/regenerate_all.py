import os
import shutil

def clean_old_files():
    print("正在清理旧的markdown文件...")
    for root, dirs, files in os.walk("../docs"):
        if "public" in root:
            continue
        for file in files:
            if file.endswith(".md") and file != "index.md":
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"已删除: {file_path}")
    
    print("\n正在清理旧的_meta.json文件...")
    for root, dirs, files in os.walk("../docs"):
        if "public" in root:
            continue
        for file in files:
            if file == "_meta.json":
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"已删除: {file_path}")
                except:
                    pass

if __name__ == "__main__":
    clean_old_files()
    print("\n清理完成！")
    print("\n请运行以下命令重新生成文件：")
    print("cd scripts && python json_to_md.py")
    print("cd scripts && python gen_meta.py")