
import xml.etree.ElementTree as ET
import os

# Doc tap tin XML
duongdan = os.path.dirname(os.path.abspath(__file__))
tree = ET.parse(os.path.join(duongdan, "danhsach.xml"))
root = tree.getroot()

# Tim sinh vien co ma 14DTH02 va xoa
for student in root.findall("student"):
    masv = student.get("id")

    if masv == "14DTH03":
        root.remove(student)
        print("Da xoa sinh vien thanh cong!")
        break
else:
    print("Khong tim thay sinh vien!")

# Luu lai file XML
ET.indent(tree, space="    ")
tree.write(
    os.path.join(duongdan, "danhsach.xml"),
    encoding="utf-8",
    xml_declaration=True
)