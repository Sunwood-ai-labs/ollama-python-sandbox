"""
会話履歴を保持するチャットのサンプル

このスクリプトは、過去の会話履歴を保持しながらチャットを行う方法を示します。
モデルは過去のやり取りを考慮して応答を生成します。
"""

from ollama import chat

# 初期の会話履歴
messages = [
    {
        'role': 'user',
        'content': 'Why is the sky blue?',  # 「空が青い理由は？」
    },
    {
        'role': 'assistant',
        'content': "The sky is blue because of the way the Earth's atmosphere scatters sunlight.",
    },
    {
        'role': 'user',
        'content': 'What is the weather in Tokyo?',  # 「東京の天気は？」
    },
    {
        'role': 'assistant',
        'content': '東京の気候は夏は暖かく湿度が高く、冬は比較的穏やかです。',
    },
]

# 対話ループ
while True:
    user_input = input('チャット入力 (終了するにはCtrl+C): ')
    response = chat(
        'llama3.2',
        messages=messages + [
            {'role': 'user', 'content': user_input},
        ],
    )

    # 会話履歴に新しい対話を追加
    messages += [
        {'role': 'user', 'content': user_input},
        {'role': 'assistant', 'content': response.message.content},
    ]
    print(response.message.content + '\n')
