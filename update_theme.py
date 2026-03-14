import re

with open('/Users/chandrakanthreddydasari/Downloads/IPL/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Tailwind config colors
html = html.replace("navy: '#0F172A'", "navy: 'var(--brand-navy)'")
html = html.replace("darker: '#020617'", "darker: 'var(--brand-darker)'")
html = html.replace("accent: '#F97316'", "accent: 'var(--brand-accent)'")
html = html.replace("muted: '#1E293B'", "muted: 'var(--brand-muted)'")
html = html.replace("text: '#94A3B8'", "text: 'var(--brand-text)'")
html = html.replace("surface: '#1E293B'", "surface: 'var(--brand-surface)'")

# Add new custom colors to Tailwind config
html = re.sub(r'(surface: \'var\(--brand-surface\)\',)', r"\g<1>\n              primary: 'var(--brand-primary)',\n              overlay: 'var(--brand-overlay)',\n              overlay2: 'var(--brand-overlay2)',", html)

# Add custom properties to the :root, [data-theme=\"dark\"] block
css_dark = """
    :root, [data-theme="dark"] {
      --brand-navy: #0F172A;
      --brand-darker: #020617;
      --brand-accent: #F97316;
      --brand-muted: #1E293B;
      --brand-text: #94A3B8;
      --brand-surface: #1E293B;
      --brand-primary: #ffffff;
      --brand-overlay: rgba(255, 255, 255, 0.05);
      --brand-overlay2: rgba(255, 255, 255, 0.2);
"""
html = re.sub(r'(:root, \[data-theme="dark"\] \{\n)', css_dark, html)

# Add custom properties to the [data-theme=\"light\"] block
css_light = """
    [data-theme="light"] {
      --brand-navy: #CBD5E1;
      --brand-darker: #F1F5F9;
      --brand-accent: #EA580C;
      --brand-muted: #FFFFFF;
      --brand-text: #475569;
      --brand-surface: #E2E8F0;
      --brand-primary: #0F172A;
      --brand-overlay: rgba(0, 0, 0, 0.05);
      --brand-overlay2: rgba(0, 0, 0, 0.2);
"""
html = re.sub(r'(\[data-theme="light"\] \{\n)', css_light, html)

# Perform bulk class replacements
html = html.replace("text-white", "text-brand-primary")
html = html.replace("hover:text-white", "hover:text-brand-primary")
html = html.replace("bg-white/5", "bg-brand-overlay")
html = html.replace("border-white/10", "border-brand-overlay")
html = html.replace("border-white/20", "border-brand-overlay2")
html = html.replace("border-white/5", "border-brand-overlay")

with open('/Users/chandrakanthreddydasari/Downloads/IPL/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
