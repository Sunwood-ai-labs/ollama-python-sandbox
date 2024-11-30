# Ollama Python サンプルコード集

このディレクトリには、Ollama PythonライブラリのAPIを試すための様々なサンプルコードが含まれています。

## サンプル一覧

### チャット系
- [chat.py](chat.py) - 基本的なチャット機能
- [async_chat.py](async_chat.py) - 非同期でのチャット
- [chat_stream.py](chat_stream.py) - ストリーミング形式でのチャット
- [chat_with_history.py](chat_with_history.py) - 会話履歴を保持するチャット

### テキスト生成系
- [generate.py](generate.py) - 基本的なテキスト生成
- [async_generate.py](async_generate.py) - 非同期でのテキスト生成
- [generate_stream.py](generate_stream.py) - ストリーミング形式でのテキスト生成
- [fill_in_middle.py](fill_in_middle.py) - 文章の途中を補完

### ツール/関数呼び出し系
- [tools.py](tools.py) - ツール/関数呼び出しの基本例
- [async_tools.py](async_tools.py) - 非同期でのツール/関数呼び出し

### 画像認識系
- [multimodal_chat.py](multimodal_chat.py) - 画像を含むチャット
- [multimodal_generate.py](multimodal_generate.py) - 画像からのテキスト生成

### モデル管理系
- [list.py](list.py) - ダウンロード済みモデルの一覧表示
- [ps.py](ps.py) - モデルのステータス表示
- [pull.py](pull.py) - モデルのダウンロード
- [create.py](create.py) - カスタムモデルの作成

### その他
- [embed.py](embed.py) - テキストの埋め込みベクトル生成

## 実行方法

