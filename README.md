# Portfolio — 이윤호 · Applied AI Engineer

MkDocs Material 기반 포트폴리오. GitHub Actions로 자동 빌드/배포됩니다.

**Live**: https://leeyunhome.github.io/portfolio/

## 로컬 개발

```bash
pip install -r requirements.txt
mkdocs serve
# → http://127.0.0.1:8000
```

## 배포

`main` 브랜치 push 시 GitHub Actions가 자동으로 `gh-pages` 브랜치에 빌드 결과를 배포합니다.
GitHub Pages 설정에서 Source를 `gh-pages` 브랜치로 지정해야 합니다.
