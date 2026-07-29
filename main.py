print("hi meir")
print ("hi")
from flask import Flask, render_template_string

app = Flask(__name__)

dashboard_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background: #f2f2f2;}
        .header { padding: 30px; background: #2d4154; color: white; text-align: center;}
        .container { margin: 40px auto; max-width: 900px; background: white; padding: 32px; border-radius: 8px; box-shadow: 0 0 18px #0002;}
        .card-grid { display: flex; gap: 24px; flex-wrap: wrap;}
        .card { flex:1 1 220px; background: #e5eefa; padding: 24px; border-radius: 8px; box-shadow: 0 2px 8px #0001;}
        .card-title { font-size: 1.2rem; margin-bottom: 12px;}
        .value { font-size: 2rem; color: #255394;}
        .footer { padding: 24px; background: #222; color: #ccc; text-align: center; margin-top:40px;}
        @media (max-width:700px) {
            .card-grid { flex-direction: column; }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Dashboard</h1>
        <p>Welcome to your analytics dashboard!</p>
    </div>
    <div class="container">
        <div class="card-grid">
            <div class="card">
                <div class="card-title">Users</div>
                <div class="value">{{ users }}</div>
            </div>
            <div class="card">
                <div class="card-title">Revenue</div>
                <div class="value">${{ revenue }}</div>
            </div>
            <div class="card">
                <div class="card-title">Active Sessions</div>
                <div class="value">{{ sessions }}</div>
            </div>
        </div>
    </div>
    <div class="footer">
        &copy; 2024 Dashboard, Inc.
    </div>
</body>
</html>
"""

@app.route('/')
def dashboard():
    # Example data - you can replace with real data source
    data = {
        "users": 1524,
        "revenue": "12,830",
        "sessions": 421
    }
    return render_template_string(dashboard_template, **data)

if __name__ == '__main__':
    app.run(debug=True)