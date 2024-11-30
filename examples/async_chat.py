"""
非同期チャット機能のサンプル

このスクリプトは、asyncioを使用して非同期でチャットを実行する方法を示します。
メインのプログラムフローをブロックせずにAIモデルと対話できます。
"""

import asyncio
from ollama import AsyncClient


async def main():
    # チャットメッセージの準備
    messages = [
        {
            'role': 'user',
            'content': 'Why is the sky blue?',  # 「空が青い理由は？」という質問
        },
    ]

    # 非同期クライアントの作成
    client = AsyncClient()
    # 非同期でチャットを実行
    response = await client.chat('llama3.2', messages=messages)
    print(response['message']['content'])


if __name__ == '__main__':
    asyncio.run(main())
