"""
画像を含むチャットのサンプル

このスクリプトは、画像とテキストを組み合わせた
マルチモーダルなチャットの方法を示します。
"""

from ollama import chat

# 画像パスの入力を受け付け
path = input('画像ファイルのパスを入力してください: ')

# 画像を含むチャットの実行
response = chat(
    model='llama3.2-vision',
    messages=[
        {
            'role': 'user',
            'content': 'この画像に何が写っていますか？簡潔に答えてください。',
            'images': [path],
        }
    ],
)

print(response.message.content)
