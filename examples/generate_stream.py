"""
ストリーミング形式でのテキスト生成サンプル

このスクリプトは、生成されたテキストをリアルタイムで
受け取って表示する方法を示します。
"""

from ollama import generate

# ストリーミングモードでテキスト生成
for part in generate('llama3.2', 'Why is the sky blue?', stream=True):
    # 生成されたテキストを逐次表示
    print(part['response'], end='', flush=True)
