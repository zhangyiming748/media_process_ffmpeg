#!/usr/bin/python
# 无法在Windows下正常运行
from glob import glob


def zh_ch2en_us(files):
    for file in files:
        print(file)
        f = open(file, 'r+')
        all_the_lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_the_lines:
            line = line.replace('，', ',')
            line = line.replace('。', '.')
            line = line.replace('（', '(')
            line = line.replace('）', ')')
            line = line.replace('“', '\"')
            line = line.replace('”', '\"')
            line = line.replace('：', ':')
            line = line.replace('；', ';')
            line = line.replace('？', '?')
            line = line.replace('！', '!')
            line = line.replace('《', '<')
            line = line.replace('》', '>')
            line = line.replace('【', '[')
            line = line.replace('】', ']')
            line = line.replace('、', '\\')
            line = line.replace('～', '~')
            f.write(line)
        f.close()
# 引用图片格式
# https://github.com/zhangyiming748/zhangyiming748.github.io/raw/master/img/fakeTPM/2.webp

if __name__ == '__main__':
    path = glob('*.md')
    print(path)
    zh_ch2en_us(path)
