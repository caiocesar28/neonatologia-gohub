import os
import re

source_file = r"C:\Users\Caio\.gemini\antigravity\scratch\neonatologia-gohub\index.html"
with open(source_file, "r", encoding="utf-8", errors="ignore") as f:
    orig = f.read()

# Extract the base64 logos
band_m = re.search(r'(const LOGO_BAND\s*=\s*\"[^\"]+\";)', orig)
uh_m   = re.search(r'(const LOGO_UH\s*=\s*\"[^\"]+\";)', orig)
ses_m  = re.search(r'(const LOGO_SES\s*=\s*\"[^\"]+\";)', orig)
ue_m   = re.search(r'(const LOGO_UE\s*=\s*\"[^\"]+\";)', orig)

logo_band_line = band_m.group(1) if band_m else ""
logo_uh_line   = uh_m.group(1) if uh_m else ""
logo_ses_line  = ses_m.group(1) if ses_m else ""
logo_ue_line   = ue_m.group(1) if ue_m else ""

template_file = r"C:\Users\Caio\.gemini\antigravity\scratch\neonatologia-gohub\template.html"
with open(template_file, "r", encoding="utf-8") as f:
    tmpl = f.read()

tmpl = tmpl.replace("/*__LOGO_BAND__*/", logo_band_line)
tmpl = tmpl.replace("/*__LOGO_UH__*/", logo_uh_line)
tmpl = tmpl.replace("/*__LOGO_SES__*/", logo_ses_line)
tmpl = tmpl.replace("/*__LOGO_UE__*/", logo_ue_line)

output_file = r"C:\Users\Caio\.gemini\antigravity\scratch\neonatologia-gohub\index.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(tmpl)

print("Generated neonatologia index.html successfully! Size:", len(tmpl))
