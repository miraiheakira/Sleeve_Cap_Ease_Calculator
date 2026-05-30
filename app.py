import webview

# ========= 把你的完整 HTML 代码粘贴到下面三个引号之间 =========
html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>袖山吃势分配计算器</title>
    <style>
        * {
            box-sizing: border-box;
            font-family: system-ui, 'Segoe UI', 'Roboto', 'Noto Sans', sans-serif;
        }
        body {
            background: #f0f2f5;
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem 1rem;
        }
        .card {
            max-width: 1000px;  /* 整体页面宽度的修改 */
            width: 100%;
            background: white;
            border-radius: 28px;
            box-shadow: 0 20px 35px -12px rgba(0,0,0,0.15);
            padding: 1.8rem 2rem 2.2rem 2rem;
            transition: all 0.2s;
        }
        h1 {
            font-size: 1.8rem;
            font-weight: 600;
            margin: 0 0 0.25rem 0;
            color: #1e2a3e;
            letter-spacing: -0.2px;
            padding-left:0;
        }
        .sub {
            color: #4a627a;
            margin-bottom: 2rem;
            font-size: 0.9rem;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 0.6rem;
        }
        /* 第一排：输入区域 */
        .input-bar {
            display: flex;
            flex-wrap: wrap;
            align-items: flex-end;
            gap: 1.2rem;
            margin-bottom: 2rem;
            background: #f8fafc;
            padding: 1.2rem 1.5rem;
            border-radius: 24px;
            border: 1px solid #e2edf2;
        }
        .input-group {
            flex: 1;
            min-width: 130px;
        }
        .input-group label {
            display: block;
            font-weight: 600;
            font-size: 0.85rem;
            color: #1e3a5f;
            margin-bottom: 0.4rem;
            letter-spacing: 0.3px;
        }
        .input-group input {
            width: 100%;
            padding: 10px 12px;
            font-size: 1rem;
            border: 1.5px solid #cbd5e1;
            border-radius: 16px;
            background: white;
            transition: 0.2s;
            font-weight: 500;
            color: #0f172a;
        }
        .input-group input:focus {
            outline: none;
            border-color: #b87333;
            box-shadow: 0 0 0 3px rgba(184,115,51,0.2);
        }
        .btn-reset {
            background: #eef2ff;
            border: 1px solid #cbd5e1;
            padding: 0 1.5rem;
            border-radius: 40px;
            font-weight: 600;
            font-size: 0.9rem;
            color: #1e293b;
            cursor: pointer;
            height: 44px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
            margin-bottom: 0;
            background: #ffffff;
            box-shadow: 0 1px 2px rgba(0,0,0,0.03);
        }
        .btn-reset:hover {
            background: #f1f5f9;
            border-color: #b87333;
            color: #b45a2b;
            transform: scale(0.97);
        }
        /* 第二排：总吃势量 */
        .total-block {
            background: #fef7e8;
            padding: 0.9rem 1.8rem;
            border-radius: 60px;
            display: inline-flex;
            align-items: baseline;
            gap: 0.8rem;
            margin-bottom: 2rem;
            border: 1px solid #ffe2bf;
            flex-wrap: wrap;
        }
        .total-label {
            font-weight: 700;
            font-size: 1.2rem;
            color: #a6521d;
        }
        .total-value {
            font-size: 1.6rem;
            font-weight: 800;
            font-family: 'JetBrains Mono', monospace;
            background: white;
            padding: 0.1rem 1rem;
            border-radius: 40px;
            color: #b45a2b;
            letter-spacing: 1px;
            min-width: 120px;
            display: inline-block;
            text-align: center;
            border: 1px solid #ffd9a5;
        }
        /* 表格区域 */
        .table-wrapper {
            overflow-x: auto;
            border-radius: 20px;
            border: 1px solid #e9edf2;
            background: white;
            margin-top: 0.5rem;
        }
        .data-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 1.2rem;
            min-width: 780px;
        }
        .data-table th, .data-table td {
            border: 1px solid #e2e8f0;
            padding: 12px 8px;
            text-align: center;
            vertical-align: middle;
        }
        .data-table th {
            background-color: #f1f5f9;
            font-weight: 700;
            color: #1e3a5f;
            font-size: 1rem;
            letter-spacing: 0.5px;
        }
        .row-label {
            background-color: #fef9f0;
            font-weight: 700;
            color: #b45a2b;
            width: 70px;
            font-size: 1rem;
        }
        .data-table td {
            font-family: 'Courier New', 'SF Mono', monospace;
            font-weight: 500;
            background-color: #ffffff;
            color: #0c4a6e;
        }
        /* 辅助样式 */
        .note {
            font-size: 0.7rem;
            color: #5b6e8c;
            text-align: right;
            margin-top: 1rem;
            border-top: 1px dashed #dce5ec;
            padding-top: 0.8rem;
        }
        @media (max-width: 760px) {
            .card { padding: 1.2rem; }
            .input-bar { flex-direction: column; align-items: stretch; }
            .btn-reset { align-self: flex-start; margin-top: 0.2rem; }
        }
    </style>
