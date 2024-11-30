"""
非同期テキスト生成のサンプル

このスクリプトは、asyncioを使用して非同期でテキストを生成する方法を示します。
プロンプトから文章を生成する際に、非同期処理を活用します。
"""

import asyncio
import ollama


async def main():
    # 非同期クライアントの作成
    client = ollama.AsyncClient()
    # プロンプトを指定してテキストを生成
    response = await client.generate('llama3.2', 'Why is the sky blue?')
    print(response['response'])


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nGoodbye!')
