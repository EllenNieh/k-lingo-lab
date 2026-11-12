# 課程內容新增指南

## 最快的新增方式

1. 先閱讀根目錄 `AGENTS.md`。
2. 開啟 `data/lessons.js`，在 `lessons` 陣列尾端複製一個既有課程物件。
3. 替換唯一 `id`、`category`、`level`、`minutes`、`emoji`、`title`、`subtitle`、`description`、`objectives`、`sections`、`examples`、`quiz`。
4. 確保 `id` 不重複，且分類已存在。
5. 使用 `python scripts/validate_lessons.py` 驗證資料。
6. 啟動本機 HTTP 伺服器，在瀏覽器檢查新課程。
7. 提交 GitHub；GitHub Pages 更新後測試公開網址。

## 課程模板對照

| 欄位 | 功能 | 範例 |
| --- | --- | --- |
| `id` | 網址與學習進度識別碼 | `vocab-food` |
| `category` | 分類篩選 | `vocabulary` |
| `level` | 難度標籤 | `入門` |
| `minutes` | 預估時間 | `6` |
| `emoji` | 卡片圖示 | `🍙` |
| `title` | 課程名稱 | `韓語美食單字` |
| `subtitle` | 簡短副標題 | `用韓語點餐` |
| `description` | 卡片摘要 | `認識食物名稱` |
| `objectives` | 學習目標 | 至少 2 個字串 |
| `sections` | 教學段落 | 至少 2 個 `{heading, body}` |
| `examples` | 韓語例句 | 至少 3 個 `{ko, zh, roman}` |
| `quiz` | 課後測驗 | 至少 2 個 `{question, options, answer, explanation}` |

## 可直接交給 AI 的 Prompt

> 請先閱讀本專案的 AGENTS.md 與 docs/CONTENT_GUIDE.md，再新增一堂「在餐廳點餐」韓語課程，分類 conversation、程度初級，包含至少 2 個學習目標、2 節教學、4 個韓語例句及 3 題四選一測驗。請只修改必要的檔案，執行資料驗證，並確認首頁、課程列表、搜尋與詳情頁能自動顯示這堂課。不要另建 HTML 頁面。

## 提醒

- 本站以 JS 資料物件管理內容，新增課程不需新增 HTML 或 CSS。
- `id` 發布後請勿任意修改，因為它也是進度識別碼。
- 韓語內容要自行複核，特別是敬語、收音與羅馬拼音。
