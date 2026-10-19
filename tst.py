from flask import Flask, render_template_string
from jinja2 import DictLoader

app = Flask(__name__)

BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        /* Bare minimum styling applied only to the base template */
        body { font-family: monospace; margin: 40px; background: #f4f4f4; color: #333; }
        header { border-bottom: 2px solid #333; padding-bottom: 10px; margin-bottom: 20px; }
        table { border-collapse: collapse; width: 100%; background: #fff; }
        th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: left; }
        th { background: #eee; }
    </style>
</head>
<body>
    <header>
        <h1>Flask Concept Demo: {{ subtitle }}</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
"""

HOME_TEMPLATE = """
{% extends "base" %}
{% block content %}
    <h2>{{ section_title }}</h2>
    <p>This table displays items passed from Python code via a list of dictionaries using a Jinja loop:</p>
    
    <table>
        <thead>
            <tr>
                <th>{{ col_id }}</th>
                <th>{{ col_name }}</th>
                <th>{{ col_role }}</th>
                <th>{{ col_status }}</th>
            </tr>
        </thead>
        <tbody>
            {% for user in users %}
            <tr>
                <td>{{ user.id }}</td>
                <td>{{ user.name }}</td>
                <td>{{ user.role }}</td>
                <td>{{ user.status }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
"""

app.jinja_loader = DictLoader({
    "base": BASE_TEMPLATE,
    "home": HOME_TEMPLATE
})

@app.route('/')
def home():
    # Dummy data: List of dictionaries to demonstrate looping and variable binding in Flask
    dummy_users = [
        {"id": 1, "name": "Alice Smith", "role": "Developer", "status": "Active"},
        {"id": 2, "name": "Bob Jones", "role": "Designer", "status": "Away"},
        {"id": 3, "name": "Charlie Brown", "role": "Admin", "status": "Active"},
        {"id": 4, "name": "Diana Prince", "role": "Tester", "status": "Offline"}
    ]
    
    # Passing variables, labels, and lists to the template
    return render_template_string(
        "{% include 'home' %}",
        title="Flask Educational App",
        subtitle="Inline Rendering & Jinja Concepts",
        section_title="User Directory (Dummy Data Grid)",
        col_id="ID Label",
        col_name="Name Label",
        col_role="Role Label",
        col_status="Status Label",
        users=dummy_users
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)