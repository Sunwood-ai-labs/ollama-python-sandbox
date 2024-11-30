"""
ダウンロード済みモデルの一覧表示サンプル

このスクリプトは、ローカルにダウンロードされている
すべてのモデルとその詳細情報を表示します。
"""

from ollama import list
from ollama import ListResponse

# モデル一覧の取得
response: ListResponse = list()

# 各モデルの情報を表示
for model in response.models:
    print('モデル名:', model.model)
    print('  サイズ (MB):', f'{(model.size.real / 1024 / 1024):.2f}')
    if model.details:
        print('  フォーマット:', model.details.format)
        print('  モデルファミリー:', model.details.family)
        print('  パラメータサイズ:', model.details.parameter_size)
        print('  量子化レベル:', model.details.quantization_level)
    print('\n')
