# 第1章 コンピュータネットワークの基本要素

## この章で学ぶこと

- 1.1 ノード
- 1.2 リンク
- 1.3 パケット
- 1.4 パケット転送
- 1.5 可視化

## 学習メモ

- **クラス／インスタンス（オブジェクト）／メソッド／self の関係**
  - クラスは設計図、インスタンス（オブジェクト）はそこから実際に作られた実体。`node1`, `node2`, `link`はそれぞれ`Node`, `Link`のインスタンス。
  - `self`は「今実行されているメソッドが、どのインスタンスに対して呼ばれたか」で毎回決まり直す。クラスをまたいで共有される固定の値ではない。
  - あるメソッドの中の`self`を別オブジェクトのメソッドに引数として渡すと、渡された側ではそれが普通の引数（別名）として受け取られる（例: `Link.__init__`内の`node_x.add_link(self)` → `add_link`側では`link`という名前で受け取る）。
- **Node**: `node_id`, `address`, `links`を持つ。`add_link`で自分につながった`Link`を記録する。
- **Link**: `node_x`, `node_y`の2つの`Node`を保持。`__init__`の中で両ノードの`add_link`を呼び出し、双方に「自分（このLink）」を登録させる。
- **Packet**: `source`, `destination`, `payload`を持つだけのデータの入れ物。
- **パケット転送の流れ**: `send_packet`は宛先が自分のアドレスと一致するかをまず見る。一致すれば即座に`receive_packet`で受信処理。一致しなければ`self.links`の中身を見て`link.transfer_packet(packet, self)`を呼び、`transfer_packet`は送信元と逆側のノード（`next_node`）の`receive_packet`を呼ぶ。
- **現状の制限（あとで直す想定）**: `send_packet`の`for link in self.links: ... break`は、宛先に近いリンクを探しているわけではなく、無条件に`self.links`の最初の1本を使うだけ。リンクが1本しかない今の構成では結果的に正しく動くが、ノードが複数のリンクを持つようになると破綻する。宛先を見て正しいリンクを選ぶルーティングは未実装（後の章で対応する見込み）。
- **NetworkGraph（可視化）**: `networkx`の`Graph`をラップしたクラス。`add_node`/`add_link`は中身を`self.graph`（=`networkx`のGraphインスタンス）に委譲するだけ。同じ名前のメソッドが2つのクラスにあるが、`self.add_node`を呼ぶのではなく`self.graph.add_node`を呼んでいるので再帰ではない（別オブジェクトの別メソッド）。
- `Node`/`Link`の`__init__`が`network_graph`を受け取り、生成時に自分自身を`network_graph.add_node`/`add_link`に登録するようになった。
- `draw()`は帯域幅を線の太さ、遅延を線の色にマッピングして`matplotlib`で描画する。`plt.show()`はGUIウィンドウを表示してそこで処理がブロックされる。

## チェックポイント（gitタグ）

コードは `simulator/` にまとめて実装する。節が完成するたびにコミット＋タグを打って、ここに対応を記録する。

| 節 | タグ | 内容 |
| --- | --- | --- |
| 1.1 | `ch01-1.1` | Nodeクラスの基本実装（node_id, address, links） |
| 1.2〜1.4.3 | `ch01-1.4.3` | Link/Packetクラス、add_link、send_packet/receive_packet/transfer_packetによるパケット転送（ルーティングは未実装） |
| 1.5 | `ch01-1.5` | NetworkGraphによる可視化、Node/Linkがnetwork_graphに自分を登録するように変更 |

第1章はここまでで完了。次は演習課題。

## 演習課題

<!-- 演習課題の解答・考察をここに記録する。コードは `simulator/` 側、対応タグは `ch01-exercise` -->

## 気づき・疑問点

<!-- つまづいた点、もっと調べたい点などを記録する -->
