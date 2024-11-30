"""
ツール/関数呼び出しの基本サンプル

このスクリプトは、AIモデルが外部関数を呼び出す方法を示します。
数値計算を行う関数を定義し、モデルがそれらを適切に使用する例を示します。
"""

from ollama import chat
from ollama import ChatResponse


def add_two_numbers(a: int, b: int) -> int:
    """
    2つの数値を加算する関数

    引数:
        a (int): 1つ目の数値
        b (int): 2つ目の数値

    戻り値:
        int: 加算結果
    """
    return a + b


def subtract_two_numbers(a: int, b: int) -> int:
    """
    2つの数値を減算する関数
    """
    return a - b


# ツールの手動定義
subtract_two_numbers_tool = {
    'type': 'function',
    'function': {
        'name': 'subtract_two_numbers',
        'description': '2つの数値を減算',
        'parameters': {
            'type': 'object',
            'required': ['a', 'b'],
            'properties': {
                'a': {'type': 'integer', 'description': '1つ目の数値'},
                'b': {'type': 'integer', 'description': '2つ目の数値'},
            },
        },
    },
}

# チャットメッセージの準備
messages = [{'role': 'user', 'content': '3たす1は？'}]
print('質問:', messages[0]['content'])

# 利用可能な関数の辞書
available_functions = {
    'add_two_numbers': add_two_numbers,
    'subtract_two_numbers': subtract_two_numbers,
}

# チャットの実行
response: ChatResponse = chat(
    'llama3.1',
    messages=messages,
    tools=[add_two_numbers, subtract_two_numbers_tool],
)

if response.message.tool_calls:
    # 複数のツール呼び出しに対応
    for tool in response.message.tool_calls:
        # 関数が利用可能か確認して実行
        if function_to_call := available_functions.get(tool.function.name):
            print('関数呼び出し:', tool.function.name)
            print('引数:', tool.function.arguments)
            output = function_to_call(**tool.function.arguments)
            print('関数の出力:', output)
        else:
            print('関数', tool.function.name, 'が見つかりません')

    # ツール呼び出し結果をモデルに返す
    messages.append(response.message)
    messages.append({'role': 'tool', 'content': str(output), 'name': tool.function.name})

    # ツール呼び出しの結果を含めた最終応答を取得
    final_response = chat('llama3.1', messages=messages)
    print('最終応答:', final_response.message.content)
else:
    print('モデルはツールを使用しませんでした')
