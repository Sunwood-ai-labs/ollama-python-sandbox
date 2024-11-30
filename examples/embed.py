"""
テキストの埋め込みベクトル生成のサンプル

このスクリプトは、テキストを数値ベクトルに変換する方法を示します。
生成された埋め込みベクトルは、テキストの意味的な類似性の計算などに使用できます。
"""

from ollama import embed

# テキストの埋め込みベクトルを生成
response = embed(model='llama3.2', input='Hello, world!')
print(response['embeddings'])
