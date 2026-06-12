with open(\"app/__init__.py\", \"r\", encoding=\"utf-8\") as f: content = f.read()
old_home = \"\"\"@app.route(\"/\\ndef home():\\n\\titems = Item.query.all()\\n\\treturn render_template(\"home.html\", items=items)\"\"\"
old_home = old_home.replace(\"(\"/\\n\", \"(\\\"/\\\")\\n\")
new_home = \"\"\"@app.route(\"/\\\")\\ndef home():\\n    page = request.args.get(\"page\", 1, type=int)\\n    items = Item.query.paginate(page=page, per_page=8)\\n    return render_template(\"home.html\", items=items)\"\"\"
content = content.replace(old_home, new_home)
