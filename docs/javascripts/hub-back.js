(function () {
  var style = document.createElement('style');
  style.textContent =
    '.lyh-hub-back{display:none}' +
    '@media (max-width:700px){' +
    '.lyh-hub-back{' +
    'display:inline-flex;align-items:center;gap:4px;' +
    'position:fixed;top:10px;left:10px;z-index:9999;' +
    'background:rgba(15,17,23,.85);color:#e2e6f0;' +
    "font:600 12px/1 -apple-system,'Segoe UI',sans-serif;" +
    'padding:6px 12px;border-radius:20px;' +
    'border:1px solid rgba(255,255,255,.15);' +
    'text-decoration:none;-webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px);' +
    '}}';
  document.head.appendChild(style);

  var a = document.createElement('a');
  a.href = 'https://leeyunhome.github.io/';
  a.className = 'lyh-hub-back';
  a.setAttribute('aria-label', '프로젝트 허브로 돌아가기');
  a.textContent = '← 허브';
  document.body.appendChild(a);
})();
