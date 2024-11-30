"""
テキストの途中補完サンプル

このスクリプトは、与えられたプレフィックスとサフィックスの間を
AIモデルが補完する方法を示します。特にコード生成に有用です。
"""

from ollama import generate

# 関数の定義の開始部分
prefix = '''def remove_non_ascii(s: str) -> str:
    """ '''

# 関数の終了部分
suffix = """
    return result
"""

# 途中を補完
response = generate(
    model='codellama:7b-code',
    prompt=prefix,
    suffix=suffix,
    options={
        'num_predict': 128,  # 生成するトークンの最大数
        'temperature': 0,    # 決定論的な出力を得るため0に設定
        'top_p': 0.9,       # サンプリングのための閾値
        'stop': ['< EOT >'], # 生成停止のトリガー
    },
)

print(response['response'])
