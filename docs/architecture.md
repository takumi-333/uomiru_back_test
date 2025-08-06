# システム構成図

```mermaid
graph LR
  subgraph FE[Frontend]
    A[ユーザブラウザ\n(Next.js ウオミルWebアプリ)]
  end

  subgraph BE[Backend]
    B[Flask APIサーバ]
    C[(MySQL データベース)]
  end

  subgraph AI[AI Service]
    D[画像生成API\n(魚の生成・進化)]
  end

  subgraph ST[Storage]
    E[(AWS S3\n魚画像ストレージ)]
  end

  %% 接続
  A -->|HTTPS/REST| B
  B -->|SQL| C
  B -->|API呼び出し| D
  B -->|S3 API| E
```