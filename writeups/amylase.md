# Lambdaman

LRDUに1文字使うのは明らかに損なのでエンコーディングすることを考える。実際割とうまく行ってまあまあ短くなるまでが初日。  
それ以降はなんのアイデアもなく1日以上停滞する。ランキングに情報理論的な限界を超える答えが続々現れて圧縮の方針では絶対に勝てないことがわかるので1から考え直して日曜の夜になんとかランダムウォークのアイデアにたどり着く。チームの皆さんにはかなり懐疑的な意見をもらったが試すのはすぐなのでやってみたらlambdaman4が解けてしまい完全にこれが答えであること確信。  
乱択に使う乱数生成は実装が単純な方がいいので線形合同法を選択する。係数を探しにウィキペディアを見たところ next = (48271 * x) % (2 << 31 - 1) という定数項がいらない設定があったので、コードゴルフに有利ということでこれを採択。  
なんでこれでいいかを冷静に考えてみると、modが（メルセンヌ）素数で48271がおそらく原始根であるから周期が最大になっているのだろうということに気が付き、同じ条件を満たすパラメータであれば小さいほうがコードが縮むことを発見した。あとはプログラム書いてぶん回し。具体的な生成器のコードはosakが異常コードゴルフで縮めてたのでよく知りません。

# Efficiency
- 1: ソースコードを実行すると当然のように停止しないが、コードを読むと4倍しているコードを22回適用しているのではい
- 2: なんかでかいループが回っていそうだがその結果に0をかけていることを発見。このあたりで読解ゲーであることに気がつく
いくつか読んだけど自分で解かなかったのもある。7-11のSATソルバー使うやつとか。