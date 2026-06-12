content = open('app/templates/base.html', 'r', encoding='utf-8').read()
content = content.replace('Siparişler</a>', 'Siparişler</a>\n              <a class="nav-link" href="{{ url_for(\'user_profile\') }}">Profilim</a>')
open('app/templates/base.html', 'w', encoding='utf-8').write(content)