import keyword

import argparse

parser = argparse.ArgumentParser(description='输入解析文件路径')
#type是要传入的参数的数据类型  help是该参数的提示信息
parser.add_argument('file_path', type=str, help='带解析的python文件路径')

args = parser.parse_args()

def code_analysis(file_path):
    """
    统计源文件的代码行数、注释行数、空白行数、有效代码行数、有效代码行的平均长度、
    最大缩进层级、if、for、while、try 等语句的数量和变量名列表、变量名的平均长度

    :param file_path: 源文件路径
    :return: 包含以上统计结果的字典
    """

    total_lines = 0      # 总行数
    comment_lines = 0    # 注释行数
    blank_lines = 0      # 空白行数
    code_lines = 0       # 代码行数
    code_length = 0      # 代码行的总长度
    max_indent = 0       # 最大缩进层级
    if_count = 0         # if 语句数量
    for_count = 0        # for 语句数量
    while_count = 0      # while 语句数量
    try_count = 0        # try 语句数量
    vars_list = []       # 变量名列表，但最后会用dict清洗
    vars_length = 0      # 变量名的总长度
    package_list= []     # 包列表，但最终会用dict清洗
    package_count = 0    # 包长度


    with open(file_path, 'r', encoding='utf8') as f:
        for line in f:
            total_lines += 1
            line = line.strip()
            if not line:
                blank_lines += 1
            elif line.startswith("#"):
                comment_lines += 1
            else:
                code_lines += 1
                code_length += len(line)

                # 统计最大缩进层级
                indent = len(line) - len(line.lstrip())
                if indent > max_indent:
                    max_indent = indent

                # 统计 if、for、while、try 等语句数量
                if line.startswith("if "):
                    if_count += 1
                elif line.startswith("for "):
                    for_count += 1
                elif line.startswith("while "):
                    while_count += 1
                elif line.startswith("try "):
                    try_count += 1

                # 分析包引用
                elif line.startswith("import "):
                    package_list += line.replace(',',' ').split()[1:]

                # TODO：部分包引用
                # elif line.startswith("from "):
                #     pass

                # 分析变量名
                words = line.split()
                for i in range(len(words)):
                    # 排除特殊字符
                    word = words[i].strip(":")
                    if len(word) > 0 and word.isidentifier() and not keyword.iskeyword(word) and not word in vars_list:
                        vars_list.append(word)
                        vars_length += len(word)

    package_dict = {k:v for k,v in enumerate(package_list)}
    vars_list = [each for each in vars_list if each not in package_list]
    var_dict = {k:v for k,v in enumerate(vars_list)}

    

    result = {"总行数": total_lines,
            "注释行数": comment_lines,
            "空白行数": blank_lines,
            "有效代码行数": code_lines,
            "包引用数量": len(package_dict),
            "引用包列表": package_dict.values(),
            "有效代码行的平均长度": code_length / code_lines if code_lines > 0 else 0,
            "最大缩进层级": max_indent,
            "if语句数量": if_count,
            "for语句数量": for_count,
            "while语句数量": while_count,
            "try语句数量": try_count,
            "变量名列表": var_dict.values(),
            "变量名的平均长度": vars_length / len(vars_list) if len(vars_list) > 0 else 0}

    return result

if __name__ == "__main__":
    result = code_analysis(args.file_path)
    for k,v in result.items():
        print(f"{k}:{v}")