"""Inspect only approved official C04 source-page schema/coverage metadata."""
import json
import re
from urllib.parse import urljoin
import v1_c04_extend_2025 as x


def main():
    for kind, url in x.old.SSE_REFERERS.items():
        body, headers = x.fetch(url, 'https://www.sse.com.cn/')
        text = x.old.decode_html(body, headers)
        scripts = [urljoin(url, s) for s in re.findall(r'<script[^>]+src=["\x27]([^"\x27]+)', text)]
        scripts += [urljoin(url, s) for s in re.findall(r'js_files=["\x27]([^"\x27]+)', text)]
        print(json.dumps({'kind': kind, 'url': url, 'scripts': scripts,
                          'coverage_notices': [s.strip()[:600] for s in text.splitlines() if any(k in s for k in ('2021', '2022', '停止', '暂停'))]}, ensure_ascii=False), flush=True)
        for script in scripts:
            if not any(k in script for k in ('dividend', 'bonus', 'overview', 'raise', 'querySearch')): continue
            b, h = x.fetch(script, url)
            js = x.old.decode_html(b, h)
            print(json.dumps({'script': script, 'schema_lines': [s.strip()[:700] for s in js.splitlines()
                             if any(k in s for k in ('sqlId', 'year', 'Year', '2021', '2022', 'record_date', 'searchyear'))]}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
