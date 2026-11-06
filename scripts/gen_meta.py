import json
import os
def gen_index_meta():
    for dir in os.listdir("../docs"):
        if dir == "public":
            continue
        if os.path.isfile(f"../docs/{dir}"):
            continue
        subdirs = [i for i in os.listdir(f"../docs/{dir}") if os.path.isdir(f"../docs/{dir}/{i}")]
        # 没有子目录的分类（如 ogden_basic_english）使用页面级 _meta.json，不生成分类元数据
        if not subdirs:
            continue
        lst = [
            {
                "type": "file",
                "name": "index",
                "label": "章节预览"
            }
        ]

        for i in subdirs:
            lst.append({
                "type": "dir",
                "name": i,
                "label": i,
                "collapsed": True,
                "overviewHeaders": [1]
            })
        with open(f"../docs/{dir}/_meta.json", "w", encoding="utf-8") as f:
            json.dump(lst, f, ensure_ascii=False, indent=2)


def gen_md_meta():
    for roots, dirs, files in os.walk("../docs"):
        for file in files:
            if file.endswith(".md") and file != "index.md":
                # # 删除旧的_meta.json文件
                # if os.path.exists(f"{roots}/_meta.json"):
                #     os.remove(f"{roots}/_meta.json")
                if not os.path.exists(f"{roots}/_meta.json"):
                    with open(f"{roots}/_meta.json", "w", encoding="utf-8") as f:
                        json.dump([os.path.splitext(file)[0]], f, ensure_ascii=False, indent=2)

                else:
                    with open(f"{roots}/_meta.json", "r", encoding="utf-8") as f:
                        lst = json.load(f)
                    if os.path.splitext(file)[0] not in lst:
                        lst.append(os.path.splitext(file)[0])
                        lst = sorted(lst, key=lambda x: int(x.split("_")[0]) if "_" in x else float('inf'))
                        with open(f"{roots}/_meta.json", "w", encoding="utf-8") as f:
                            json.dump(lst, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    gen_index_meta()
    gen_md_meta()