# Coin Parking Webシステム

## 1. ビジネス背景・目的説明書

### 背景

当社が保有する月極駐車場には、長期的に契約のない空きスペースが一定数存在し、収益化されていない状態が続いています。一方で、地域には時間貸し駐車場のニーズが高まっており、特にスマートフォンからの即時予約・決済が可能な「キャッシュレス型コインパーキング」への期待が高まっています。

### 目的

未契約の空きスペースを活用し、Web上で閲覧・予約・決済が完結するコインパーキングシステムを構築。新たな収益モデルを確立し、将来的には多拠点展開およびB2BパートナーへのOEM提供も視野に入れたサービス基盤を構築することを目的とします。

## 2. 要求仕様書

### 機能要件
- 駐車場検索（地図／住所）＋空き状況表示
- 駐車場詳細表示（画像・料金・場所）
- 予約機能（日付・時間指定）
- Stripe連携によるオンライン決済（クレジットカード）
- マイページ機能（履歴・キャンセル）
- 管理画面機能（予約一覧、売上レポート、CSV出力、PDF出力、検索機能）

### 非機能要件
- モバイルファースト設計
- Dockerコンテナ対応
- 管理者ログイン認証（簡易）
- セキュアな決済・認証連携

## 3. UI ワイヤーフレーム（テキスト）
- **トップページ**: 検索バー、地図エリア（Google Map）、駐車場リスト（カード）
- **詳細ページ**: 駐車場画像、住所、料金、予約ボタン
- **予約ページ**: カレンダー、時間入力、カード情報
- **マイページ**: 予約履歴 / キャンセルボタン
- **管理画面**: タブ（予約検索 / 売上分析）、ボタン（CSV出力 / PDF出力）

## 4. データ設計（ER概要）
```
ParkingSpot
- id (PK)
- name
- address
- latitude / longitude
- hourly_rate / daily_rate

Reservation
- id (PK)
- parking_spot_id (FK)
- user_email
- start_time / end_time
- total_price
- is_paid
```

## 5. API仕様書
```
POST /api/create-payment-intent/
Request: { "amount": 1500 }
Response: { "clientSecret": "..." }

GET /admin/search/
Params: email, start, end
Response: JSONリスト

GET /admin/sales/export/
Params: start, end
Response: CSVファイル

GET /admin/search/pdf/
Params: email
Response: PDFファイル（帳票）
```

## 6. インフラ・運用設計
- Docker + docker-compose
- PostgreSQL
- Django + React
- 静的ファイル: Cloudflare Pages もしくは S3互換
- Stripe（決済）
- SendGrid（通知メール）

### 運用
- 定期バックアップ（DB）
- エラーログ・売上ログ保存
- PDF/CSV出力ファイル一時保存

## 7. 受入基準 & テスト計画
- 予約・支払い・キャンセルが正常に動作
- 売上グラフが日付範囲で変化
- PDF・CSVがダウンロード可能
- 管理者ログインが機能し、検索・出力ができる

### テスト方針
- 単体テスト（モデル・API）
- E2Eテスト（予約→支払い→マイページ）
- UIテスト（主要画面クリック動作）
- PDF出力の内容一致確認
