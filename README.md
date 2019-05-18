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

## サービスのユーザの人口の高齢化
[ニコニコ動画も高齢化しているというデータがある](https://togetter.com/li/974789)ように、実はアメブロでも同様の老化が起きていることがわかっている。  
ユーザプロフィールと登録している生年月日を突合すると、ブログを書いたときの平均年齢が逆算できる。  
その時の平均の年齢を `age` とすると、このようなグラフになる  
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970599-24d1ff00-79be-11e9-8b1e-8a645e6a8b67.png">
 <div> 図X. 年齢の経年変化 </div>
</div>
ほぼサービス人口の年齢が新陳代謝してない 

## 結局流行語（大賞）は長生きするのか

見ていきましょう

### 壁ドン（2014年）

<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969312-bc305580-79b0-11e9-90dc-f46bfc166300.png">
 <div> 図1. 壁ドン </div>
</div>


### 妖怪ウォッチ(2014年)
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969328-eda92100-79b0-11e9-9e8b-c4051998567d.png">
 <div> 図2. 妖怪ウォッチ </div>
</div>

### 爆買い(2015年)
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970404-e89d9f00-79bb-11e9-8010-03460ae08c0a.png">
 <div> 図X. 爆買い </div>
</div>

### PPAP(2016年)
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970248-00742380-79ba-11e9-98b2-4e118b6ae439.png">
 <div> 図X. PPAP </div>
</div>

## 最近気になるキーワード
### マッチングアプリ
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969627-14b52200-79b4-11e9-8b03-661db001cfb7.png">
 <div> 図X. マッチングアプリ </div>
</div>

## 周期性のあるキーワード
### 花粉症 
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970699-775feb00-79bf-11e9-9bb2-cd769531fe16.png">
 <div> 図X. 花粉症 </div>
</div>

### PM2.5 
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970716-aaa27a00-79bf-11e9-9cbf-901bd72a4284.png">
 <div> 図X. PM2.5 </div>
</div>

## TV,新聞に対して、SNS各種は継続して人気が上がり続ける
ブロードキャスト型のコンテンツのテレビに対して、twitter, facebook, line, youtube, instagramなどは人気が上がり続けている  

### Twitter
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969694-96a54b00-79b4-11e9-8bcc-dc500fe5602d.png">
 <div> 図X. Twitter </div>
</div>

### Facebook
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969696-a15fe000-79b4-11e9-8190-d1605e8b7b79.png">
 <div> 図X. Facebook</div>
</div>

### line
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969701-ae7ccf00-79b4-11e9-9656-3137090c1291.png">
 <div> 図X. line</div>
</div>

### インスタグラム
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969705-bc325480-79b4-11e9-86c8-fdf0c2d13798.png">
 <div> 図X. インスタグラム</div>
</div>

### YouTube
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970318-c35c6100-79ba-11e9-9fb8-e60634415032.png">
 <div> 図X. YouTube</div>
</div>

### テレビ
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969958-17b11200-79b6-11e9-9c2a-5c1cd5d15ca8.png">
 <div> 図X. テレビ </div>
</div>

### 新聞
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970292-82fce300-79ba-11e9-9bc7-2aef8a78124f.png">
 <div> 図X. 新聞 </div>
</div>

