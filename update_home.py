content = open('app/templates/home.html', 'r', encoding='utf-8').read()
content = content.replace('{% for item in items[::-1] %}', '{% for item in items.items[::-1] %}')
content = content.replace('{% for item in items %}', '{% for item in items.items %}')
content = content.replace('{% if not items %}', '{% if not items.items %}')

pagination_html = """
    <div class="mt-4 text-center">
        {% if items.has_prev %}
            <a href="{{ url_for('home', page=items.prev_num) }}" class="btn btn-outline-info">Geri</a>
        {% endif %}
        {% for page_num in items.iter_pages(left_edge=1, right_edge=1, left_current=1, right_current=2) %}
            {% if page_num %}
                {% if items.page == page_num %}
                    <a href="{{ url_for('home', page=page_num) }}" class="btn btn-info">{{ page_num }}</a>
                {% else %}
                    <a href="{{ url_for('home', page=page_num) }}" class="btn btn-outline-info">{{ page_num }}</a>
                {% endif %}
            {% else %}
                <span class="btn btn-outline-secondary disabled">...</span>
            {% endif %}
        {% endfor %}
        {% if items.has_next %}
            <a href="{{ url_for('home', page=items.next_num) }}" class="btn btn-outline-info">İleri</a>
        {% endif %}
    </div>
"""
content = content.replace('{% if not items.items %}', pagination_html + '\n\n\t{% if not items.items %}')
open('app/templates/home.html', 'w', encoding='utf-8').write(content)