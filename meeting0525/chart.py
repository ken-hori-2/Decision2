from graphviz import Digraph

G = Digraph(format="png")

G.attr("node", shape="box", width="1", color="orange")

G.node("start", shape="oval", color="pink")
G.node("注文を確認")
G.node("注文情報に問題はある？", shape="diamond", color="yellow")
G.node("在庫チェック")
G.node("在庫はある？", shape="diamond", color="yellow")
G.node("配送")
G.node("配送伝票番号の入力")
G.node("購入者へメール通知")
G.node("end", shape="oval", color="gray")

G.edge("start", "注文を確認")
G.edge("注文を確認", "注文情報に問題はある？", label="     ")
G.edge("注文情報に問題はある？", "注文を確認", label=" ある")
G.edge("注文情報に問題はある？", "在庫チェック", label=" ない")
G.edge("在庫チェック", "在庫はある？", label="     ")
G.edge("在庫はある？", "在庫チェック", label=" ない")
G.edge("在庫はある？", "配送", label=" ある")
G.edge("配送", "配送伝票番号の入力")
G.edge("配送伝票番号の入力", "購入者へメール通知")
G.edge("購入者へメール通知", "end")

G.render("order_state")