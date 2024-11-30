"""
基本的なチャット機能のサンプル

このスクリプトは、Ollamaを使用して単純なチャットを実行する方法を示します。
単一の質問に対する応答を取得します。
"""

from ollama import chat

# チャットメッセージの準備
messages = [
    {
        'role': 'user',
        'content': 'Why is the sky blue?',  # 「空が青い理由は？」という質問
    },
]

# モデルとチャットを実行
response = chat('llama3.2', messages=messages)

# 応答の表示
print(response['message']['content'])
