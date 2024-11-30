"""
モデルのステータス表示サンプル

このスクリプトは、現在実行中のモデルの状態と
リソース使用状況を表示します。
"""

from ollama import ps, pull, chat
from ollama import ProcessResponse

# テスト用にモデルをロード
print('モデルをロード中...')
response = pull('llama3.2', stream=True)
progress_states = set()
for progress in response:
    if progress.get('status') in progress_states:
        continue
    progress_states.add(progress.get('status'))
    print(progress.get('status'))

print('\n')

print('モデルの読み込みを待機中... \n')
chat(model='llama3.2', messages=[{'role': 'user', 'content': 'こんにちは'}])

# プロセス情報の取得と表示
response: ProcessResponse = ps()
for model in response.models:
    print('モデル名: ', model.model)
    print('  ダイジェスト: ', model.digest)
    print('  有効期限: ', model.expires_at)
    print('  サイズ: ', model.size)
    print('  VRAM使用量: ', model.size_vram)
    print('  詳細情報: ', model.details)
    print('\n')
