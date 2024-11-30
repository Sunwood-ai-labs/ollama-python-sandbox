"""
モデルのダウンロードサンプル

このスクリプトは、Ollamaからモデルをダウンロードし、
進捗状況をプログレスバーで表示します。
"""

from tqdm import tqdm
from ollama import pull


def main():
    current_digest, bars = '', {}
    
    # モデルのダウンロードを開始
    for progress in pull('llama3.2', stream=True):
        digest = progress.get('digest', '')
        
        # 新しいレイヤーの開始時に前のプログレスバーを閉じる
        if digest != current_digest and current_digest in bars:
            bars[current_digest].close()

        # ステータスメッセージの表示
        if not digest:
            print(progress.get('status'))
            continue

        # 新しいレイヤーのプログレスバーを作成
        if digest not in bars and (total := progress.get('total')):
            bars[digest] = tqdm(
                total=total,
                desc=f'ダウンロード中 {digest[7:19]}',
                unit='B',
                unit_scale=True
            )

        # プログレスバーの更新
        if completed := progress.get('completed'):
            bars[digest].update(completed - bars[digest].n)

        current_digest = digest


if __name__ == '__main__':
    main()
