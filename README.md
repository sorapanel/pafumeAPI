# 香水API - Perfume API

## 概要

このAPIは、様々な香水に関する詳細な情報をJSON形式で提供します。商品のタイトル、ブランド名、カテゴリ、概要など、香水に関する豊富なデータを取得できます。香水関連のアプリケーション開発やデータ分析にご活用ください。

## エンドポイント

### 香水情報一覧の取得

*   **パス:** `/perfume_api/perfume_info/`
*   **メソッド:** `GET`
*   **概要:** 香水の情報リストをJSON形式で返します。

### レスポンス例 (HTTP 200 OK)

```json
{
    "count": 123,
    "next": "http://127.0.0.1:8000/perfume_api/perfume_info/?page=2&page_size=50",
    "previous": null,
    "results": [
        {
            "id": 1,
            "categories": [
                {
                    "id": 1,
                    "category": "シトラス系"
                },
                {
                    "id": 2,
                    "category": "ウッディ系"
                }
            ],
            "title": "ネバーエンディング サマー",
            "brand": "Maison Margiela",
            "brandJp": "メゾン マルジェラ",
            "description": "イタリアのアマルフィ海岸での終わらない夏をテーマにした、爽やかさと深みを兼ね備えたシトラスウッディの香り。ビターオレンジ、アールグレイ、ベチバーなどが織りなす。"
        },
        {
            "id": 2,
            "categories": [
                {
                    "id": 3,
                    "category": "フローラル系"
                }
            ],
            "title": "ローズ ド マントン",
            "brand": "CHANEL",
            "brandJp": "シャネル",
            "description": "南仏マントンのバラ園をイメージした、優雅で洗練されたフローラルブーケの香り。ローズ、ジャスミン、サンダルウッドが調和。"
        }
        // ... (続く)
    ]
}
```
### レスポンスヘッダー
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
### レスポンスフィールド
| フィールド名    | 型       | 説明                                                 |
| :-------------- | :------- | :--------------------------------------------------- |
| `id`            | `integer` | 香水の一意な識別子                                   |
| `categories`    | `array`  | 香水が属するカテゴリのリスト。各要素は以下の構造を持つ: |
| &nbsp;&nbsp;`id` | `integer` | カテゴリの一意な識別子                               |
| &nbsp;&nbsp;`category` | `string` | カテゴリ名 (例: "シトラス系", "フローラル系")       |
| `title`         | `string` | 香水の商品名                                         |
| `brand`         | `string` | ブランド名 (英語表記)                                |
| `brandJp`       | `string` | ブランド名 (日本語表記)                              |
| `description`   | `string` | 香水の商品概要・説明                                 |
| `count`         | `integer` | 全体の香水情報の総数                                 |
| `next`          | `string` | 次のページを取得するためのURL。最終ページの場合は `null` |
| `previous`      | `string` | 前のページを取得するためのURL。最初のページの場合は `null` |
### クエリパラメータ
| フィールド名    | 型       | 説明                                                 |
| :-------------- | :------- | :--------------------------------------------------- |
| `category`    | `string`  | 香水が属するカテゴリ|
| `title`         | `string` | 香水の商品名                                         |
| `brand`         | `string` | ブランド名 (英語表記)                                |
| `brandJp`       | `string` | ブランド名 (日本語表記)                              |
| `page_size`      | `integer` | レスポンスのレコード数指定（デフォルト50, 最大200） |
| `page`      | `integer` | ページ数の指定                                     |
## Skill
Django REST Framework
