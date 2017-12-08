import requests
import os


def downLoadImg(url, dir='/ky/data/wechatImg'):
    ir = requests.get(url)
    if ir.status_code == 200:
        (filepath, filename) = os.path.split(url)
        newfile = os.path.join(dir, filename)
        open(newfile, 'wb').write(ir.content)
        return newfile


if __name__ == '__main__':
    downLoadImg('https://avatars1.githubusercontent.com/u/4088439?s=460&v=4')
