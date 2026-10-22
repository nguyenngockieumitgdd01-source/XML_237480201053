import xml.etree.ElementTree as ET
import os

# Doc tap tin XML
duongdan = os.path.dirname(os.path.abspath(__file__))
tree = ET.parse(os.path.join(duongdan, "danhsach.xml"))
root = tree.getroot()

# Tim sinh vien co ma 14DTH02 va sua thong tin
for student in root.findall("student"):
    masv = student.get("id")

    if masv == "14DTH02":
        student.find("name").text = "Nguyen Van Nam"
        student.find("date").text = "10-10-2002"
        student.find("city").text = "Ho Chi Minh"

        print("Da sua thong tin sinh vien thanh cong!")
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