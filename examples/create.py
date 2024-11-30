"""
カスタムモデルの作成サンプル

このスクリプトは、Modelfileを使用してカスタムモデルを作成する方法を示します。
既存のモデルをベースに、新しい特性を持つモデルを作成できます。
"""

import sys
from ollama import create

args = sys.argv[1:]
if len(args) == 2:
    # ローカルファイルからモデルを作成
    path = args[1]
else:
    print('使用法: python create.py <モデル名> <Modelfileのパス>')
    sys.exit(1)

# モデルファイルの定義
modelfile = f"""
FROM {path}
"""

# サンプルのModelfile
example_modelfile = """
FROM llama3.2
# 温度パラメータを1に設定（高いほど創造的、低いほど一貫性のある出力）
PARAMETER temperature 1
# コンテキストウィンドウサイズを4096に設定
PARAMETER num_ctx 4096

# カスタムシステムメッセージの設定
SYSTEM You are Mario from super mario bros, acting as an assistant.
"""

# モデルの作成（進捗をストリーミング表示）
for response in create(model=args[0], modelfile=modelfile, stream=True):
    print(response['status'])
