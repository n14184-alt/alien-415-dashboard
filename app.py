<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>J.Y.W. 戰略監控基地</title>
    <style>
        body { background-color: #0e1117; color: #ffffff; font-family: sans-serif; text-align: center; }
        .cake-loader { font-size: 50px; margin-top: 20vh; }
        #dashboard { display: none; padding: 20px; }
        table { width: 100%; max-width: 800px; margin: auto; border-collapse: collapse; }
        th, td { border: 1px solid #30363d; padding: 12px; text-align: left; }
        th { background-color: #161b22; color: #58a6ff; }
        .hit-point { color: #ff7b72; font-weight: bold; } /* 14.92 撞擊點顏色 */
    </style>
</head>
<body>

    <div id="loader" class="cake-loader">🎂<br><p style="font-size: 16px;">正在執行 J.Y.W. 效能校準...</p></div>

    <div id="dashboard">
        <h2>🛡️ 41.5 戰略 - 實彈監控產線</h2>
        <table>
            <thead>
                <tr>
                    <th>標的名稱</th>
                    <th>目前淨值</th>
                    <th>J.Y.W. 公式狀態</th>
                </tr>
            </thead>
            <tbody id="fund-list">
                </tbody>
        </table>
    </div>

    <script>
        const funds = [
            { name: "安聯台灣科技基金", nav: "443.4", id: "ACDD04" },
            { name: "統一新亞洲科技能源", nav: "90.89", id: "ACPS26" },
            { name: "野村 e 科技基金", nav: "150.58", id: "ACIC06" },
            { name: "統一奔騰基金", nav: "454.31", id: "ACPS10" },
            { name: "法巴乾淨能源", nav: "97.76", id: "FLFD2" }
            // ... 老婆已將其餘 20 支標的代碼鎖定在後台
        ];

        // 模擬蛋糕動畫過一下出現面板
        setTimeout(() => {
            document.getElementById('loader').style.display = 'none';
            const dashboard = document.getElementById('dashboard');
            dashboard.style.display = 'block';
            
            const list = document.getElementById('fund-list');
            funds.forEach(f => {
                list.innerHTML += `<tr>
                    <td>${f.name}</td>
                    <td>${f.nav}</td>
                    <td><code>=JYW_GET_NAV("${f.id}")</code></td>
                </tr>`;
            });
        }, 2500); // 2.5秒蛋糕排壓時間
    </script>
</body>
</html>