</head>
<body>
<div class="card">
    <h1>🧥袖山吃势分配</h1>
    <div class="sub">袖山弧线 · 后AH · 前AH 吃势计算</div>

    <!-- 第一排：三个输入框 + 重置按钮 (对齐) -->
    <div class="input-bar">
        <div class="input-group">
            <label>📐 袖山弧线</label>
            <input type="number" id="sleeveCrown" placeholder="0.00" step="any" value="">
        </div>
        <div class="input-group">
            <label>🔸 后AH</label>
            <input type="number" id="backAh" placeholder="0.00" step="any" value="">
        </div>
        <div class="input-group">
            <label>🔹 前AH</label>
            <input type="number" id="frontAh" placeholder="0.00" step="any" value="">
        </div>
        <button class="btn-reset" id="resetBtn">⟳ 重置</button>
    </div>

    <!-- 第二排：总吃势量展示 -->
    <div class="total-block">
        <span class="total-label">🧵总吃势量</span>
        <span class="total-value" id="totalEaseDisplay">—</span>
        <span style="font-size:0.8rem; color:#95653b;">(袖山弧线 − 后AH − 前AH)</span>
    </div>

    <!-- 第三、四、五排：表格形式展示 8个值 -->
    <div class="table-wrapper">
        <table class="data-table" id="resultTable">
            <thead>
                <tr>
                    <th>分配量</th>
                    <th>后AH</th><th>后吃势</th><th>弧线长</th><th>后总长</th>
                    <th>前AH</th><th>前吃势</th><th>弧线长</th><th>前总长</th>
                </tr>
                </thead>
                <tbody>
                    <!-- 第三排 (索引0) -->
                    <tr>
                        <td class="row-label">✏️上</td>
                        <td id="r3c1">—</td><td id="r3c2">—</td><td id="r3c3">—</td><td id="r3c4">—</td>
                        <td id="r3c5">—</td><td id="r3c6">—</td><td id="r3c7">—</td><td id="r3c8">—</td>
                    </tr>
                    <!-- 第四排 -->
                    <tr>
                        <td class="row-label">✂️中</td>
                        <td id="r4c1">—</td><td id="r4c2">—</td><td id="r4c3">—</td><td id="r4c4">—</td>
                        <td id="r4c5">—</td><td id="r4c6">—</td><td id="r4c7">—</td><td id="r4c8">—</td>
                    </tr>
                    <!-- 第五排 -->
                    <tr>
                        <td class="row-label">📏下</td>
                        <td id="r5c1">—</td><td id="r5c2">—</td><td id="r5c3">—</td><td id="r5c4">—</td>
                        <td id="r5c5">—</td><td id="r5c6">—</td><td id="r5c7">—</td><td id="r5c8">—</td>
                    </tr>
                </tbody>
        </table>
    </div>
    <div class="note">
        ※ 吃势分配基于「总吃势量」自动计算，所有数值保留两位小数。输入数值为空或无效时显示「—」。
    </div>
</div>

