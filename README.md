# Pythonで動かしながら学ぶ コンピュータネットワーク 学習記録

[『Ｐｙｔｈｏｎで動かしながら学ぶ　コンピュータネットワーク』（中山悠 著、講談社サイエンティフィク）](https://www.kspub.co.jp/book/detail/5402092.html) を読みながら、Pythonでコードを動かして学んだことをまとめるリポジトリです。

## 構成

本のシミュレータは章をまたいで同じクラス（`Node`, `Link`, `Packet` など）を改良し続ける1つのプログラムなので、コードは `simulator/` 1箇所にまとめて育てていきます。章ごとのフォルダ（`chXX_xxx/`）はコードを置かず、学習記録（`README.md`）専用です。

```
simulator/              # 育て続ける1つのネットワークシミュレータ本体
  Node.py
  Link.py
  Packet.py
  ...
ch01_basic_elements/
  README.md             # 学習メモ・節ごとのgitタグ対応表
ch02_network_and_time/
  README.md
...
```

### 節ごとの記録（gitタグ）

1.1, 1.2 のように節単位で「両方残したい」場合は、ファイルを複製せずgitのコミット＋タグで残します。

```bash
# 1.1が完成したら
git add -A
git commit -m "1.1: Node/Link/Packetを実装"
git tag ch01-1.1

# 1.2に進んで完成したら
git commit -m "1.2: 可視化を追加"
git tag ch01-1.2

# あとから1.1時点のコードを見る
git show ch01-1.1:simulator/Node.py
# 1.1と1.2の差分を見る
git diff ch01-1.1 ch01-1.2 -- simulator/
```

タグ名は `chXX-Y.Z`（節）、演習課題は `chXX-exercise` を使う。各章の`README.md`に節とタグの対応を記録する。

## 章一覧

| 章 | タイトル | 状態 | フォルダ |
| --- | --- | --- | --- |
| 第0章 | ネットワークの基礎知識 | - | - |
| 第1章 | コンピュータネットワークの基本要素 | 🚧 進行中 | [ch01_basic_elements](./ch01_basic_elements) |
| 第2章 | ネットワークと時間 | - | - |
| 第3章 | スイッチとMACアドレス | - | - |
| 第4章 | MACアドレス学習とループ回避 | - | - |
| 第5章 | IPパケットとフラグメント | - | - |
| 第6章 | ルーティングプロトコル | - | - |
| 第7章 | レイヤとカプセル化 | - | - |
| 第8章 | アドレスの問い合わせ | - | - |
| 第9章 | IPアドレスの配布と変換 | - | - |
| 第10章 | コネクションと信頼性 | - | - |
| 第11章 | 確認応答と再送制御 | - | - |
| 第12章 | 輻輳とウィンドウ制御 | - | - |
| 第13章 | 待ち行列と通信品質 | - | - |
| 第14章 | アプリケーションとデータ転送 | - | - |
| 第15章 | 暗号化と鍵交換 | - | - |

状態の凡例: 🚧 進行中 / ✅ 完了 / - 未着手

## セットアップ

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
 ## 更新
  .\venv\Scripts\Activate.ps1
  python simulator/main.py

    git add -A
  git commit -m "1.1: Nodeクラスを実装"
  git tag ch01-1.1
  git push
  git push origin ch01-1.1