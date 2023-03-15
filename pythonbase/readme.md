# Python標準テンプレート

## 使用するツール

- poetry: 仮想環境
- black: フォーマッタ
- flake8: リンター
- pytest: テストランナー
- mypy: 静的型検査
- make: タスクランナー

## コードスタイル

- [PEP8](https://peps.python.org/pep-0008/)に準拠する
  - [和訳](https://pep8-ja.readthedocs.io/ja/latest/)も参照
- ただし、Maximum Line Lengthだけは120文字とする
  - 79文字は逆に読みづらい(と思う)ので
  - PEP8にもA Foolish Consistency is the Hobgoblin of Little Mindsと書いているので許してもらう

## Type Hints

- できるだけType Hints(PEP0484)を記載する
  - 3.9以降が使える場合は3.9以降の書き方で記載する

## テストの書き方

- Arrange(準備)、Act(実行)、Assert(検証)のAAAパターンに沿って記載し、AAAの間は空行もしくはコメントを記載する