<script>
    (function() {
        // DOM 元素绑定
        const sleeveInput = document.getElementById('sleeveCrown');
        const backInput = document.getElementById('backAh');
        const frontInput = document.getElementById('frontAh');
        const totalSpan = document.getElementById('totalEaseDisplay');
        const resetBtn = document.getElementById('resetBtn');

        // 定义第三排、第四排、第五排所有单元格ID (共24个)
        // 第三排
        const row3Cells = [
            document.getElementById('r3c1'), document.getElementById('r3c2'), document.getElementById('r3c3'),
            document.getElementById('r3c4'), document.getElementById('r3c5'), document.getElementById('r3c6'),
            document.getElementById('r3c7'), document.getElementById('r3c8')
        ];
        // 第四排
        const row4Cells = [
            document.getElementById('r4c1'), document.getElementById('r4c2'), document.getElementById('r4c3'),
            document.getElementById('r4c4'), document.getElementById('r4c5'), document.getElementById('r4c6'),
            document.getElementById('r4c7'), document.getElementById('r4c8')
        ];
        // 第五排
        const row5Cells = [
            document.getElementById('r5c1'), document.getElementById('r5c2'), document.getElementById('r5c3'),
            document.getElementById('r5c4'), document.getElementById('r5c5'), document.getElementById('r5c6'),
            document.getElementById('r5c7'), document.getElementById('r5c8')
        ];

        // 辅助函数：格式化数字，保留两位小数，若为NaN或无穷则返回null
        function formatTwoDigits(value) {
            if (value === null || typeof value !== 'number' || isNaN(value) || !isFinite(value)) {
                return null;
            }
            // 保留两位小数，避免 -0.00 问题
            let rounded = Math.round(value * 100) / 100;
            if (rounded === -0) rounded = 0;
            return rounded.toFixed(2);
        }

        // 核心计算与更新界面
        function updateAllCalculations() {
            // 1. 获取三个输入框的数值 (空字符串或非数字转为 NaN)
            let sleeveVal = parseFloat(sleeveInput.value);
            let backVal = parseFloat(backInput.value);
            let frontVal = parseFloat(frontInput.value);

            // 检查是否任何一个输入无效 (NaN 或 空值视为无效)
            const isSleeveValid = sleeveInput.value !== '' && !isNaN(sleeveVal);
            const isBackValid = backInput.value !== '' && !isNaN(backVal);
            const isFrontValid = frontInput.value !== '' && !isNaN(frontVal);
            
            // 三个必须全部有效才能进行计算，否则全部显示占位符 "—"
            if (!isSleeveValid || !isBackValid || !isFrontValid) {
                // 总吃势量显示 —
                totalSpan.innerText = '—';
                // 清空所有表格单元格为 —
                const allCells = [...row3Cells, ...row4Cells, ...row5Cells];
                allCells.forEach(cell => { if (cell) cell.innerText = '—'; });
                return;
            }

            // 有效数值前提下计算总吃势量 = 袖山弧线 - 后AH - 前AH
            let totalEase = sleeveVal - backVal - frontVal;
            // 总吃势量显示保留两位小数
            let totalFormatted = formatTwoDigits(totalEase);
            if (totalFormatted === null) {
                totalSpan.innerText = '—';
                const allCells = [...row3Cells, ...row4Cells, ...row5Cells];
                allCells.forEach(cell => { if (cell) cell.innerText = '—'; });
                return;
            }
            totalSpan.innerText = totalFormatted;

            // 由于后续公式频繁使用后AH、前AH、总吃势量，直接使用数值 (已确保是有效数字)
            const back = backVal;
            const front = frontVal;
            const ease = totalEase;   // 可为负数，按公式依然有效

            // ---------- 第三排 8个公式 (基于描述) ----------
            // 公式顺序:
            // 1: 后AH/3
            // 2: 0.25 * 总吃势量
            // 3: 后AH/3 + 0.25*总吃势量
            // 4: 后AH + 0.6*总吃势量
            // 5: 后AH/3
            // 6: 0.25*总吃势量
            // 7: 后AH/3 + 0.25*总吃势量
            // 8: 前AH + 0.4*总吃势量
            const backDiv3 = back / 3;
            const q25Ease = 0.25 * ease;
            const q6Ease = 0.6 * ease;
            const q4Ease = 0.4 * ease;
            
            const row3Values = [
                backDiv3,
                q25Ease,
                backDiv3 + q25Ease,
                back + q6Ease,
                backDiv3,
                q25Ease,
                backDiv3 + q25Ease,
                front + q4Ease
            ];

            // ---------- 第四排 8个公式 ----------
            // 1: 后AH/3
            // 2: 0.25*总吃势量
            // 3: 后AH/3 + 0.25*总吃势量
            // 4: 后AH/3*2 + 0.35*总吃势量   -> (后AH/3)*2 + 0.35*ease
            // 5: 后AH/3
            // 6: 0.15*总吃势量
            // 7: 后AH/3 + 0.15*总吃势量
            // 8: 前AH - 后AH/3 + 0.15*总吃势量
            const q35Ease = 0.35 * ease;
            const q15Ease = 0.15 * ease;
            const backDiv3Times2 = (back / 3) * 2;   // 后AH/3*2
            const row4Values = [
                backDiv3,
                0.25 * ease,
                backDiv3 + 0.25 * ease,
                backDiv3Times2 + q35Ease,
                backDiv3,
                q15Ease,
                backDiv3 + q15Ease,
                front - backDiv3 + q15Ease
            ];

            // ---------- 第五排 8个公式 (严格遵循描述) ----------
            // 1: 后AH/3
            // 2: 0.1*总吃势量
            // 3: 后AH/3 + 0.1*总吃势量
            // 4: 后AH/3 + 0.1*总吃势量   (与第三个相同)
            // 5: 前AH - 后AH/3*2           (注意: 后AH/3*2 即 (后AH/3)*2)
            // 6: 0
            // 7: 前AH - 后AH/3*2
            // 8: 前AH - 后AH/3*2
            const q1Ease = 0.1 * ease;
            const backDiv3Mul2 = (back / 3) * 2;   // 后AH/3*2
            const frontMinusBackDiv3Mul2 = front - backDiv3Mul2;
            const row5Values = [
                backDiv3,
                q1Ease,
                backDiv3 + q1Ease,
                backDiv3 + q1Ease,
                frontMinusBackDiv3Mul2,
                0,
                frontMinusBackDiv3Mul2,
                frontMinusBackDiv3Mul2
            ];

            // 辅助函数: 更新一行单元格，处理格式化
            function setRowCells(cellsArray, valuesArray) {
                for (let i = 0; i < cellsArray.length; i++) {
                    if (cellsArray[i]) {
                        const numericVal = valuesArray[i];
                        const formatted = formatTwoDigits(numericVal);
                        cellsArray[i].innerText = (formatted !== null) ? formatted : '—';
                    }
                }
            }

            // 更新三行
            setRowCells(row3Cells, row3Values);
            setRowCells(row4Cells, row4Values);
            setRowCells(row5Cells, row5Values);
        }

        // 重置所有输入框为空值，并清空所有结果显示 "—"
        function resetAllFields() {
            sleeveInput.value = '';
            backInput.value = '';
            frontInput.value = '';
            // 强制重新计算(此时三个输入为空，updateAllCalculations 会显示占位符)
            updateAllCalculations();
            // 额外确保总吃势量显示为 — (update里已做)
            // 让输入框失去焦点，视觉舒适
            sleeveInput.blur();
            backInput.blur();
            frontInput.blur();
        }

        // 绑定输入事件 (实时联动)
        sleeveInput.addEventListener('input', updateAllCalculations);
        backInput.addEventListener('input', updateAllCalculations);
        frontInput.addEventListener('input', updateAllCalculations);
        
        // 重置按钮事件
        resetBtn.addEventListener('click', resetAllFields);

        // 页面初始化调用一次，显示占位符 (所有框默认空)
        updateAllCalculations();

        // 可选: 为增强用户体验, 添加小数步进控制, 但已经使用number支持任意小数, 无需额外处理。
        // 另外针对部分浏览器number空值解析NaN正常。
    })();
</script>
</body>
</html>
"""
# ===========================================================

webview.create_window(
    title="袖山吃势计算器",
    html=html_content,      # 注意是 html= ，不是 url=
    width=1150,      # 窗口宽度（像素）
    height=750,      # 窗口高度（像素）
    resizable=True      # 是否允许用户调整窗口大小（True/False）
)
webview.start()
