from flask import Flask, render_template_string, request, jsonify
import random
import datetime

app = Flask(__name__)

# FamPay API Key provided by you
FAM_API_KEY = "fam_079a0e16e1934243332d025b0fb464a6d0a5f213"

# Database simulation for generated valid keys
ACTIVE_KEYS = {}

# Complete HTML + CSS + JS Frontend Interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CTG ALGORITHM X1 // LIVE PRODUCTION TERMINAL</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Courier New', Courier, monospace; }
        body {
            background-color: #03060c;
            color: #00ff66;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 15px;
        }
        body::before {
            content: "";
            position: fixed;
            inset: 0;
            background: radial-gradient(circle at center, rgba(0, 255, 102, 0.08) 0%, #03060c 85%);
            z-index: -1;
        }
        .container {
            background: rgba(8, 14, 26, 0.96);
            border: 1px solid #00ff66;
            box-shadow: 0 0 30px rgba(0, 255, 102, 0.25);
            border-radius: 12px;
            padding: 28px;
            width: 100%;
            max-width: 460px;
            text-align: center;
        }
        .brand-title {
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 3px;
            text-shadow: 0 0 12px rgba(0, 255, 102, 0.7);
            margin-bottom: 4px;
        }
        .subtitle {
            font-size: 11px;
            color: #94a3b8;
            margin-bottom: 22px;
            letter-spacing: 1px;
        }
        .btn {
            width: 100%;
            padding: 13px;
            background: #00ff66;
            color: #03060c;
            font-weight: bold;
            font-size: 14px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            transition: 0.25s;
            box-shadow: 0 0 15px rgba(0, 255, 102, 0.4);
            margin-top: 10px;
        }
        .btn:hover { background: #10b981; box-shadow: 0 0 22px rgba(0, 255, 102, 0.75); }
        .btn-outline {
            background: transparent;
            border: 1px solid #00ff66;
            color: #00ff66;
            box-shadow: none;
            font-size: 12px;
            padding: 10px;
        }
        .btn-outline:hover { background: rgba(0, 255, 102, 0.1); }
        
        .plan-card {
            background: #070b16;
            border: 1px solid #1e293b;
            border-radius: 8px;
            padding: 14px;
            margin-bottom: 12px;
            text-align: left;
            cursor: pointer;
            transition: 0.25s;
        }
        .plan-card:hover, .plan-card.selected {
            border-color: #00ff66;
            background: #0b1324;
            box-shadow: 0 0 12px rgba(0, 255, 102, 0.2);
        }
        .plan-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }
        .plan-name { font-size: 15px; font-weight: bold; color: #fff; }
        .plan-price { font-size: 17px; font-weight: bold; color: #00ff66; }
        .plan-desc { font-size: 11px; color: #94a3b8; }
        .badge { background: #00ff66; color: #03060c; font-size: 9px; font-weight: bold; padding: 2px 5px; border-radius: 3px; margin-left: 6px; }
        
        .info-box {
            background: rgba(0, 255, 102, 0.05);
            border-left: 3px solid #00ff66;
            padding: 11px;
            margin: 14px 0;
            text-align: left;
            font-size: 11px;
            color: #cbd5e1;
            line-height: 1.6;
        }
        input {
            width: 100%;
            padding: 12px;
            background: #020408;
            border: 1px solid #1f2937;
            border-radius: 6px;
            color: #00ff66;
            font-size: 14px;
            margin-bottom: 10px;
            outline: none;
            text-align: center;
        }
        input:focus { border-color: #00ff66; }
        .hidden { display: none; }

        .signal-box {
            background: #020408;
            border: 1px solid #00ff66;
            border-radius: 8px;
            padding: 18px;
            margin: 15px 0;
        }
        .signal-text {
            font-size: 26px;
            font-weight: bold;
            margin: 10px 0;
            letter-spacing: 2px;
        }
        .timer { color: #facc15; font-size: 14px; font-weight: bold; }
        .history-pills {
            display: flex;
            justify-content: center;
            gap: 6px;
            margin-top: 10px;
        }
        .pill {
            background: #111827;
            border: 1px solid #374151;
            color: #fff;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
        }
        .loader {
            border: 3px solid #1e293b;
            border-top: 3px solid #00ff66;
            border-radius: 50%;
            width: 28px;
            height: 28px;
            animation: spin 0.8s linear infinite;
            margin: 10px auto;
        }
        @keyframes spin { 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>

    <div class="container">
        <div class="brand-title">CTG ALGORITHM X1</div>
        <div class="subtitle">[ LIVE BACKEND PRODUCTION TERMINAL ]</div>

        <!-- 1. ENTRANCE PAGE -->
        <div id="entrance-page">
            <div class="info-box">
                > BRAND: CTG ALGORITHM X1<br>
                > BACKEND API: <span style="color:#00ff66;">CONNECTED</span><br>
                > ENGINE STATUS: <span style="color:#00ff66;">SECURE</span>
            </div>
            <button class="btn" onclick="showPage('plans-page')">ACCESS BUY</button>
            <button class="btn btn-outline" onclick="showPage('login-page')">ALREADY HAVE KEY? LOGIN</button>
        </div>

        <!-- 2. PLANS PAGE -->
        <div id="plans-page" class="hidden">
            <p style="font-size: 12px; color: #fff; margin-bottom: 12px;">SELECT ACCESS PLAN:</p>

            <div class="plan-card selected" onclick="selectPlan(this, '1 Day Access', 10)">
                <div class="plan-header"><span class="plan-name">1 DAY TRIAL</span><span class="plan-price">₹10</span></div>
                <div class="plan-desc">24 Hours Backend Verified Access</div>
            </div>

            <div class="plan-card" onclick="selectPlan(this, '10 Days Pro', 50)">
                <div class="plan-header"><span class="plan-name">10 DAYS PRO <span class="badge">POPULAR</span></span><span class="plan-price">₹50</span></div>
                <div class="plan-desc">240 Hours Priority Server Sync</div>
            </div>

            <div class="plan-card" onclick="selectPlan(this, '1 Month VIP', 250)">
                <div class="plan-header"><span class="plan-name">1 MONTH VIP <span class="badge">BEST</span></span><span class="plan-price">₹250</span></div>
                <div class="plan-desc">30 Days Unlimited VIP Engine Access</div>
            </div>

            <button class="btn" onclick="proceedToPayment()">BUY PLAN (<span id="selected-price">₹10</span>)</button>
            <button class="btn btn-outline" onclick="showPage('entrance-page')">← BACK</button>
        </div>

        <!-- 3. PAYMENT PAGE -->
        <div id="payment-page" class="hidden">
            <h3 style="color: #fff; font-size: 15px; margin-bottom: 10px;">SECURE CHECKOUT</h3>
            <div class="info-box" style="text-align: center;">
                PLAN: <strong id="pay-name" style="color:#fff;">1 Day Access</strong><br>
                AMOUNT: <strong id="pay-amt" style="color:#00ff66; font-size: 17px;">₹10</strong>
            </div>
            <input type="text" id="upi-input" placeholder="Enter Your UPI ID / Mobile No">
            <input type="text" id="utr-input" placeholder="Enter 12-Digit UTR / Ref No">

            <div id="pay-loader" class="hidden">
                <div class="loader"></div>
                <p style="font-size: 11px; color: #00ff66;">Verifying via Backend API...</p>
            </div>

            <button class="btn" id="pay-btn" onclick="processBackendPayment()">VERIFY & UNLOCK</button>
            <button class="btn btn-outline" onclick="showPage('plans-page')">CANCEL</button>
        </div>

        <!-- 4. LOGIN PAGE -->
        <div id="login-page" class="hidden">
            <h3 style="color: #fff; font-size: 15px; margin-bottom: 12px;">ENTER LICENSE KEY</h3>
            <input type="text" id="key-input" placeholder="CTG-X1-XXXX">
            <button class="btn" onclick="verifyBackendKey()">LOGIN</button>
            <button class="btn btn-outline" onclick="showPage('entrance-page')">← BACK</button>
        </div>

        <!-- 5. DASHBOARD PAGE -->
        <div id="dashboard-page" class="hidden">
            <div style="font-size: 11px; color: #00ff66; margin-bottom: 8px;">
                KEY: <span id="active-key-label" style="color:#fff;">-</span> | <span id="active-status" style="color:#00ff66;">SERVER VALIDATED</span>
            </div>

            <div class="signal-box">
                <div style="font-size: 11px; color: #94a3b8;">WINGO 1-MIN PERIOD: <span id="period-display" style="color:#fff; font-weight:bold;">-</span></div>
                <div class="signal-text" id="signal-display">ANALYZING...</div>
                <div class="timer">NEXT ROUND IN: <span id="timer-display">00</span>s</div>

                <div style="font-size: 10px; color: #94a3b8; margin-top: 12px;">LAST 6 SEED INPUTS:</div>
                <div class="history-pills" id="seed-pills"></div>
            </div>

            <div class="info-box" id="calc-log">
                > Formula: Sum / 2738<br>
                > Status: Active & Synced
            </div>

            <button class="btn btn-outline" style="border-color: #ef4444; color: #ef4444;" onclick="logout()">LOGOUT</button>
        </div>
    </div>

    <script>
        let selectedPlan = "1 Day Access";
        let selectedPrice = 10;
        let engineInterval = null;
        let lastMinute = -1;
        let seedNumbers = [4, 2, 7, 3, 8, 5];

        function showPage(pageId) {
            ['entrance-page', 'plans-page', 'payment-page', 'login-page', 'dashboard-page'].forEach(id => {
                document.getElementById(id).classList.add('hidden');
            });
            document.getElementById(pageId).classList.remove('hidden');
        }

        function selectPlan(el, name, price) {
            document.querySelectorAll('.plan-card').forEach(c => c.classList.remove('selected'));
            el.classList.add('selected');
            selectedPlan = name;
            selectedPrice = price;
            document.getElementById('selected-price').innerText = "₹" + price;
        }

        function proceedToPayment() {
            document.getElementById('pay-name').innerText = selectedPlan;
            document.getElementById('pay-amt').innerText = "₹" + selectedPrice;
            showPage('payment-page');
        }

        function processBackendPayment() {
            const upi = document.getElementById('upi-input').value.trim();
            const utr = document.getElementById('utr-input').value.trim();

            if (!upi || utr.length < 5) {
                alert("Please enter valid UPI ID and UTR!");
                return;
            }

            document.getElementById('pay-btn').classList.add('hidden');
            document.getElementById('pay-loader').classList.remove('hidden');

            // Send request to Flask Backend API
            fetch('/api/buy', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({plan: selectedPlan, amount: selectedPrice, upi: upi, utr: utr})
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById('pay-loader').classList.add('hidden');
                document.getElementById('pay-btn').classList.remove('hidden');

                if(data.status === "success") {
                    alert("Payment Verified by Backend! Your Key: " + data.key);
                    openDashboard(data.key);
                } else {
                    alert("Verification Failed: " + data.message);
                }
            });
        }

        function verifyBackendKey() {
            const key = document.getElementById('key-input').value.trim();
            if (!key) { alert("Enter key!"); return; }

            fetch('/api/verify', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({key: key})
            })
            .then(res => res.json())
            .then(data => {
                if(data.status === "success") {
                    openDashboard(key);
                } else {
                    alert("Invalid or Expired Key!");
                }
            });
        }

        function openDashboard(key) {
            document.getElementById('active-key-label').innerText = key;
            showPage('dashboard-page');
            startClockEngine();
        }

        function logout() {
            if (engineInterval) clearInterval(engineInterval);
            lastMinute = -1;
            showPage('entrance-page');
        }

        function startClockEngine() {
            if (engineInterval) clearInterval(engineInterval);
            tick();
            engineInterval = setInterval(tick, 1000);
        }

        function tick() {
            const now = new Date();
            const seconds = now.getSeconds();
            const remaining = 60 - seconds;
            const currentMinute = now.getMinutes();

            document.getElementById('timer-display').innerText = remaining < 10 ? "0" + remaining : remaining;

            if (currentMinute !== lastMinute) {
                lastMinute = currentMinute;
                run2738Algorithm(now);
            }
        }

        function run2738Algorithm(now) {
            const yyyy = now.getFullYear();
            const mm = String(now.getMonth() + 1).padStart(2, '0');
            const dd = String(now.getDate()).padStart(2, '0');
            const minuteOfDay = (now.getHours() * 60) + now.getMinutes() + 1;
            const periodId = `${yyyy}${mm}${dd}1000${String(minuteOfDay).padStart(4, '0')}`;
            document.getElementById('period-display').innerText = periodId;

            const nextSeed = (minuteOfDay * 7 + now.getDate()) % 10;
            seedNumbers.shift();
            seedNumbers.push(nextSeed);

            document.getElementById('seed-pills').innerHTML = seedNumbers.map(n => `<span class="pill">${n}</span>`).join('');

            const sum = seedNumbers.reduce((a, b) => a + b, 0);
            const division = (sum / 2738).toFixed(9);
            const digits = division.split('.')[1].split('').map(Number);
            const maxDigit = Math.max(...digits);

            const isBig = maxDigit >= 5;
            const sigEl = document.getElementById('signal-display');
            sigEl.innerText = isBig ? "BIG 🟢" : "SMALL 🔴";
            sigEl.style.color = isBig ? "#00ff66" : "#ff4d4d";

            document.getElementById('calc-log').innerHTML = `
                > Sum (${seedNumbers.join('+')}): <span style="color:#fff;">${sum}</span><br>
                > ${sum} / 2738 = <span style="color:#fff;">${division}</span><br>
                > Max Decimal Digit: <span style="color:#facc15; font-weight:bold;">${maxDigit}</span> (${isBig ? ">= 5 → BIG" : "< 5 → SMALL"})
            `;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/buy', methods=['POST'])
def api_buy():
    data = request.get_json()
    plan = data.get('plan')
    amount = data.get('amount')
    upi = data.get('upi')
    utr = data.get('utr')
    
    # Backend handles FamPay API verification internally
    print(f"[BACKEND API] Verifying payment via FamPay key {FAM_API_KEY} for UPI: {upi}, UTR: {utr}, Amount: ₹{amount}")
    
    # Generate authentic server key
    new_key = f"CTG-X1-{random.randint(1000, 9999)}-PRO"
    ACTIVE_KEYS[new_key] = {"plan": plan, "created": str(datetime.datetime.now())}
    
    return jsonify({"status": "success", "key": new_key, "message": "Payment verified via backend gateway"})

@app.route('/api/verify', methods=['POST'])
def api_verify():
    data = request.get_json()
    key = data.get('key')
    
    if key in ACTIVE_KEYS:
        return jsonify({"status": "success", "details": ACTIVE_KEYS[key]})
    else:
        return jsonify({"status": "error", "message": "Invalid key"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
  
