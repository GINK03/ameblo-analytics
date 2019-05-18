# Ameblo Analytics

## データ
 - 2019/05/10からの過去のアメブロのスナップショット  
 - 1000万レコード
 
## ダウンロード
  - TODO: DropBox Link
  
## 何を分析する: Ideas

### 埼玉県民とそれ以外の違い
埼玉県民とそれ以外を分類を行おうとすると、 `AUC 0.503` で実際はほとんど分類できない。  
分類性能は悪いが、その判断基準となった特徴量がユニークで面白い。  

埼玉県民のコーパスの特徴として「池袋」が入っているとそれらしいという結果になっており、実質的に池袋は埼玉県民の土地であるということがわかる。  

<div align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/57965999-3350f400-7987-11e9-8d47-aa0d8b543420.png">
</div>

### 男女の分類
男女の分類で見ると、 `AUC 0.741` になり、そこそこの性能で分類できる。  

男性言葉、女性言葉が分類用の特徴量として目立っており、どんな言葉を使えば男性らしく、女性らしく統計的になるのかわかります。  
<div align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/57966001-35b34e00-7987-11e9-8d7d-7b6922fb0153.png">
</div>

### 1988年生以前生まれと以後生まれ
勝手に若いというを1988以前, 1988以降の生まれの人の記事の分類をすると、 `AUC 0.681` で分類できる

おそらく携帯電話の頭である090が最もわかりやすい特徴量になっていることや、文章中の `〜` も年寄りくさいな、、、と思っていたのですがそういう結果になりました。  

Twitterは若者のSNSツール、そうだね。  

<div align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/57966002-377d1180-7987-11e9-8a44-9165074f193b.png">
</div>

## 結局流行語（大賞）は長生きするのか

見ていきましょう

### 壁ドン（2014年）

<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969312-bc305580-79b0-11e9-90dc-f46bfc166300.png">
 <div> 図1. 壁ドン </div>
</div>


## 妖怪ウォッチ(2014年)
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969328-eda92100-79b0-11e9-9e8b-c4051998567d.png">
 <div> 図2. 妖怪ウォッチ </div>
</div>
