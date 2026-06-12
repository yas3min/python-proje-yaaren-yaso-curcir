content = open(\"app/templates/login.html\", \"r\", encoding=\"utf-8\").read()
link = \"<a href=\" + chr(34) + \"{{ url_for('reset_request') }}\" + chr(34) + \">Sifremi Unuttum</a><br><br>\\n    </form>\"
content = content.replace(\"</form>\", link)
open(\"app/templates/login.html\", \"w\", encoding=\"utf-8\").write(content)
