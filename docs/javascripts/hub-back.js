(function () {
  var style = document.createElement('style');
  style.textContent =
    '.lyh-hub-back{display:none}' +
    '@media (max-width:700px){' +
    '.lyh-hub-back{' +
    'display:inline-flex;align-items:center;gap:4px;' +
    'position:fixed;bottom:14px;left:14px;z-index:9999;' +
    'background:var(--md-default-bg-color);' +
    'color:var(--md-default-fg-color);' +
    "font:600 12px/1 var(--md-text-font-family,-apple-system,'Segoe UI',sans-serif);" +
    'padding:8px 14px;border-radius:20px;' +
    'border:1px solid var(--md-default-fg-color--lightest);' +
    'box-shadow:0 2px 8px rgba(0,0,0,.18);' +
    'text-decoration:none;' +
    '}}';
  document.head.appendChild(style);

  var a = document.createElement('a');
  a.href = 'https://leeyunhome.github.io/';
  a.className = 'lyh-hub-back';
  a.setAttribute('aria-label', '프로젝트 허브로 돌아가기');
  a.textContent = '← 허브';
  document.body.appendChild(a);
})();
