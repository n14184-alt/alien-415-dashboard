/**
 * PROJECT W - 丫環 試算表 數據 擊穿 模組
 * 物理 性 鎖定 ID： 136KQ4C1o9XwxOTzN1D7Zdvrls4tIW0Fi6Eq8JuiQMlk
 */
function doGet(e) {
  const fundCode = e.parameter.code; // 接收來自 APP.PY 的 ACDD01
  const ss = SpreadsheetApp.openById("136KQ4C1o9XwxOTzN1D7Zdvrls4tIW0Fi6Eq8JuiQMlk");
  const sheet = ss.getSheetByName("工作表1"); // 請 物理 性 核對 您的 分頁 名稱
  const data = sheet.getDataRange().getValues();
  
  let result = { status: "沒 水 ( 找不到 )", price: 0 };

  // 物理 性 掃描 A 欄 ( 基金 代碼 )
  for (let i = 0; i < data.length; i++) {
    if (data[i][0] == fundCode) { // 如果 找到 ACDD01
      result.status = "有 水 ( 命中 )";
      result.price = data[i][2]; // 物理 性 抓取 C 欄 ( 淨值 )
      break;
    }
  }
  
  // 執行 物理 性 噴發
  return ContentService.createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}
