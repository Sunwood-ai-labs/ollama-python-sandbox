"""
基本的なテキスト生成のサンプル

このスクリプトは、プロンプトからテキストを生成する
最も基本的な使用方法を示します。
"""

from ollama import generate

# プロンプトを指定してテキストを生成
response = generate('llama3.2', 'Why is the sky blue?')
print(response['response'])
