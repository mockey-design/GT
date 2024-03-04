## About graph_edit2.py

#Overview

このスクリプトは、センサーデータの処理と可視化を行う。

CSVファイルからセンサーデータを読み込み、特定のセンサーペア間でデータを交換し、特定のセンサーカラムを削除した後、残りのセンサーカラムの名前をSensor Data 1から４６の順に命名し直す。

#System

*センサーデータの読み込みと前処理　

*指定されたセンサーペア間でのデータの交換　

*特定のセンサーカラムの削除と残りのカラムのリネーム　

*センサーごとにグループ化されたデータの可視化と2x3のサブプロットグリッドへのプロット　　

*可視化されたデータの高解像度PNGファイルへの保存

#Command

```
python3 graph_edit2.py <csvファイルへのパス>
```

#Requirments

Python 3

Pandas

Matplotlib

Numpy

#出力

updated_log_228.csvという名前の修正されたCSVファイル

sensor_plot.pngという名前のセンサーデータのプロットを含むPNGファイル

これらの出力ファイルは入力ファイルと同じディレクトリ上に出力される。

##graph_edit2.ipynbはgraph_edit2.pyのipynb形式
