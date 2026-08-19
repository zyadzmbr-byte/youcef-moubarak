import os
import re

dir_path = r"c:\webs\يوسف مبارك"

def replace_in_file(file_path):
    encodings = ['utf-8', 'utf-16le', 'cp1256']
    content = None
    used_encoding = None
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                content = f.read()
            used_encoding = enc
            break
        except UnicodeDecodeError:
            pass

    if content is None:
        print(f"Skipping {file_path} due to encoding issues.")
        return

    # 1. Branding replacements
    content = re.sub(r'منصة التبيان التعليمية', "منصة يوسف مبارك التعليمية", content)
    content = re.sub(r'منصة التبيان', "منصة يوسف مبارك", content)
    content = re.sub(r'التبيان', "يوسف مبارك", content)
    content = re.sub(r'Spedia', "يوسف مبارك", content)
    
    # Mohamed Hosny branding
    content = re.sub(r'منصة محمد حسني التعلمية', "منصة يوسف مبارك التعليمية", content)
    content = re.sub(r'منصة محمد حسني', "منصة يوسف مبارك", content)
    content = re.sub(r'مستر محمد حسني', "مستر يوسف مبارك", content)
    content = re.sub(r'محمد حسني', "يوسف مبارك", content)
    
    # Earlier branding
    content = re.sub(r'منصة professor التعليمية', "منصة يوسف مبارك التعليمية", content)
    content = re.sub(r'منصة professor', "منصة يوسف مبارك", content)
    content = re.sub(r'Prof\.Ramy Elkhayat', "مستر يوسف مبارك", content)
    content = re.sub(r'Prof\. Ramy Elkhayat', "مستر يوسف مبارك", content)
    content = re.sub(r'Ramy Elkhayat', "يوسف مبارك", content)
    content = re.sub(r'Senior English Teacher', "", content)
    content = re.sub(r'اللغة الإنجليزية', "اللغة العربية", content)
    content = re.sub(r'اللغه الانجليزيه', "اللغة العربية", content)
    content = re.sub(r'01016058274', "01228731752", content)
    content = re.sub(r'logo\.png', "hero.jpg", content)
    content = re.sub(r'logo\.jpg', "hero.jpg", content) 
    content = re.sub(r'hosny\.jpg', "hero.jpg", content) 
    
    # Facebook replacing Youtube
    if 'index.html' in file_path:
        content = re.sub(r'href="https://youtube[^"]*"', 'href="https://www.facebook.com/share/1HbZF7fWTt/"', content)
        content = content.replace('class="fab fa-youtube"', 'class="fab fa-facebook-f"')
        content = content.replace('background: #ff0000;', 'background: #1877f2;')
        content = content.replace('<p style="font-size:18px; margin-top:-10px; color:#12b8c5; font-weight:bold;">Senior English Teacher</p>', '')

    # Admin panel bugs
    if 'admin.html' in file_path:
        # Code generation await and removing renderTables
        code_bug_target = """            if (window.fsData && window.fsData.addCode) {
                window.fsData.addCode(codeObj).catch(er => console.error("Firebase Add Code Error:", er));
            }"""
        code_bug_replacement = """            if (window.fsData && window.fsData.addCode) {
                try {
                    await window.fsData.addCode(codeObj);
                } catch(er) {
                    console.error("Firebase Add Code Error:", er);
                }
            }"""
        content = content.replace(code_bug_target, code_bug_replacement)
        content = content.replace("            alert('تم توليد الكود بنجاح: ' + c);\n            window.renderTables();", "            alert('تم توليد الكود بنجاح: ' + c);")
        
        # ex-country bug
        content = content.replace("country: document.getElementById('ex-country').value,", "country: document.getElementById('ex-country') ? document.getElementById('ex-country').value : 'EG',")
        
        # af-country bug
        content = content.replace("country: document.getElementById('af-country').value,", "country: document.getElementById('af-country') ? document.getElementById('af-country').value : 'EG',")
        
        # video direct upload removal
        vid_target = """                <div class="form-group">
                    <label>رفع الفيديو (اختياري)</label>
                    <input type="file" id="ct-yt" accept="video/*">
                </div>"""
        content = content.replace(vid_target, "")
        
        vid_js_target = """                    if (ytLinkEl && ytLinkEl.value.trim() !== '') {
                        newItem.videoUrl = ytLinkEl.value.trim();
                    } else if (ytEl && ytEl.files && ytEl.files[0]) {
                        try {
                            btn.innerText = "جاري رفع الفيديو... (يرجى عدم إغلاق الصفحة)";
                            newItem.videoUrl = await window.uploadToCloudinary(ytEl.files[0]);
                        } catch (e) {
                            throw new Error("فشل رفع فيديو الكورس: " + e.message);
                        }
                    }"""
        vid_js_replacement = """                    if (ytLinkEl && ytLinkEl.value.trim() !== '') {
                        newItem.videoUrl = ytLinkEl.value.trim();
                    }"""
        content = content.replace(vid_js_target, vid_js_replacement)

    with open(file_path, 'w', encoding=used_encoding) as f:
        f.write(content)

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(('.html', '.js', '.css')):
            replace_in_file(os.path.join(root, file))
print("Done fixing all bugs.")
