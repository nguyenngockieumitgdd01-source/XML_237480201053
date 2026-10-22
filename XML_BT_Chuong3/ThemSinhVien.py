import xml.etree.ElementTree as ET
import os

# Doc tap tin XML
duongdan = os.path.dirname(os.path.abspath(__file__))
file_xml = os.path.join(duongdan, "danhsach.xml")

tree = ET.parse(file_xml)
root = tree.getroot()

# Nhap thong tin sinh vien can them lai
masv = input("Nhap ma sinh vien: ")
hoten = input("Nhap ho ten: ")
ngaysinh = input("Nhap ngay sinh (dd-mm-yyyy): ")
thanhpho = input("Nhap thanh pho: ")

# Kiem tra sinh vien da ton tai chua
for student in root.findall("student"):
    if student.get("id") == masv:
        print("Sinh vien nay da ton tai!")
        break
else:
    # Tao sinh vien moi
    student = ET.Element("student", id=masv)

    name = ET.SubElement(student, "name")
    name.text = hoten

    date = ET.SubElement(student, "date")
    date.text = ngaysinh

    city = ET.SubElement(student, "city")
    city.text = thanhpho

    # Them vao danh sach
    root.append(student)

    # Luu file XML
    ET.indent(tree, space="    ")
    tree.write(
        file_xml,
        encoding="utf-8",
        xml_declaration=True
    )

    print("Da them lai sinh vien thanh cong!")