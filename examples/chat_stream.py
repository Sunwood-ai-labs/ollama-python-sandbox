"""
ストリーミング形式でのチャット機能のサンプル

このスクリプトは、応答をリアルタイムで受け取り、
徐々に表示する方法を示します。
"""

from ollama import chat

# チャットメッセージの準備
messages = [
    {
        'role': 'user',
        'content': 'Why is the sky blue?',  # 「空が青い理由は？」という質問
    },
]

# ストリーミングモードでチャットを実行
for part in chat('llama3.2', messages=messages, stream=True):
    # 応答を逐次表示
    print(part['message']['content'], end='', flush=True)

print()  # 最後に改行を入れる
