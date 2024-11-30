"""
画像からのテキスト生成サンプル

このスクリプトは、xkcdウェブコミックの画像を取得し、
その内容についてAIモデルに説明させる方法を示します。
"""

import sys
import random
import httpx
from ollama import generate


def main():
    # 最新のxkcdコミックの情報を取得
    latest = httpx.get('https://xkcd.com/info.0.json')
    latest.raise_for_status()

    # コミック番号の指定または乱数生成
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = random.randint(1, latest.json().get('num'))

    # 指定したコミックの情報を取得
    comic = httpx.get(f'https://xkcd.com/{num}/info.0.json')
    comic.raise_for_status()

    print(f'xkcd #{comic.json().get("num")}: {comic.json().get("alt")}')
    print(f'リンク: https://xkcd.com/{num}')
    print('---')

    # コミックの画像を取得
    raw = httpx.get(comic.json().get('img'))
    raw.raise_for_status()

    # 画像の説明をストリーミングで生成
    for response in generate('llava', 'このコミックを説明してください:', images=[raw.content], stream=True):
        print(response['response'], end='', flush=True)

    print()


if __name__ == '__main__':
    main()
