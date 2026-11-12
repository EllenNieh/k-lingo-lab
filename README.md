# 💗 K-Lingo Lab｜韓語互動學習手冊

以活潑互動的方式，幫助韓語零基礎學習者從字母、單字、情境對話到基本文法逐步學習。此專案的重點是透過 **AGENTS.md** 定義可重複使用的開發規則，讓 AI 未來能依同一套資料格式快速新增課程，而不需要重做網站。

## 功能

- 首頁：課程分類、推薦課程、學習進度
- 課程庫：分類篩選與關鍵字搜尋
- 課程詳情：教學段落、韓語例句、語音播放、四選一測驗
- 學習進度：使用瀏覽器 localStorage 保存已完成課程
- 響應式設計：支援手機、平板與桌面
- 結構化教材：目前提供 6 堂示範課程，未來可持續擴充

## 本機執行

需要使用 HTTP 伺服器（因為網站使用 JavaScript ES Modules），**不要直接雙擊 index.html 用 file:// 開啟**。

```bash
cd k-lingo-lab
python -m http.server 8000
```

瀏覽器開啟 `http://localhost:8000`。

## 部署 GitHub Pages

1. 在 GitHub 建立公開儲存庫，例如 `k-lingo-lab`。
2. 上傳本專案的**全部檔案與資料夾**，確保 `index.html` 位於儲存庫根目錄。
3. 進入 **Settings → Pages**。
4. 在 **Build and deployment** 選擇 **Deploy from a branch**。
5. 選擇 `main` 分支與 `/(root)`，點擊 **Save**。
6. 等待 GitHub 完成部署後，開啟 `https://<你的帳號>.github.io/k-lingo-lab/`。
7. 實際測試課程列表、課程詳細頁、搜尋、測驗與完成進度。

如果儲存庫名稱不同，公開網址也要相應調整。GitHub Pages 發布可能需要幾分鐘。

## 如何新增一堂課？

1. 閱讀 [AGENTS.md](./AGENTS.md) 與 [新增指南](./docs/CONTENT_GUIDE.md)。
2. 在 [`data/lessons.js`](./data/lessons.js) 的 `lessons` 陣列新增符合規範的物件。
3. 依照 `AGENTS.md` 的欄位與測驗規則完成資料。
4. 執行 `python scripts/validate_lessons.py`。
5. 預覽網站並檢查課程列表、搜尋、發音、測驗與進度。

**無需新增獨立 HTML 頁面。** 網站會根據資料自動產生課程卡片與詳細內容。

## 注意事項

- 韓語發音採用 Web Speech API，實際音色及支援程度取決於瀏覽器與裝置是否有韓語語音。
- 學習進度只保存在目前瀏覽器，不會跨裝置同步。
- 這是學習展示專案，韓語內容仍應在正式教學使用前由具備語言能力的人員複核。
- Google Fonts 若無法連線，會自動改用系統備援字型。

## 作業說明

本專案示範了「規則優先的 AI 開發」：`AGENTS.md` 定義目的、目錄、資料格式、設計規範、AI 修改流程與驗收標準。之後只要請 AI 依規則新增課程，便能延續既有網站的結構與互動功能，達成可重複使用與長期擴充。
