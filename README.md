# mypkg
## battery simulation

![test](https://github.com/karinodoraneko/mypkg/actions/workflows/test.yml/badge.svg)

ROS2を用いて、ロボットなど機械のバッテリー残量の変化と、残量低下時の警告アラートをシミュレートするパッケージです。

## ノードとトピック
このパッケージには以下の2つのノードが含まれています。

### 1. battery
バッテリー残量をシミュレートするノードです。
* **Publisher**: 
    * トピック名: `battery_level`
    * メッセージ型: `std_msgs/msg/Int16`
    * 内容: バッテリー残量（100%から開始し、1秒ごとに1%ずつ減少）

### 2. listener
バッテリー残量を監視するノードです。
* **Subscriber**: 
    * トピック名: `battery_level`
    * メッセージ型: `std_msgs/msg/Int16`
    * 内容: `battery` ノードから受信した残量データ
    * 動作: 残量が30%を下回ると、警告（WARN）ログを出力します。

## 使い方
### 実行方法
```
$ ros2 launch mypkg battery_check.launch.py
```

### 実行例
実行すると、以下のようなログが端末に表示されます。残量が30%未満になると警告（WARN）が表示されます。
```
[INFO] [launch]: All log files can be found below ...
[INFO] [battery-1]: process started with pid [1234]
[INFO] [listener-2]: process started with pid [1235]
[INFO] [battery-1]: [battery] Battery: 100%
[INFO] [listener-2]: [listener] Battery Level: 100%
...
[INFO] [battery-1]: [battery] Battery: 30%
[INFO] [listener-2]: [listener] Battery Level: 30%
[INFO] [battery-1]: [battery] Battery: 29%
[WARN] [listener-2]: [listener] Low Battery! Level: 29%
```

## 動作環境
- Ubuntu 22.04 LTS

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Yuto Matsushima

## 謝辞
- 参考文献
  - [ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
