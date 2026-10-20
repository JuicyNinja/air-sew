/*
 * Local preview shim for the Air Sew mockup files (*.dc.html).
 *
 * The mockups were authored on a design canvas that renders <x-dc> templates:
 *   - {{name}} holes are filled from the Component's renderVals()
 *   - onClick="{{fn}}" / onInput="{{fn}}" bind event handlers
 *   - <sc-for list="{{items}}" as="s"> repeats its body per item ({{s.field}})
 *   - <helmet> content belongs in <head>
 * This file reimplements just enough of that so the mockups open in a normal
 * browser. It is a viewing aid only: build the real site from the markup,
 * not from this shim.
 */
(function () {
  function start() {
    var host = document.querySelector('x-dc');
    if (!host) return;
    var helmet = host.querySelector('helmet');
    if (helmet) { while (helmet.firstChild) document.head.appendChild(helmet.firstChild); helmet.remove(); }
    var template = host.innerHTML;
    var scriptEl = document.querySelector('script[data-dc-script]');
    var props = {};
    try { props = JSON.parse(scriptEl.getAttribute('data-props') || '{}'); } catch (e) {}

    function DCLogic(p) { this.props = p || {}; this.state = {}; }
    DCLogic.prototype.setState = function (patch) {
      var next = typeof patch === 'function' ? patch(this.state) : patch;
      this.state = Object.assign({}, this.state, next);
      render();
    };
    var Component = new Function('DCLogic', scriptEl.textContent + '\nreturn Component;')(DCLogic);
    var inst = new Component(props);
    if (!inst.state) inst.state = {};

    var handlers = [];
    function val(v) {
      if (typeof v === 'function') { handlers.push(v); return '__dc_fn_' + (handlers.length - 1); }
      return v == null ? '' : String(v);
    }
    function fill(html, vals, prefix) {
      return html.replace(/\{\{\s*([\w.]+)\s*\}\}/g, function (m, key) {
        if (prefix) {
          if (key.indexOf(prefix + '.') !== 0) return m;
          return val(vals[key.slice(prefix.length + 1)]);
        }
        return key in vals ? val(vals[key]) : m;
      });
    }
    function render() {
      handlers = [];
      var vals = inst.renderVals() || {};
      var html = template.replace(/<sc-for\s+list="\{\{\s*(\w+)\s*\}\}"\s+as="(\w+)"[^>]*>([\s\S]*?)<\/sc-for>/g,
        function (m, listName, as, body) {
          return (vals[listName] || []).map(function (item) { return fill(body, item, as); }).join('');
        });
      html = fill(html, vals);
      var active = document.activeElement, activeIdx = -1;
      var all = host.querySelectorAll('input,button,textarea,select');
      for (var i = 0; i < all.length; i++) if (all[i] === active) activeIdx = i;
      host.innerHTML = html;
      host.querySelectorAll('*').forEach(function (el) {
        Array.prototype.slice.call(el.attributes).forEach(function (a) {
          var m = /^__dc_fn_(\d+)$/.exec(a.value);
          if (m && a.name.indexOf('on') === 0) {
            el.removeAttribute(a.name);
            el.addEventListener(a.name.slice(2), handlers[+m[1]]);
          } else if (m) { el.removeAttribute(a.name); }
        });
      });
      if (activeIdx >= 0) { var again = host.querySelectorAll('input,button,textarea,select')[activeIdx]; if (again) again.focus(); }
    }
    render();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
