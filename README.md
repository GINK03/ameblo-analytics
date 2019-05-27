# Ameblo Analytics

## 序
　国内最大級の自然言語のデータ・セットが一般ユーザがアクセスできる範囲であるものは2chとアメブロなどがあります。  
 アメブロは広大で数千万の投稿があると思われますが、全てをパースし切ることはできませんでした。（またしなくてもサンプルサイズ的に十分だという視点ではあります）  
 
 ユーザには女性が多く、後述するFaceBookやLineなどの浸透スピードを鑑みると、レートマジョリティに相当するメディアだと思われます。  
 
 せっかくいろいろ遊べそうなコーパスであるのに、どうにも使い勝手が良くなく何かを導くのにアイディアをひねる必要があります。  

## データ
 - 2019/05/10からの過去のアメブロのスナップショット  
 - 1272万記事
 - 142万人のプロフィール 
 
## ダウンロード
  - [ブログをパースしたもの](https://www.dropbox.com/s/wpl53r0tm0jh5i9/jsons_content_snapshot_20190510.tar.gz?dl=0)
  - [プロフィールをパースしたもの](https://www.dropbox.com/s/zc3nl0wx6b2o1s7/jsons_profile_snapshot_20190510.tar.gz?dl=0)
  
## コード
 基本的にはデータをダウンロードして `A, B, C, D, ...` の順序で実行していくことで再現できます(メモリが32GBは必要です)  
 
[GitHub](https://github.com/GINK03/ameblo-analytics)   
  
## 分析(集計)すること
 - 代表的な角度でのクラシフィケーション（分類）とその重要度
 - 流行語大賞は結局、その後も根付くのか
 - 周期性のあるキーワード
 - TV,新聞の衰退と、SNSやYouTubeの躍進

## こういった大規模コーパスで分類するのに向いている疎行列 + Stochastic Gradient Descent  
[Andrew NGさんが説明しているStochastic Gradient Descentの動画](https://www.youtube.com/watch?v=W9iWNJNFzQI)がありわかりやすいです。  

すべてのデータ・セットを一度にオンメモリに展開して最適化するというものではないので、 
1000万を超えるコーパスでもうまくすれば分類することができます。  

ScikitLearnには線形モデル各種をSGDで最適化できる関数が用意されていて、SVM, Logistic Regressonなどなどが損失関数の設定で行えるようになっています。  
またペナルティも、L1, L2のほかelasticが最新のScikitLearnでは用意されていて便利です（2019年5月現在のAnacondaのデフォルトのScikitLearnは実装されていないようですが...）  

### 実際にやった分類
ScikitLearnのSGDClassifierを利用して、ペナルティをelasticとしました。  

kfoldしながら、optunaでAUCの最大となる点を探索しながら各種ハイパラを探索させている。  

[コード](https://github.com/GINK03/ameblo-analytics/blob/master/F001_train.py)

## 代表的な角度でのクラシフィケーション（分類）とその重要度

### 埼玉県民とそれ以外の違い
埼玉県民とそれ以外を分類を行おうとすると、 `AUC 0.503` で実際はほとんど分類できない。  
分類性能は悪いが、その判断基準となった特徴量がユニークで面白い。  

埼玉県民のコーパスの特徴として「池袋」が入っているとそれらしいという結果になっており、実質的に池袋は埼玉県民の土地であるということがわかる。  

<div align="center">
  <div> 表1. 埼玉県民とその他 </div>
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/57965999-3350f400-7987-11e9-8d47-aa0d8b543420.png">
</div>

### 男女の分類
男女の分類で見ると、 `AUC 0.741` になり、そこそこの性能で分類できる。  

男性言葉、女性言葉が分類用の特徴量として目立っており、どんな言葉を使えば男性らしく、女性らしく統計的になるのかった  

<div align="center">
  <div> 表２. 男女の分類 </div>
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/57966001-35b34e00-7987-11e9-8d7d-7b6922fb0153.png">
</div>

### 1988年生以前生まれと以後生まれ
勝手に若いというを1988以前, 1988以降の生まれの人の記事の分類をすると、 `AUC 0.681` で分類できる

おそらく携帯電話の頭である090が最もわかりやすい特徴量になっていることや、息子、娘がいること、文章中の `〜` も年寄りくさいな、、、と思っていたのですがそういう結果になった  

Twitterは若者のSNSツール、そうだね。  

<div align="center">
  <div> 表3. 年代別 </div>
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/57966002-377d1180-7987-11e9-8a44-9165074f193b.png">
</div>

## サービスのユーザの人口の高齢化
[ニコニコ動画も高齢化しているというデータがある](https://togetter.com/li/974789)ように、実はアメブロでも同様の老化が起きていることがわかっている。  
ユーザプロフィールと登録している生年月日を突合すると、ブログを書いたときの平均年齢が逆算できる。  
その時の平均の年齢を `age` とすると、このようなグラフになる  
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970599-24d1ff00-79be-11e9-8b1e-8a645e6a8b67.png">
 <div> 図1. 年齢の経年変化 </div>
</div>
ほぼサービス人口の年齢が新陳代謝してない 

## 結局流行語（大賞）は長生きするのか

見ていきましょう  

アメブロはサービスとしても現在進行系で記事数が増加しておりそのバイアスを排除するため、その集計粒度の月の総数で割ることで一定の正規化をしている  

### 壁ドン（2014年）

<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969312-bc305580-79b0-11e9-90dc-f46bfc166300.png">
 <div> 図2. 壁ドン </div>
</div>


### 妖怪ウォッチ(2014年)
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969328-eda92100-79b0-11e9-9e8b-c4051998567d.png">
 <div> 図3. 妖怪ウォッチ </div>
</div>

### 爆買い(2015年)
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970404-e89d9f00-79bb-11e9-8010-03460ae08c0a.png">
 <div> 図4. 爆買い </div>
</div>

### PPAP(2016年)
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970248-00742380-79ba-11e9-98b2-4e118b6ae439.png">
 <div> 図5. PPAP </div>
</div>

## ライフステージなどに応じたキーワード  

### ガン
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57978523-63ad9680-7a4a-11e9-8713-edf79901f231.png">
 <div> 図6. ガン </div>
</div>

### 出産
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57978534-a4a5ab00-7a4a-11e9-800a-9798d7707a0a.png">
 <div> 図7. 出産 </div>
</div>

### 結婚
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57978547-ddde1b00-7a4a-11e9-92c4-d706573fdcfc.png">
 <div> 図8. 結婚 </div>
</div>

## 周期性のあるキーワード
### 花粉症 
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970699-775feb00-79bf-11e9-9bb2-cd769531fe16.png">
 <div> 図９. 花粉症 </div>
</div>

### PM2.5 
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970716-aaa27a00-79bf-11e9-9cbf-901bd72a4284.png">
 <div> 図10. PM2.5 </div>
</div>

### 暑い
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970789-9743de80-79c0-11e9-959a-f5de21d547f3.png">
 <div> 図11. 暑い </div>
</div>
２０１８年が過去ないほどの比率で”暑い”と言われており、実際に人々がそう感じていたということが定量的にわかります



## TV,新聞に対して、SNS各種は継続して人気が上がり続ける
ブロードキャスト型のコンテンツのテレビに対して、twitter, facebook, line, youtube, instagramなどは人気が上がり続けている  

### Twitter
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969694-96a54b00-79b4-11e9-8bcc-dc500fe5602d.png">
 <div> 図12. Twitter </div>
</div>

### Facebook
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969696-a15fe000-79b4-11e9-8190-d1605e8b7b79.png">
 <div> 図13. Facebook</div>
</div>

### line
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969701-ae7ccf00-79b4-11e9-9656-3137090c1291.png">
 <div> 図14. line</div>
</div>

### インスタグラム
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969705-bc325480-79b4-11e9-86c8-fdf0c2d13798.png">
 <div> 図15. インスタグラム</div>
</div>

### YouTube
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970318-c35c6100-79ba-11e9-9fb8-e60634415032.png">
 <div> 図16. YouTube</div>
</div>

### テレビ
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57969958-17b11200-79b6-11e9-9c2a-5c1cd5d15ca8.png">
 <div> 図17. テレビ </div>
</div>

### 新聞
<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/4949982/57970292-82fce300-79ba-11e9-9bc7-2aef8a78124f.png">
 <div> 図18. 新聞 </div>
</div>

## まとめ
何らかの判別のモデルを作成して、その特徴量を見ると何で分離されているのかわかりやすですが、判別性能が十分に出ないのであれば、強く一般化できない特徴量だと思われます。 

アメブロという媒体の特性か、Twitterで流行りの激おこぷんぷん丸などのバズワードや言い回しは殆ど使われていないようでした。  

サービス自体が若い世代の参入が少ないという状態にあるので、ガンの頻出や結婚出産も比例して上がっていることがわかりました。  

高齢化の影響を受けつつもテレビと新聞は人気が現状維持か少し落ち気味です。年齢的なバイアスを外せばSNSに順調にシェアを奪われているように見えます。  
