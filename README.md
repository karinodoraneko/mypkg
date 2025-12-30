# battery-simulationコマンド

![test](https://github.com/karinodoraneko/mypkg/actions/workflows/test.yml/badge.svg)

ROS2を用いて、ロボットなど機械のバッテリー残量の変化と、残量低下時の警告アラートをシミュレートするパッケージです。

* **battery**: バッテリー残量（100%から開始）をトピックとして配信し、時間経過とともに減少させます。
* **listener**: バッテリー残量を購読し、残量が30%を下回ると警告ログを出力します。

## 使い方
### 実行方法
```
$ ros2 launch mypkg talk_listen.launch.py
```

### 出力例
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
- Ubuntu 24.04 LTS

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Yuto Matsushima

## 謝辞
- 参考文献
  - [ryuichiueda/my_slides robosys_2025](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2025)
