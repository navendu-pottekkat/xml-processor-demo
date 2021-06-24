from xml.dom import minidom

doc = minidom.parse("student_details.xml")

students = doc.getElementsByTagName("student")

for student in students:
    name = student.getElementsByTagName("name")[0].firstChild.data
    house = student.getElementsByTagName("house")[0].firstChild.data
    description = student.getElementsByTagName("description")[
        0].firstChild.data

    print(f"{name} of house {house} {description}.")
